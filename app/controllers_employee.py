from crypt import methods

from app.forms import LoginForm
from app.models import Employee, EmployeeLogs, Administrator, AdministratorLogs, Clock
from app.ordinary_functions import response, validator_cpf
from app import app, db
from flask import request, render_template
import json

@app.route('/<employee_id>/create_clock', methods = ['POST'])
def create_clock(employee_id):
    body = request.get_json()
    try:
        clock_object = Clock(clock_employee_id=employee_id, clock_input=body['clock_input'], clock_output=body['clock_output'], clock_extra=body['clock_extra'])
        db.session.add(clock_object)
        
        log_object = EmployeeLogs(employeelogs_type='POST', employeelogs_employee_id=employee_id, employeelogs_action=f'Entered record: {clock_object.clock_id}')
        db.session.add(log_object)
        
        db.session.commit()
        return response(201, 'Clock', clock_object.to_json(), 'Clock inserted successfully')
    except Exception as e:
        print('Error', e)
        return response(400, 'Clock', {}, 'Clock not inserted')

@app.route('/<employee_id>/read_clock', methods = ['GET'])
def read_clock(employee_id):
    try:
        clock_object = Clock.query.filter_by(clock_employee_id = employee_id).all()
        clock_json = [clock.to_json() for clock in clock_object]
        return response(200, 'Clocks', clock_json, 'OK')
    except Exception as e:
        print('Error', e)
        return response(400, 'Clocks', {}, 'Error')
