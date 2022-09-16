from flask import Response
import json
from app.models import User, UserLogs, Clock, ClockLogs


def generate_response(status, content_name, content, message = False):
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

def is_user(user_id):
    current_user = User.query.filter_by(user_id=user_id).first()
    if current_user == None:
        return False
    else:
        return True

def is_admin(user_id):
    current_user = User.query.filter_by(user_id=user_id).first()
    if current_user.user_is_admin == 0:
        return False
    else:
        return True
