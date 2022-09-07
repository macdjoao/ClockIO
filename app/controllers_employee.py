from crypt import methods

from app.forms import LoginForm
from app.models import Employee, EmployeeLogs, Administrator, AdministratorLogs, Clock
from app.ordinary_functions import generate_response, validator_cpf
from app import app, db
from flask import request, render_template
from flask_sqlalchemy import SQLAlchemy
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
        return generate_response(201, 'Clock', clock_object.to_json(), 'Clock inserted successfully')
    except Exception as e:
        print('Error', e)
        return generate_response(400, 'Clock', {}, 'Clock not inserted')

@app.route('/<employee_id>/read_clock', methods = ['GET'])
def read_clock(employee_id):
    try:
        clock_object = Clock.query.filter_by(clock_employee_id = employee_id).all()
        clock_json = [clock.to_json() for clock in clock_object]
        return generate_response(200, 'Clocks', clock_json, 'OK')
    except Exception as e:
        print('Error', e)
        return generate_response(400, 'Clocks', {}, 'Error')

# @app.route('/<employee_id>/read_clock/filter', methods = ['GET'])
# def read_clock(employee_id):
#     body = request.get_json()
#     try:
#         if('initial_date' in body and 'final_date' not in body):
#             query = # search all the registers after 'initial_date'
#             query = Clock.clock_input < body['initial_date']
#         if('initial_date' not in body and 'final_date' in body):
#             query = # search all the registers before 'final_date'
#             query = Clock.clock_input > body['final_date']
#         if('initial_date' in body and 'final_date' in body):
#             query = # search all the registers between 'initial_date' and 'final_date'
#             query = Clock.clock_input < body['initial_date'], Clock.clock_input > body['final_date']
#         if('extra' in body):
#             query = # search only the registers marked with 'extra'
#         clock_object = Clock.query.filter_by('query').all()
#         clock_json = clock_object.to_json()
#         return generate_response(200, 'Clocks', clock_json, 'OK')
#     except Exception as e:
#         print('Error', e)
#         return generate_response(400, 'Clocks', {}, 'Error')
