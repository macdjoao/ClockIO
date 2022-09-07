from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, DateTimeField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    email = StringField('email', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    remember_me = BooleanField('remember_me')



class CreateEmployeeForm(FlaskForm):
    employee_cpf = StringField('employee_cpf', validators=[DataRequired()])
    employee_email = StringField('employee_email', validators=[DataRequired()])
    employee_name = StringField('employee_name', validators=[DataRequired()])
    employee_password_hash = PasswordField('employee_password_hash', validators=[DataRequired()])
    pass

class UpdateEmployeeForm(FlaskForm):
    pass

class DeleteEmployeeForm(FlaskForm):
    pass

class ReadEmployeeSingleForm(FlaskForm):
    pass




class CreateClockForm(FlaskForm):
    pass

class UpdateClockForm(FlaskForm):
    pass

class ReadClockSingleForm(FlaskForm):
    pass
