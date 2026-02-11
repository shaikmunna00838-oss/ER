# Employee Recruiting Management System
# Backend: Flask
# Database: SQLite (can be switched to MySQL)

from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
import random
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'secret123'

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///recruitment.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# -------------------- MODELS --------------------

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    department = db.Column(db.String(50))
    username = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(100))
    attempt_status = db.Column(db.Integer, default=0)  # 0 = not attempted, 1 = attempted
    score = db.Column(db.Integer, default=0)
    result_status = db.Column(db.String(20), default='PENDING')


class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    department = db.Column(db.String(50))
    question = db.Column(db.String(500))
    option_a = db.Column(db.String(200))
    option_b = db.Column(db.String(200))
    option_c = db.Column(db.String(200))
    option_d = db.Column(db.String(200))
    correct_option = db.Column(db.String(1))


class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(100))


class Notification(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    message = db.Column(db.String(300))
    date = db.Column(db.DateTime, default=datetime.utcnow)

# -------------------- ROUTES --------------------

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':

        existing_user = User.query.filter_by(username=request.form['username']).first()

        if existing_user:
            flash("Username already exists! Choose another one.")
            return redirect(url_for('register'))

        existing_email = User.query.filter_by(email=request.form['email']).first()

        if existing_email:
            flash("Email already registered!")
            return redirect(url_for('register'))

        user = User(
            name=request.form['name'],
            email=request.form['email'],
            department=request.form['department'],
            username=request.form['username'],
            password=request.form['password']
        )

        db.session.add(user)
        db.session.commit()
        flash('Registration successful!')
        return redirect(url_for('login'))

    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(username=request.form['username'], password=request.form['password']).first()
        if user:
            if user.attempt_status == 1:
                flash('You have already attempted the quiz')
                return redirect(url_for('result'))
            session['user_id'] = user.id
            return redirect(url_for('quiz'))
        flash('Invalid login credentials')
    return render_template('login.html')

@app.route('/quiz')
def quiz():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    user = User.query.get(session['user_id'])

    # Prevent re-attempt
    if user.attempt_status == 1:
        flash("You have already attempted the quiz!")
        return redirect(url_for('result'))

    questions = Question.query.filter_by(department=user.department).all()

    if len(questions) < 15:
        flash("Not enough questions in database!")
        return redirect(url_for('index'))
    for q in questions:
        print(q.id, q.question)

        quiz_questions = random.sample(questions, 15)
        session['quiz_questions'] = [q.id for q in quiz_questions]

    return render_template('quiz.html', questions=quiz_questions)



@app.route('/submit_quiz', methods=['POST'])
def submit_quiz():
    score = 0
    for qid in session['quiz_questions']:
        question = Question.query.get(qid)
        answer = request.form.get(str(qid))
        if answer == question.correct_option:
            score += 1

    user = User.query.get(session['user_id'])
    user.score = score
    user.attempt_status = 1

    if score >= 8:
        user.result_status = 'SELECTED'

        notification = Notification(
        user_id=user.id,
        message="Congratulations! You are selected for Campus Interview.")
        db.session.add(notification)

    else:
        user.result_status = 'FAILED'

    db.session.commit()
    return redirect(url_for('result'))


@app.route('/result')
def result():
    user = User.query.get(session['user_id'])
    notifications = Notification.query.filter_by(user_id=user.id).all()
    return render_template('result.html', user=user, notifications=notifications)


# -------------------- ADMIN --------------------

@app.route('/admin', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        admin = Admin.query.filter_by(username=request.form['username'], password=request.form['password']).first()
        if admin:
            session['admin'] = True
            return redirect(url_for('admin_dashboard'))
    return render_template('admin_login.html')


@app.route('/admin/dashboard')
def admin_dashboard():
    users = User.query.all()
    return render_template('admin_dashboard.html', users=users)


@app.route('/admin/notify/<int:user_id>', methods=['POST'])
def notify(user_id):
    message = request.form['message']
    notification = Notification(user_id=user_id, message=message)
    db.session.add(notification)
    db.session.commit()
    return redirect(url_for('admin_dashboard'))


@app.route('/admin/selected')
def selected_candidates():
    users = User.query.filter_by(result_status="SELECTED").all()
    return render_template("admin_dashboard.html", users=users)

@app.route('/admin/failed')
def failed_candidates():
    users = User.query.filter_by(result_status="FAILED").all()
    return render_template("admin_dashboard.html", users=users)

@app.route('/admin/delete/<int:user_id>')
def delete_user(user_id):
    user = User.query.get(user_id)
    db.session.delete(user)
    db.session.commit()
    flash("User deleted successfully")
    return redirect(url_for('admin_dashboard'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
