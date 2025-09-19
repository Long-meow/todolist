from package import db, login_manager, bcrypt 
from flask_login import UserMixin
from datetime import datetime 

@login_manager.user_loader 
def load_user(user_id):
  return User.query.get(int(user_id)) 

class User(db.Model, UserMixin): 
  id = db.Column(db.Integer, primary_key=True) 
  username = db.Column(db.String(20), unique=True, nullable=False) 
  image_file = db.Column(db.String(20), nullable=False, default='default.jpg') 
  password_hash = db.Column(db.String(60), nullable=False) 
  tasks = db.relationship('Task', backref='author', lazy=True)

  @property 
  def password(self): 
    return self.password 
  
  @password.setter 
  def password(self, password): 
    self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')    
    
  def check_password(self, password): 
    return bcrypt.check_password_hash(self.password_hash, password) 
  
  
  def __repr__(self): 
    return f"User('{self.username}', '{self.email}', '{self.image_file}')"
  
class Task(db.Model): 
  id = db.Column(db.Integer, primary_key=True, nullable=False)
  title = db.Column(db.String(500), nullable=False) 
  description = db.Column(db.Text, nullable=True)
  date = db.Column(db.DateTime, nullable=False) 
  completed = db.Column(db.Boolean, default=False, nullable=False)
  created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
  
  def __repr__(self):
    return f"Task('{self.title}', '{self.date}', '{self.completed}')" 
  