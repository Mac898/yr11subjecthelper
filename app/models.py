#models
from app import db
db = db.get_db()

class Class(db.Model):
    __tablename__ = 'Class'
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(30), unique=True)
    type = db.Column(db.String(4))
    students = db.relationship('Student', lazy=True)

class Teacher(db.Model):
    __tablename__ = 'Teachers'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(60))
    last_name = db.Column(db.String(60))
    classes = db.relationship('class', backref='Teacher', lazy=True)

class Student(db.Model):
    __tablename__ = "Student"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(60))
    last_name = db.Column(db.String(60))
    srn = db.Column(db.Integer)
    classENG = db.Column(db.Integer, db.ForeignKey('Class.id'), uselist=False)
    classMTH = db.Column(db.Integer, db.ForeignKey('Class.id'), uselist=False)
    classEXTM = db.Column(db.Integer, db.ForeignKey('Class.id'), uselist=False)
    classEXTE = db.Column(db.Integer, db.ForeignKey('Class.id'), uselist=False)
    classE1 = db.Column(db.Integer, db.ForeignKey('Class.id'), uselist=False)
    classE2 = db.Column(db.Integer, db.ForeignKey('Class.id'), uselist=False)
    ClassE3 = db.Column(db.Integer, db.ForeignKey('Class.id'), uselist=False)
    ClassE4 = db.Column(db.Integer, db.ForeignKey('Class.id'), uselist=False)
