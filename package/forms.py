from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, SubmitField, IntegerField, HiddenField, TextAreaField, DateTimeLocalField, BooleanField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError, Optional
from package.models import User
from datetime import datetime

class RegistrationForm(FlaskForm): 
  def validate_username(self, username):
    user = User.query.filter_by(username=username.data).first() 
    if user: 
      raise ValidationError('That username is taken. Please choose a different one.')
  
  username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
  password = PasswordField('Password', validators=[DataRequired()])
  confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
  submit = SubmitField('Sign Up')
  
class LoginForm(FlaskForm): 
  username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
  password = PasswordField('Password', validators=[DataRequired()])
  submit = SubmitField('Login') 
  
class TaskForm(FlaskForm): 
  title = StringField('Title', validators=[DataRequired(), Length(min=1, max=100)])
  description = TextAreaField('Description', validators=[Optional(), Length(max=500)])
  date = DateTimeLocalField('Due Date', validators=[DataRequired()], default=datetime.now)
  completed = BooleanField('Completed', default=False)
  submit = SubmitField('Add Task')

class UpdateTaskForm(FlaskForm):
  id = HiddenField('Task ID')
  title = StringField('Title', validators=[DataRequired(), Length(min=1, max=100)])
  description = TextAreaField('Description', validators=[Optional(), Length(max=500)])
  date = DateTimeLocalField('Due Date', validators=[DataRequired()])
  completed = BooleanField('Completed')
  submit = SubmitField('Update Task')

class DeleteTaskForm(FlaskForm):
  id = HiddenField('Task ID')
  submit = SubmitField('Delete Task')