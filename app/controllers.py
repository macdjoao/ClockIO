from .models import Employee, EmployeeLogs, Administrator, AdministratorLogs, Clock 
from . import app, db
from flask import Response, request, render_template
import json


def response(status, content_name, content, message = False):
    body = {}
    body[content_name]=content
    if (message):
        body["Message"]=message
    return Response(json.dumps(body, default=str), status=status, mimetype="application/json")

def employee_log(employeelogs_type, employeelogs_employee_id, employeelogs_action):
    log_object = EmployeeLogs(employeelogs_type=employeelogs_type, employeelogs_employee_id=employeelogs_employee_id, employeelogs_action=employeelogs_action)
    return log_object

def administrator_log(administratorlogs_type, administratorlogs_administrator_id, administratorlogs_action):
    log_object = AdministratorLogs(administratorlogs_type=administratorlogs_type, administratorlogs_administrator_id=administratorlogs_administrator_id, administratorlogs_action=administratorlogs_action)
    return log_object

@app.route("/")
def index():
    return 'hello world'

@app.route("/employee", methods = ["POST"])
def create_employee():
    body = request.get_json()
    try:
        employee_object = Employee(employee_cpf=body["employee_cpf"], employee_email=body["employee_email"], employee_name=body["employee_name"], employee_password_hash=body["employee_password_hash"])
        log_object = administrator_log('POST', 1, f'CREATE A EMPLOYEE {body["employee_name"]}')
        db.session.add(employee_object)
        db.session.add(log_object)
        db.session.commit()
        return response(201, "Employee", employee_object.to_json(), "Employee created")
    except Exception as exception:
        print("Error", exception)
        return response(400, "Employee", {}, "Employee not created")
