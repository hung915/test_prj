from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy.orm import backref
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:root@localhost:5432/test_model"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
Migrate(app, db)


class Person(db.Model):
    __tablename__ = 'per1'

    # def __init__(self, name):
    #     self.name = name

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    addresses = db.relationship('Address', backref='per1', lazy=True)


class Address(db.Model):
    __tablename__ = 'addr'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), nullable=False)
    person_id = db.Column(db.Integer, db.ForeignKey('per1.id'))

    # def __init__(self, email, person_id):
    #     self.email = email
    #     self.person_id = person_id


# class Certificates(db.Model):
#     """Storing certificates"""
#
#     __tablename__ = "certificates"
#
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     name = db.Column(db.String(50), nullable=False)
#     original_filename = db.Column(db.String(500), nullable=True)
#     path = db.Column(db.String(500), nullable=True)
#     created_date = db.Column(
#         db.DateTime, nullable=True, default=datetime.utcnow
#     )
#     created_by = db.Column(db.String(100), nullable=True)
#     updated_date = db.Column(db.DateTime, nullable=True)
#     updated_by = db.Column(db.String(100), nullable=True)
#     deleted_date = db.Column(db.DateTime, nullable=True)
#     deleted_by = db.Column(db.String(100), nullable=True)
#
#     def __init__(self, name):
#         self.name = name
#
#     def __repr__(self):
#         return "name: {}".format(self.name)
#
#
# class EmployeeCertificates(db.Model):
#     """Storing employee certificates"""
#
#     __tablename__ = "employee_certificates"
#
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     certificate_type = db.Column(db.Integer, nullable=False)
#     certificate_id = db.Column(db.Integer, db.ForeignKey("certificates.id"))
#     certificate = db.relationship(
#         "Certificates", backref=backref("certificates", uselist=False)
#     )
#     other_type = db.Column(db.String(200), nullable=True)
#     start_date = db.Column(db.DateTime, nullable=True)
#     end_date = db.Column(db.DateTime, nullable=True)
#     created_by = db.Column(db.String(100), nullable=True)
#     updated_date = db.Column(db.DateTime, nullable=True)
#     updated_by = db.Column(db.String(100), nullable=True)
#     deleted_date = db.Column(db.DateTime, nullable=True)
#     deleted_by = db.Column(db.String(100), nullable=True)
#
#     def __init__(self, certificate_type, certificate_id):
#         self.certificate_type = certificate_type
#         self.certificate_id = certificate_id
#
#     def __repr__(self):
#         return "certificate_type: {}".format(self.certificate_type)
#
#
class EmployeePositions(db.Model):
    __tablename__ = 'employee_positions'
    id = db.Column(db.Integer, primary_key=True)
    position_name = db.Column(db.String(50), nullable=False)
    employees = db.relationship('Employees', backref='employee_positions', passive_deletes=True)

    def __init__(self, position_name):
        self.position_name = position_name


class Employees(db.Model):
    __tablename__ = 'employees'
    id = db.Column(db.Integer, primary_key=True)
    position_id = db.Column(db.Integer, db.ForeignKey('employee_positions.id', ondelete='CASCADE'), nullable=False)
    grade = db.Column(db.String(50), nullable=False)

    def __init__(self, grade, position_id):
        self.grade = grade
        self.position_id = position_id
