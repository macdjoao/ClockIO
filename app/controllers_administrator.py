from crypt import methods

from app.forms import LoginForm
from app.models import Employee, EmployeeLogs, Administrator, AdministratorLogs, Clock
from app.ordinary_functions import response, employee_log, administrator_log, validator_cpf
from app import app, db
from flask import request, render_template
import json


@app.route('/')
def login():
    form = LoginForm()
    return render_template('login.html', form=form)

@app.route('/employee', methods = ['POST'])
def create_employee():
    body = request.get_json()
    try:
            employee_object = Employee(employee_cpf=validator_cpf(body['employee_cpf']), employee_email=body['employee_email'], employee_name=body['employee_name'], employee_password_hash=body['employee_password_hash'])
            log_object = administrator_log('POST', 1, f'CREATE A EMPLOYEE {body["employee_name"]}')
            db.session.add(employee_object)
            db.session.add(log_object)
            db.session.commit()
            return response(201, 'Employee', employee_object.to_json(), 'Employee created')
    except Exception as exception:
            print('Error', exception)
            return response(400, 'Employee', {}, 'Employee not created')

@app.route('/employee', methods = ['GET'])
def read_employee_all():
    employees_objects = Employee.query.all()
    employees_json = [employee.to_json() for employee in employees_objects]
    return response(200, 'Employees', employees_json, 'OK')

@app.route('/employee/<employee_id>', methods = ['GET'])
def read_employee_single(employee_id):
    employee_object = Employee.query.filter_by(employee_id = employee_id).first()
    employee_json = employee_object.to_json()
    return response(200, 'Employee', employee_json, 'OK')

@app.route('/employee/<employee_id>', methods = ['PUT'])
def update_employee(employee_id):
    employee_object = Employee.query.filter_by(employee_id = employee_id).first()
    body = request.get_json()
    try:
        if ('employee_cpf' in body):
            employee_object.employee_cpf = validator_cpf(body['employee_cpf'])
        if ('employee_email' in body):
            employee_object.employee_email = body['employee_email']
        if ('employee_name' in body):
            employee_object.employee_name = body['employee_name']
        if ('employee_first_access' in body):
            employee_object.employee_first_access = body['employee_first_access']        
        log_object = administrator_log('PUT', 1, f'UPDATE EMPLOYEE {body["employee_name"]}')        
        db.session.add(employee_object)
        db.session.add(log_object)
        db.session.commit()
        return response(200, 'Employee', employee_object.to_json(), 'Employee updated')
    except Exception as exception:
        print('Error', exception)
        return response(400, 'Employee', employee_id, 'Employee not updated')

@app.route('/employee/<employee_id>', methods = ['DELETE'])
def delete_employee(employee_id):
    employee_object = Employee.query.filter_by(employee_id = employee_id).first()
    try:
        log_object = administrator_log('DELETE', 1, f'DELETE EMPLOYEE {employee_id}')
        db.session.delete(employee_object)
        db.session.add(log_object)
        db.session.commit()
        return response(200, "Employee", employee_object.to_json(), "Employee deleted")
    except Exception as exception:
        print("Error", exception)
        return response(400, "Employee", {}, "Employee not deleted")
