# app.py - Main Application
from flask import Flask, render_template, request, redirect, url_for, flash
from database import init_db, add_student, get_all_students, get_student_by_name
from models import db, Student

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'

# Initialize database
init_db(app)

@app.route('/')
def home():
    total_students = Student.query.filter_by(is_active=True).count()
    return render_template('home.html', total_students=total_students)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        student_data = {
            'student_name': request.form.get('student_name', '').strip(),
            'registration_number': request.form.get('registration_number', '').strip(),
            'email': request.form.get('email', '').strip(),
            'programme': request.form.get('programme', '').strip()
        }

        if not all(student_data.values()):
            flash('All fields are required!', 'error')
            return render_template('register.html', form_data=student_data)

        success, message, student = add_student(student_data)

        if success:
            flash(message, 'success')
            return redirect(url_for('student_profile', student_name=student.student_name))
        else:
            flash(message, 'error')
            return render_template('register.html', form_data=student_data)

    return render_template('register.html', form_data=None)

@app.route('/students')
def students_list():
    all_students = Student.query.all()
    return render_template('students_list.html', students=all_students)

@app.route('/search', methods=['GET'])
def search_students():
    search_term = request.args.get('q', '').strip()
    if search_term:
        student = get_student_by_name(search_term)
        return render_template(
            'students_list.html',
            students=[student] if student else [],
            search_term=search_term
        )
    return redirect(url_for('students_list'))

@app.route('/students/<string:student_name>')
def student_profile(student_name):
    student = Student.query.filter_by(student_name=student_name).first_or_404()
    return render_template('student_profile.html', student=student)

@app.route('/students/<string:student_name>/edit', methods=['GET', 'POST'])
def edit_student(student_name):
    student = Student.query.filter_by(student_name=student_name).first_or_404()

    if request.method == 'POST':
        student.student_name = request.form.get('student_name', student.student_name)
        student.email = request.form.get('email', student.email)
        student.programme = request.form.get('programme', student.programme)
        db.session.commit()
        return redirect(url_for('student_profile', student_name=student.student_name))

    return render_template('edit_student.html', student=student)

@app.route('/students/<string:student_name>/delete', methods=['POST'])
def delete_student(student_name):
    student = Student.query.filter_by(student_name=student_name).first_or_404()
    db.session.delete(student)
    db.session.commit()
    return redirect(url_for('students_list'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)