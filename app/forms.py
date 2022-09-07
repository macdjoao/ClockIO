from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, DateTimeField
from wtforms.validators import DataRequired


#'BooleanField', 'DecimalField', 'DateField', 'DateTimeField', 'FieldList',
#'FloatField', 'FormField', 'IntegerField', 'RadioField', 'SelectField',
#'SelectMultipleField', 'StringField', 'TimeField'

class LoginForm(FlaskForm):
    email = StringField('email', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    remember_me = BooleanField('remember_me')

class CreateEmployeeForm(FlaskForm):
    employee_cpf = StringField('employee_cpf', validators=[DataRequired()])
    employee_email = StringField('employee_email', validators=[DataRequired()])
    employee_name = StringField('employee_name', validators=[DataRequired()])
    employee_password_hash = PasswordField('employee_password_hash', validators=[DataRequired()])

class UpdateEmployeeForm(FlaskForm):
    employee_cpf = StringField('employee_cpf')
    employee_email = StringField('employee_email')
    employee_name = StringField('employee_name')
    employee_first_access = BooleanField('employee_first_access')

class DeleteEmployeeForm(FlaskForm):
    employee_cpf = StringField('employee_cpf', validators=[DataRequired()])

class ReadEmployeeSingleForm(FlaskForm):
    employee_cpf = StringField('employee_cpf', validators=[DataRequired()])

class CreateClockForm(FlaskForm):
    clock_input = DateTimeField('clock_input', validators=[DataRequired()])
    clock_output = DateTimeField('clock_output', validators=[DataRequired()])
    clock_extra = BooleanField('clock_extra')

class UpdateClockForm(FlaskForm):
    clock_input = DateTimeField('clock_input')
    clock_output = DateTimeField('clock_output')
    clock_extra = BooleanField('clock_extra')

class ReadClockSingleForm(FlaskForm):
    employee_cpf = StringField('employee_cpf', validators=[DataRequired()])
