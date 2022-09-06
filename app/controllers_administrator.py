from crypt import methods

from app.forms import LoginForm
from app.models import Employee, EmployeeLogs, Administrator, AdministratorLogs, Clock
from app.ordinary_functions import response, validator_cpf
from app import app, db
from flask import request, render_template
import json


@app.route('/', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print(form.email.data)
        print(form.password.data)
        print(form.remember_me.data)
    else:
        print(form.errors)
    return render_template('login.html', form=form)

@app.route('/administrator/create_employee', methods = ['POST'])
def create_employee():
    body = request.get_json()
    try:
            employee_object = Employee(employee_cpf=validator_cpf(body['employee_cpf']), employee_email=body['employee_email'], employee_name=body['employee_name'], employee_password_hash=body['employee_password_hash'])
            db.session.add(employee_object)
            
            log_object = AdministratorLogs(administratorlogs_type='POST', administratorlogs_administrator_id=1, administratorlogs_action=f'Create employee {body["employee_name"]}')
            db.session.add(log_object)
            
            db.session.commit()
            return response(201, 'Employee', employee_object.to_json(), 'Employee entered successfully')
    except Exception as e:
            print('Error', e)
            return response(400, 'Employee', {}, 'Employee not inserted')

@app.route('/administrator/read_employee_all', methods = ['GET'])
def read_employee_all():
    try:
        employees_objects = Employee.query.all()
        employees_json = [employee.to_json() for employee in employees_objects]
        return response(200, 'Employees', employees_json, 'OK')
    except Exception as e:
        print('Error', e)
        return response(400, 'Employees', {}, 'Error')

@app.route('/administrator/read_employee_single/<employee_id>', methods = ['GET'])
def read_employee_single(employee_id):
    try:
        employee_object = Employee.query.filter_by(employee_id = employee_id).first()
        employee_json = employee_object.to_json()
        return response(200, 'Employee', employee_json, 'OK')
    except Exception as e:
        print('Error', e)
        return response(400, 'Employee', {}, 'Error')

@app.route('/administrator/update_employee/<employee_id>', methods = ['PUT'])
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
        db.session.add(employee_object)        
        log_object = AdministratorLogs(administratorlogs_type='PUT', administratorlogs_administrator_id=1, administratorlogs_action=f'Update employee {body["employee_name"]}')
        db.session.add(log_object)
        db.session.commit()
        return response(200, 'Employee', employee_object.to_json(), 'Employee update successfully')
    except Exception as e:
        print('Error', e)
        return response(400, 'Employee', employee_id, 'Employee not update')

@app.route('/administrator/delete_employee/<employee_id>', methods = ['DELETE'])
def delete_employee(employee_id):
    employee_object = Employee.query.filter_by(employee_id = employee_id).first()
    try:
        log_object = AdministratorLogs(administratorlogs_type='DELETE', administratorlogs_administrator_id=1, administratorlogs_action=f'Delete employee {employee_id}')
        db.session.delete(employee_object)
        db.session.add(log_object)
        db.session.commit()
        return response(200, "Employee", employee_object.to_json(), "Employee deleted successfully")
    except Exception as e:
        print('Error', e)
        return response(400, "Employee", {}, "Employee not deleted")
