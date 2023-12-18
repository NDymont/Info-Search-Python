from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, IntegerField, SelectField, DateField, HiddenField
from wtforms.validators import DataRequired


class StudentForm(FlaskForm):
    student_id = HiddenField('Student ID')
    full_name = StringField('full_name', validators=[DataRequired()])
    birth_date = DateField('birth_date', validators=[DataRequired()])
    enrollment_year = IntegerField('enrollment_year', validators=[DataRequired()])
    #     university_id = db.Column(db.Integer, db.ForeignKey('university.id'), nullable=False)
    university = SelectField("university", coerce=int, validators=[DataRequired()])


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')
