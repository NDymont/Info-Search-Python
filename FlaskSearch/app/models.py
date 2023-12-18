from . import db
from flask_login import UserMixin


class University(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(128), nullable=False)
    short_name = db.Column(db.String(15), nullable=False)
    creation_date = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return f'{self.short_name}'
        # return f'<University: {self.id}-{self.full_name}-{self.short_name}-{self.creation_date}>'


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(128), nullable=False)
    birth_date = db.Column(db.Date, nullable=False)
    enrollment_year = db.Column(db.Integer, nullable=False)
    university_id = db.Column(db.Integer, db.ForeignKey('university.id'), nullable=False)
    university = db.relationship("University", backref=db.backref('student', lazy=True))

    def __repr__(self):
        return '<Student %r>' % self.id


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)
