# Flask To-Do List App

A modern, responsive to-do list application built with Flask and Bootstrap.

## Features

- User Registration and Authentication
- Create, Read, Update, Delete Tasks
- Task Completion Toggle
- Due Date Management
- Task Descriptions
- Responsive Bootstrap UI
- Modal Forms

## Technology Stack

- **Backend**: Flask, SQLAlchemy, Flask-Login
- **Frontend**: Bootstrap 5, Font Awesome Icons
- **Database**: MySQL
- **Authentication**: Flask-Login with Bcrypt

## Installation

1. Clone the repository
   ```bash
   git clone https://github.com/yourusername/flask-todo-app.git
   cd flask-todo-app
   ```

2. Create virtual environment
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

4. Setup database
   ```sql
   CREATE DATABASE totolist;
   ```

5. Run migrations
   ```bash
   flask db init
   flask db migrate -m "Initial migration"
   flask db upgrade
   ```

6. Run the application
   ```bash
   python run.py
   ```

## Usage

1. Register a new account or Login
2. Create tasks using "Add New Task" button
3. Edit tasks by clicking "Edit" button
4. Mark tasks complete using checkbox
5. Delete tasks using "Delete" button

## Project Structure

```
flask-todo-app/
├── package/
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   ├── forms.py
│   └── templates/
├── migrations/
├── run.py
└── requirements.txt
```

## License

MIT License