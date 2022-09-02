from .models import EmployeeLogs, AdministratorLogs
from flask import Response
import json


def response(status, content_name, content, message = False):
    body = {}
    body[content_name]=content
    if (message):
        body['Message']=message
    return Response(json.dumps(body, default=str), status=status, mimetype='application/json')

def validator_cpf(cpf):
    valid_cpf = str(cpf)
    valid_cpf = valid_cpf.replace('-', '')
    valid_cpf = valid_cpf.replace('.', '')
    valid_cpf = valid_cpf.replace(' ', '')
    if valid_cpf.isdigit() and len(valid_cpf) == 11:
        return valid_cpf
    else:
        raise ValueError

def employee_log(employeelogs_type, employeelogs_employee_id, employeelogs_action):
    log_object = EmployeeLogs(employeelogs_type=employeelogs_type, employeelogs_employee_id=employeelogs_employee_id, employeelogs_action=employeelogs_action)
    return log_object

def administrator_log(administratorlogs_type, administratorlogs_administrator_id, administratorlogs_action):
    log_object = AdministratorLogs(administratorlogs_type=administratorlogs_type, administratorlogs_administrator_id=administratorlogs_administrator_id, administratorlogs_action=administratorlogs_action)
    return log_object
