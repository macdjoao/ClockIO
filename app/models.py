from email.policy import default
from . import db


class Employee(db.Model):
    __tablename__ = 'employees'

    employee_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    employee_cpf = db.Column(db.String(11), nullable=False, unique=True)
    employee_email = db.Column(db.String, nullable=False, unique=True)
    employee_name = db.Column(db.String(200), nullable=False)
    employee_password_hash = db.Column(db.String, nullable=False)
    employee_first_access = db.Column(db.Boolean, default=False)

    def __init__(self, employee_id, employee_cpf, employee_email, employee_name, employee_password_hash, employee_first_access):
        self.employee_id = employee_id
        self.employee_cpf = employee_cpf
        self.employee_email = employee_email
        self.employee_name = employee_name
        self.employee_password_hash = employee_password_hash
        self.employee_first_access = employee_first_access

    def __repr__(self):
        return f'<employee_id: {self.employee_id}, employee_cpf: {self.employee_cpf}, employee_email: {self.employee_email}, employee_name: {self.employee_name}, employee_password_hash: {self.employee_password_hash}, employee_first_access: {self.employee_first_access}>'

    def to_json(self):
        return {"employee_id": self.employee_id, "employee_cpf": self.employee_cpf, "employee_email": self.employee_email, "employee_name": self.employee_name, "employee_password_hash": self.employee_password_hash, "employee_first_access": self.employee_first_access}
      

class Clock(db.Model):
    __tablename__ = 'clocks'

    clock_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    clock_employee_id = db.Column(db.Integer, db.ForeignKey("employees.employee_id"))
    clock_input = db.Column(db.DateTime, nullable=False)
    clock_output = db.Column(db.DateTime, nullable=False)
    clock_extra = db.Column(db.Boolean, default=False)

    employee = db.relationship('Employee', foreign_keys=clock_employee_id)

    def __init__(self, clock_id, clock_employee_id, clock_input, clock_output, clock_extra):
        self.clock_id = clock_id
        self.clock_employee_id = clock_employee_id
        self.clock_input = clock_input
        self.clock_output = clock_output
        self.clock_extra = clock_extra

    def __repr__(self):
        return f'<clock_id: {self.clock_id}, clock_employee_id: {self.clock_employee_id}, clock_input: {self.clock_input}, clock_output: {self.clock_output}, clock_extra: {self.clock_extra}>'

    def to_json(self):
        return {"clock_id": self.clock_id, "clock_employee_id": self.clock_employee_id, "clock_input": self.clock_input, "clock_output": self.clock_output, "clock_extra": self.clock_extra}
