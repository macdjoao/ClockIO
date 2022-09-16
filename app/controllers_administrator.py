from crypt import methods

from app.forms import LoginForm
from app.models import Employee, EmployeeLogs, Administrator, AdministratorLogs, Clock
from app.ordinary_functions import generate_response, validator_cpf
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
            employee_object = Employee(employee_cpf=validator_cpf(body['employee_cpf']), employee_name=body['employee_name'], employee_password=body['employee_password'])
            db.session.add(employee_object)
            
            log_object = AdministratorLogs(administratorlogs_type='POST', administratorlogs_administrator_id=1, administratorlogs_action=f'Create employee {body["employee_name"]}')
            db.session.add(log_object)
            
            db.session.commit()
            return generate_response(201, 'Employee', employee_object.to_json(), 'Employee entered successfully')
    except Exception as e:
            print('Error', e)
            return generate_response(400, 'Employee', {}, 'Employee not inserted')

@app.route('/administrator/read_employee_all', methods = ['GET'])
def read_employee_all():
    try:
        employees_objects = Employee.query.all()
        employees_json = [employee.to_json() for employee in employees_objects]
        return generate_response(200, 'Employees', employees_json, 'OK')
    except Exception as e:
        print('Error', e)
        return generate_response(400, 'Employees', {}, 'Error')

@app.route('/administrator/read_employee_single/<employee_id>', methods = ['GET'])
def read_employee_single(employee_id):
    try:
        employee_object = Employee.query.filter_by(employee_id = employee_id).first()
        employee_json = employee_object.to_json()
        return generate_response(200, 'Employee', employee_json, 'OK')
    except Exception as e:
        print('Error', e)
        return generate_response(400, 'Employee', {}, 'Error')

@app.route('/administrator/update_employee/<employee_id>', methods = ['PUT'])
def update_employee(employee_id):
    employee_object = Employee.query.filter_by(employee_id = employee_id).first()
    body = request.get_json()
    try:
        if ('employee_cpf' in body):
            employee_object.employee_cpf = validator_cpf(body['employee_cpf'])
        if ('employee_name' in body):
            employee_object.employee_name = body['employee_name']
        if ('employee_first_access' in body):
            employee_object.employee_first_access = body['employee_first_access']
        if ('employee_status' in body):
            employee_object.employee_status = body['employee_status']
        db.session.add(employee_object)        
        log_object = AdministratorLogs(administratorlogs_type='PUT', administratorlogs_administrator_id=1, administratorlogs_action=f'Update employee {employee_id}')
        db.session.add(log_object)
        db.session.commit()
        return generate_response(200, 'Employee', employee_object.to_json(), 'Employee updated successfully')
    except Exception as e:
        print('Error', e)
        return generate_response(400, 'Employee', employee_id, 'Employee not updated')

@app.route('/administrator/delete_employee/<employee_id>', methods = ['DELETE'])
def delete_employee(employee_id):
    employee_object = Employee.query.filter_by(employee_id = employee_id).first()
    try:
        log_object = AdministratorLogs(administratorlogs_type='DELETE', administratorlogs_administrator_id=1, administratorlogs_action=f'Delete employee {employee_id}')
        db.session.delete(employee_object)
        db.session.add(log_object)
        db.session.commit()
        return generate_response(200, "Employee", employee_object.to_json(), "Employee deleted successfully")
    except Exception as e:
        print('Error', e)
        return generate_response(400, "Employee", {}, "Employee not deleted")

@app.route('/administrator/update_clock/<clock_id>', methods = ['PUT'])
def update_clock(clock_id):
    clock_object = Clock.query.filter_by(clock_id = clock_id).first()
    body = request.get_json()
    try:
        if('new_input' in body):
            clock_object.clock_input = body['new_input']
        if('new_output' in body):
            clock_object.clock_output = body['new_output']
        if('clock_extra' in body):
            clock_object.clock_extra = body['clock_extra']
        db.session.add(clock_object)
        
        log_object = AdministratorLogs(administratorlogs_type='PUT', administratorlogs_administrator_id=1, administratorlogs_action=f'Update clock {clock_id}')
        db.session.add(log_object)
        
        db.session.commit()
        return generate_response(200, 'Clock', clock_object.to_json(), 'Clock updated successfully')
    except Exception as e:
        print('Error', e)
        return generate_response(400, 'Clock', {}, 'Clock not updated')

@app.route('/administrator/read_clock_all', methods = ['GET'])
def read_clock_all():
    try:
        clock_object = Clock.query.all()
        clock_json = [clock.to_json() for clock in clock_object]
        return generate_response(200, 'Clocks', clock_json, 'OK')
    except Exception as e:
        print('Error', e)
        return generate_response(400, 'Clocks', {}, 'Error')

@app.route('/administrator/read_clock_single/<employee_id>', methods = ['GET'])
def read_clock_single(employee_id):
    try:
        clock_object = Clock.query.filter_by(clock_employee_id = employee_id ).all()
        clock_json = [clock.to_json() for clock in clock_object]
        return generate_response(200, 'Clocks', clock_json, 'OK')
    except Exception as e:
        print('Error', e)
        return generate_response(400, 'Clocks', {}, 'Error')

# @app.route('/administrator/read_clock_all/filter')
# def read_clock_all_filter():
#     pass

# @app.route('/administrator/read_clock_single/<employee_id>/filter')
# def read_clock_single_filter():
#     pass
