from crypt import methods

from app.forms import LoginForm
from app.models import User, UserLogs, Clock, ClockLogs
from app.ordinary_functions import generate_response, validator_cpf, is_user, is_admin
from app import app, db
from flask import request, render_template
import json

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print(form.email.data)
        print(form.password.data)
    else:
        print(form.errors)
    return render_template('login.html', form=form)

@app.route('/<user_id>/create_employee', methods = ['GET', 'POST'])
def create_employee(user_id):
    if is_user(user_id) == False:
        return generate_response(404, 'User', {}, 'You are not a user')
    if is_admin(user_id) == False:
        return generate_response(400, 'User', {}, 'You dont have privileges to do this')

    body = request.get_json()
    try:
        employee_object = User(user_cpf=validator_cpf(body['user_cpf']), user_name=body['user_name'], user_password=body['user_cpf'], user_first_access=True, user_status=True, user_is_admin=False)
        db.session.add(employee_object)
        log_object = UserLogs(userlogs_type='POST', userlogs_user_id=user_id, userlogs_action=f'Create employee {body["user_name"]}')
        db.session.add(log_object)
        db.session.commit()
        return generate_response(201, 'Employee', employee_object.to_json(), 'Employee entered successfully')
    except Exception as e:
            print('Error', e)
            return generate_response(400, 'Employee', {}, 'Employee not inserted')

@app.route('/<user_id>/read_users', methods = ['GET'])
def read_users(user_id):
    if is_user(user_id) == False:
        return generate_response(404, 'User', {}, 'You are not a user')
    if is_admin(user_id) == False:
        return generate_response(400, 'User', {}, 'You dont have privileges to do this')

    try:
        users_objects = User.query.all()
        users_json = [user.to_json() for user in users_objects]
        return generate_response(200, 'Users', users_json, 'OK')
    except Exception as e:
        print('Error', e)
        return generate_response(400, 'Users', {}, 'Error')

@app.route('/<user_id>/update_employee/<employee_id>', methods = ['GET', 'PUT'])
def update_employee(user_id, employee_id):
    if is_user(user_id) == False:
        return generate_response(404, 'User', {}, 'You are not a user')
    if is_admin(user_id) == False:
        return generate_response(400, 'User', {}, 'You dont have privileges to do this')

    employee_object = User.query.filter_by(user_id = employee_id).first()
    if employee_object == None:
        return generate_response(404, 'Employee', employee_id, 'Employee not found')
    if employee_object.user_is_admin == 1:
        return generate_response(400, 'Employee', employee_id, 'This is a Admin User, you cannot update him')
    else:
        body = request.get_json()
        try:
            if ('employee_cpf' in body):
                employee_object.user_cpf = validator_cpf(body['employee_cpf'])
            if ('employee_name' in body):
                employee_object.user_name = body['employee_name']
            if ('employee_first_access' in body):
                employee_object.user_first_access = body['employee_first_access']
            if ('employee_status' in body):
                employee_object.user_status = body['employee_status']
            db.session.add(employee_object)        
            log_object = UserLogs(userlogs_type='PUT', userlogs_user_id=user_id, userlogs_action=f'Update employee {employee_id}')
            db.session.add(log_object)
            db.session.commit()
            return generate_response(200, 'Employee', employee_object.to_json(), 'Employee updated successfully')
        except Exception as e:
            print('Error', e)
            return generate_response(400, 'Employee', employee_id, 'Employee not updated')

@app.route('/<user_id>/update_clock/<clock_id>', methods = ['PUT'])
def update_clock(user_id, clock_id):
    if is_user(user_id) == False:
        return generate_response(404, 'User', {}, 'You are not a user')
    if is_admin(user_id) == False:
        return generate_response(400, 'User', {}, 'You dont have privileges to do this')

    clock_object = Clock.query.filter_by(clock_id = clock_id).first()
    if clock_object == None:
        return generate_response(404, 'Clock', clock_id, 'Clock not found')
    body = request.get_json()
    try:
        if('new_input' in body):
            clock_object.clock_input = body['new_input']
        if('new_output' in body):
            clock_object.clock_output = body['new_output']
        if('clock_extra' in body):
            clock_object.clock_extra = body['clock_extra']
        db.session.add(clock_object)
        log_object = ClockLogs(clocklogs_clock_id=clock_id, clocklogs_type='PUT', clocklogs_user_id=user_id)
        db.session.add(log_object)
        db.session.commit()
        return generate_response(200, 'Clock', clock_object.to_json(), 'Clock updated successfully')
    except Exception as e:
        print('Error', e)
        return generate_response(400, 'Clock', {}, 'Clock not updated')

@app.route('/<user_id>/read_clock', methods = ['GET'])
def read_clock(user_id):
    if is_user(user_id) == False:
        return generate_response(404, 'User', {}, 'You are not a user')
    if is_admin(user_id) == False:
        return generate_response(400, 'User', {}, 'You dont have privileges to do this')

    try:
        clock_object = Clock.query.all()
        clock_json = [clock.to_json() for clock in clock_object]
        return generate_response(200, 'Clocks', clock_json, 'OK')
    except Exception as e:
        print('Error', e)
        return generate_response(400, 'Clocks', {}, 'Error')











@app.route('/<employee_id>/create_clock', methods = ['POST'])
def create_clock(employee_id):
    if is_user(employee_id) == False:
        return generate_response(404, 'User', {}, 'You are not a user')
    if is_admin(employee_id) == True:
        return generate_response(400, 'User', {}, 'You dont have privileges to do this')

    body = request.get_json()
    try:
        clock_object = Clock(clock_user_id=employee_id, clock_input=body['clock_input'], clock_output=body['clock_output'], clock_extra=body['clock_extra'])
        db.session.add(clock_object)        
        db.session.commit()
        return generate_response(201, 'Clock', clock_object.to_json(), 'Clock inserted successfully')
    except Exception as e:
        print('Error', e)
        return generate_response(400, 'Clock', {}, 'Clock not inserted')

@app.route('/<employee_id>/read_my_clocks', methods = ['GET'])
def read_my_clocks(employee_id):
    if is_user(employee_id) == False:
        return generate_response(404, 'User', {}, 'You are not a user')
    if is_admin(employee_id) == True:
        return generate_response(400, 'User', {}, 'You dont have privileges to do this')

    try:
        clock_object = Clock.query.filter_by(clock_user_id = employee_id).all()
        clock_json = [clock.to_json() for clock in clock_object]
        return generate_response(200, 'Clocks', clock_json, 'OK')
    except Exception as e:
        print('Error', e)
        return generate_response(400, 'Clocks', {}, 'Error')
