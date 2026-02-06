from flask import Flask, render_template, redirect, url_for, flash, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash
import os
from dotenv import load_dotenv


load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-secret')

# Use MySQL if DATABASE_URL provided (for cPanel), else SQLite for local development
DATABASE_URL = os.getenv('DATABASE_URL')
if DATABASE_URL:
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lkak.db'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)
login_manager.login_view = 'admin_login'

from models import User, Project, ContactMessage

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def index():
    projects = Project.query.order_by(Project.created_at.desc()).limit(6).all()
    hero_items = projects[:3] if projects else []
    return render_template('index.html', projects=projects, hero_items=hero_items)

@app.route('/projects')
def projects_view():
    projects = Project.query.order_by(Project.created_at.desc()).all()
    return render_template('projects.html', projects=projects)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        cm = ContactMessage(name=name, email=email, message=message)
        db.session.add(cm)
        db.session.commit()
        flash('Message received — we will get back to you.', 'success')
        return redirect(url_for('contact'))
    return render_template('contact.html')
