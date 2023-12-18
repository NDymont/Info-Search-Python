from werkzeug.security import check_password_hash

from app import app, db
from app.models import University, Student, User

from flask import render_template, request, redirect, flash, url_for
from app.forms import StudentForm, LoginForm
from flask_login import login_user, login_required, logout_user, current_user


@app.route('/')
def index():
    return render_template("layout.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.password == form.password.data:
            login_user(user)
            flash('Login successful!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Login unsuccessful. Check username and password.', 'danger')
    return render_template('login.html', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/dashboard')
@login_required
def dashboard():
    return f'Hello, {current_user.username}!'


@app.route('/universities')
def universitiesView():
    universities = University.query.all()
    return render_template('university_view.html', universities=universities, title='Университеты')


@app.route('/universities/add', methods=['GET', 'POST'])
@login_required
def createUniversities():
    if request.method == 'GET':
        return render_template('createpage.html')

    if request.method == 'POST':
        try:
            full_name = request.form['full_name']
            short_name = request.form['short_name']
            creation_date = request.form['creation_date']
            university = University(full_name=full_name, short_name=short_name, creation_date=creation_date)
            db.session.add(university)
            db.session.commit()
            flash('Университет успешно добавлен', 'success')
            return redirect('/universities')
        except Exception as e:
            flash(f'Ошибка при добавлении университета: {str(e)}', 'error')
            return render_template('createpage.html', error='неправильные данные, попробуйте снова',
                                   full_name=full_name, short_name=short_name, creation_date=creation_date)


@app.route('/universities/update/<int:id>', methods=['GET', 'POST'])
@login_required
def updateUniversities(id):
    university = University.query.get_or_404(id)

    if request.method == 'GET':
        return render_template('edit_university.html', university=university)

    if request.method == 'POST':
        try:
            university.full_name = request.form['full_name']
            university.short_name = request.form['short_name']
            university.creation_date = request.form['creation_date']
            db.session.commit()
            flash('Университет успешно обновлен', 'success')
            return redirect('/universities')
        except Exception as e:
            flash(f'Ошибка при обновлении университета: {str(e)}', 'error')
            return render_template('edit_university.html', university=university,
                                   error='Неправильные данные, попробуйте снова')


@app.route('/universities/delete/<int:id>', methods=['GET', 'POST'])
def deleteUniversities(id):
    university = University.query.get_or_404(id)

    if request.method == 'GET':
        return render_template('deletepage.html', name=university.full_name)

    if request.method == 'POST':
        try:
            db.session.delete(university)
            db.session.commit()
            flash('Университет успешно удален', 'success')
            return redirect('/universities')
        except Exception as e:
            print(str(e))
            flash(f'Ошибка при удалении университета: {str(e)}', 'error')
            return render_template('deletepage.html', error='Ошибка при удалении университета', university=university)


@app.route('/students')
def studentsView():
    students = Student.query.all()
    return render_template('student/view.html', students=students, title='Студенты')


@app.route('/students/add', methods=['GET', 'POST'])
@login_required
def createStudent():
    form = StudentForm()
    form.university.choices = [(university.id, university.short_name)
                               for university in University.query.all()]

    if form.validate_on_submit():
        new_student = Student(full_name=form.full_name.data,
                              birth_date=form.birth_date.data,
                              enrollment_year=form.enrollment_year.data
                              , university_id=form.university.data
                              )
        db.session.add(new_student)
        db.session.commit()
        return redirect(url_for('studentsView'))
    return render_template('student/add_student.html', form=form, title="Создать студента")


@app.route('/students/update/<int:student_id>', methods=['GET', 'POST'])
@login_required
def editStudent(student_id):
    student = Student.query.get_or_404(student_id)
    form = StudentForm()
    form.university.choices = [(university.id, university.short_name) for university in University.query.all()]

    if request.method == 'GET':
        form.student_id.data = student.id
        form.full_name.data = student.full_name
        form.birth_date.data = student.birth_date
        form.enrollment_year.data = student.enrollment_year
        form.university.data = student.university_id

    if form.validate_on_submit():
        student.full_name = form.full_name.data
        student.birth_date = form.birth_date.data
        student.enrollment_year = form.enrollment_year.data
        student.university_id = form.university.data

        db.session.commit()
        return redirect(url_for('studentsView'))

    return render_template('student/add_student.html', form=form, title="Редактировать студента")


@app.route('/students/delete/<int:id>', methods=['GET', 'POST'])
def deleteStudent(id):
    student = Student.query.get_or_404(id)

    if request.method == 'GET':
        return render_template('deletepage.html', name=student.full_name)

    if request.method == 'POST':
        try:
            db.session.delete(student)
            db.session.commit()
            flash('Студент успешно удален', 'success')
            return redirect('/students')
        except Exception as e:
            print(str(e))
            flash(f'Ошибка при удалении студента: {str(e)}', 'error')
            return render_template('deletepage.html', error='Ошибка при удалении студента')
