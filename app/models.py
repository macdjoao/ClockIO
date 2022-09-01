from datetime import datetime
from . import db

# Migrate updates to the database
# $ flask db stamp head
# $ flask db migrate
# $ flask db upgrade

class Administrator(db.Model):
    __tablename__ = 'administrators'

    administrator_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    administrator_name = db.Column(db.String(255), nullable=False)
    administrator_password_hash = db.Column(db.String(255), nullable=False)
    administrator_first_access = db.Column(db.Boolean, default=False)

    def __init__(self, administrator_id, administrator_name, administrator_password_hash, administrator_first_access):
        self.administrator_id = administrator_id
        self.administrator_name = administrator_name
        self.administrator_password_hash = administrator_password_hash
        self.administrator_first_access = administrator_first_access

    def __repr__(self):
        return f'<administrator_id: {self.administrator_id}, administrator_name: {self.administrator_name}, administrator_password_hash: {self.administrator_password_hash}, administrator_first_access: {self.administrator_first_access}>'

    def to_json(self):
        return {"administrator_id": self.administrator_id, "administrator_name": self.administrator_name, "administrator_password_hash": self.administrator_password_hash, "administrator_first_access": self.administrator_first_access}


class AdministratorLogs(db.Model):
    __tablename__ = 'administratorlogs'

    administratorlogs_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    administratorlogs_datetime = db.Column(db.DateTime, default=datetime.utcnow)
    administratorlogs_type = db.Column(db.String(255), nullable=False)
    administratorlogs_administrator_id = db.Column(db.Integer, db.ForeignKey("administrators.administrator_id"))
    administratorlogs_action = db.Column(db.Text, nullable=False)

    employee = db.relationship('Administrator', foreign_keys=administratorlogs_administrator_id)

    def __init__(self, administratorlogs_id, administratorlogs_datetime, administratorlogs_type, administratorlogs_administrator_id, administratorlogs_action):
        self.administratorlogs_id = administratorlogs_id
        self.administratorlogs_datetime = administratorlogs_datetime
        self.administratorlogs_type = administratorlogs_type
        self.administratorlogs_administrator_id = administratorlogs_administrator_id
        self.administratorlogs_action = administratorlogs_action

    def __repr__(self):
        return f'<administratorlogs_id: {self.administratorlogs_id}, administratorlogs_datetime: {self.administratorlogs_datetime}, administratorlogs_type: {self.administratorlogs_type}, administratorlogs_administrator_id: {self.administratorlogs_administrator_id}, administratorlogs_action: {self.administratorlogs_action}>'

    def to_json(self):
        return {"administratorlogs_id": self.administratorlogs_id, "administratorlogs_datetime": self.administratorlogs_datetime, "administratorlogs_type": self.administratorlogs_type, "administratorlogs_administrator_id": self.administratorlogs_administrator_id, "administratorlogs_action": self.administratorlogs_action}


class Employee(db.Model):
    __tablename__ = 'employees'

    employee_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    employee_cpf = db.Column(db.String(11), nullable=False, unique=True)
    employee_email = db.Column(db.String(255), nullable=False, unique=True)
    employee_name = db.Column(db.String(255), nullable=False)
    employee_password_hash = db.Column(db.String(255), nullable=False)
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


class EmployeeLogs(db.Model):
    __tablename__ = 'employeelogs'

    employeelogs_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    employeelogs_datetime = db.Column(db.DateTime, default=datetime.utcnow)
    employeelogs_type = db.Column(db.String(255), nullable=False)
    employeelogs_employee_id = db.Column(db.Integer, db.ForeignKey("employees.employee_id"))
    employeelogs_action = db.Column(db.Text, nullable=False)

    employee = db.relationship('Employee', foreign_keys=employeelogs_employee_id)

    def __init__(self, employeelogs_id, employeelogs_datetime, employeelogs_type, employeelogs_employee_id, employeelogs_action):
        self.employeelogs_id = employeelogs_id
        self.employeelogs_datetime = employeelogs_datetime
        self.employeelogs_type = employeelogs_type
        self.employeelogs_employee_id = employeelogs_employee_id
        self.employeelogs_action = employeelogs_action

    def __repr__(self):
        return f'<employeelogs_id: {self.employeelogs_id}, employeelogs_datetime: {self.employeelogs_datetime}, employeelogs_type: {self.employeelogs_type}, employeelogs_employee_id: {self.employeelogs_employee_id}, employeelogs_action: {self.employeelogs_action}>'

    def to_json(self):
        return {"employeelogs_id": self.employeelogs_id, "employeelogs_datetime": self.employeelogs_datetime, "employeelogs_type": self.employeelogs_type, "employeelogs_employee_id": self.employeelogs_employee_id, "employeelogs_action": self.employeelogs_action}


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
