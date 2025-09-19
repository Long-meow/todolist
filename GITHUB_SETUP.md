# GitHub Setup Guide

## Step 1: Initialize Git Repository

```bash
cd /path/to/your/flask-todo-app
git init
git add .
git commit -m "Initial commit: Flask To-Do App"
```

## Step 2: Create GitHub Repository

1. Go to [GitHub.com](https://github.com)
2. Click "+" → "New repository"
3. Name: `flask-todo-app`
4. Description: `Flask To-Do List Application`
5. Make it Public or Private
6. **DO NOT** check "Initialize with README"
7. Click "Create repository"

## Step 3: Connect to GitHub

```bash
git remote add origin https://github.com/YOUR_USERNAME/flask-todo-app.git
git branch -M main
git push -u origin main
```

## Step 4: Update README

Edit `README.md` and replace:
- `yourusername` with your GitHub username
- Update repository URL if needed

## Step 5: Push Updates

```bash
git add .
git commit -m "Update project"
git push origin main
```

Your Flask To-Do App is now on GitHub! 🎉

## Running Locally

```bash
git clone https://github.com/YOUR_USERNAME/flask-todo-app.git
cd flask-todo-app
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python run.py
```
