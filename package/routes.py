from flask import render_template, url_for, flash, redirect, request, jsonify
from package import app, db, bcrypt
from package.forms import RegistrationForm, LoginForm, TaskForm, UpdateTaskForm, DeleteTaskForm
from package.models import User, Task 
from flask_login import login_user, current_user, logout_user, login_required
from datetime import datetime 

@app.route('/') 
@app.route('/home') 
def home():
  return render_template('home.html') 

@app.route('/register', methods=['GET', 'POST'] )
def register(): 
  register_form = RegistrationForm() 
  if request.method == 'POST' and register_form.validate_on_submit(): 
    new_user = User(username = register_form.username.data, password = register_form.password.data)
    
    db.session.add(new_user)
    db.session.commit()
    login_user(new_user)
    flash(f"Welcome {new_user.username}!", category='success alert fade show')
    return redirect(url_for('home'))
  if register_form.errors != {}: 
    for err_msg in register_form.errors.values(): 
      flash(f"There was an error in creating user {err_msg}", category="danger")
  return render_template('register.html', register_form = register_form) 

@app.route('/login', methods=['GET', 'POST'])
def login():
  login_form = LoginForm() 
  if request.method == 'POST' and login_form.validate_on_submit(): 
    attempted_user = User.query.filter_by(username = login_form.username.data).first() 
    if attempted_user and attempted_user.check_password(login_form.password.data):
      flash(f'You have successfully login as {attempted_user.username}', category="success alert fade show")
      login_user(attempted_user)
      return redirect(url_for('home'))
    else: 
      flash('Username or password is not match! Please try again', category="danger")
  return render_template('login.html', login_form = login_form)

@app.route('/tasks')
@login_required 
def tasks():
  tasks = Task.query.filter_by(user_id=current_user.id).order_by(Task.created_at.desc()).all()
  add_task_form = TaskForm()
  return render_template('tasks.html', tasks=tasks, add_task_form=add_task_form)

@app.route('/add_task', methods=['POST'])
@login_required
def add_task():
  title = request.form.get('title')
  description = request.form.get('description', '')
  date_str = request.form.get('date')
  
  if not title or not date_str:
    flash("Title and date are required.", category="danger")
    return redirect(url_for('tasks'))
  
  try:
    from datetime import datetime
    task_date = datetime.fromisoformat(date_str)
    
    new_task = Task(
      title=title,
      description=description,
      date=task_date,
      user_id=current_user.id
    )
    db.session.add(new_task)
    db.session.commit()
    flash(f"Task '{new_task.title}' has been added!", category="success")
    return redirect(url_for('tasks'))
  except ValueError as e:
    flash("Invalid date format. Please check your input.", category="danger")
    return redirect(url_for('tasks'))
  except Exception as e:
    flash("Error adding task. Please try again.", category="danger")
    return redirect(url_for('tasks'))

@app.route('/update_task/<int:task_id>', methods=['POST'])
@login_required
def update_task(task_id):
  task = Task.query.get_or_404(task_id)
  if task.user_id != current_user.id:
    flash("You don't have permission to update this task.", category="danger")
    return redirect(url_for('tasks'))
  
  title = request.form.get('title')
  description = request.form.get('description', '')
  date_str = request.form.get('date')
  completed = request.form.get('completed') == 'y'
  
  if not title or not date_str:
    flash("Title and date are required.", category="danger")
    return redirect(url_for('tasks'))
  
  try:
    from datetime import datetime
    task_date = datetime.fromisoformat(date_str)
    
    task.title = title
    task.description = description
    task.date = task_date
    task.completed = completed
    db.session.commit()
    flash(f"Task '{task.title}' has been updated!", category="success")
    return redirect(url_for('tasks'))
  except ValueError as e:
    flash("Invalid date format. Please check your input.", category="danger")
    return redirect(url_for('tasks'))
  except Exception as e:
    flash("Error updating task. Please try again.", category="danger")
    return redirect(url_for('tasks'))

@app.route('/delete_task/<int:task_id>', methods=['POST'])
@login_required
def delete_task(task_id):
  task = Task.query.get_or_404(task_id)
  if task.user_id != current_user.id:
    flash("You don't have permission to delete this task.", category="danger")
    return redirect(url_for('tasks'))
  
  try:
    task_title = task.title
    db.session.delete(task)
    db.session.commit()
    flash(f"Task '{task_title}' has been deleted!", category="success")
  except Exception as e:
    db.session.rollback()
    flash("Error deleting task. Please try again.", category="danger")
  
  return redirect(url_for('tasks'))

@app.route('/toggle_task/<int:task_id>', methods=['POST'])
@login_required
def toggle_task(task_id):
  task = Task.query.get_or_404(task_id)
  if task.user_id != current_user.id:
    return jsonify({'error': 'Permission denied'}), 403
  
  try:
    task.completed = not task.completed
    db.session.commit()
    return jsonify({'success': True, 'completed': task.completed})
  except Exception as e:
    db.session.rollback()
    return jsonify({'error': 'Failed to update task'}), 500 

@app.route('/logout') 
def logout():
  logout_user()
  flash("You have been logged out!", category="success alert fade show")
  return redirect(url_for('home'))