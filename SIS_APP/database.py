# database.py - Database Operations
from models import db, Student

def init_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    with app.app_context():
        db.create_all()
        print("✅ Database initialized successfully!")

        if Student.query.count() == 0:
            add_sample_data()

def add_sample_data():
    sample_students = [
        Student(
            student_name='John Doe',
            email='john.doe@university.edu',
            programme='Computer Science'
        ),
        Student(
            student_name='Jane Smith',
            email='jane.smith@university.edu',
            programme='Information Technology'
        ),
        Student(
            student_name='Alice Johnson',
            email='alice.johnson@university.edu',
            programme='Mathematics'
        ),
        Student(
            student_name='Bob Brown',
            email='bob.brown@university.edu',
            programme='Physics'
        )
    ]

    for student in sample_students:
        db.session.add(student)
    db.session.commit()
    print("📚 Sample data added!")

def get_all_students():
    return Student.query.filter_by(is_active=True).all()

def get_student_by_name(student_name):
    return Student.query.filter_by(
        student_name=student_name,
        is_active=True
    ).first()

def add_student(student_data):
    try:
        existing = get_student_by_name(student_data['student_name'])
        if existing:
            return False, "Student name already exists!", None

        existing_email = Student.query.filter_by(email=student_data['email']).first()
        if existing_email:
            return False, "Email already registered!", None

        new_student = Student(
            student_name=student_data['student_name'],
            email=student_data['email'],
            programme=student_data['programme']
        )

        db.session.add(new_student)
        db.session.commit()
        return True, "Student registered successfully!", new_student

    except Exception as e:
        db.session.rollback()
        return False, f"Database error: {str(e)}", None

def update_student(student_name, updated_data):
    try:
        student = get_student_by_name(student_name)
        if not student:
            return False, "Student not found!"

        if 'email' in updated_data and updated_data['email'] != student.email:
            existing_email = Student.query.filter_by(email=updated_data['email']).first()
            if existing_email:
                return False, "Email already registered!"

        student.student_name = updated_data.get('student_name', student.student_name)
        student.email = updated_data.get('email', student.email)
        student.programme = updated_data.get('programme', student.programme)

        db.session.commit()
        return True, "Student record updated successfully!"

    except Exception as e:
        db.session.rollback()
        return False, f"Database error: {str(e)}"

def delete_student(student_name):
    try:
        student = get_student_by_name(student_name)
        if not student:
            return False, "Student not found!"

        db.session.delete(student)
        db.session.commit()
        return True, "Student record deleted successfully!"

    except Exception as e:
        db.session.rollback()
        return False, f"Database error: {str(e)}"

def delete_student_permanently(student_name):
    try:
        student = get_student_by_name(student_name)
        if not student:
            return False, "Student not found!"

        db.session.delete(student)
        db.session.commit()
        return True, "Student record deleted permanently!"

    except Exception as e:
        db.session.rollback()
        return False, f"Database error: {str(e)}"