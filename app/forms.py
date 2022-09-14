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

class NewPassword(FlaskForm):
    # when first_access is true, the user must redefine his password
    pass

class CreateEmployeeForm(FlaskForm):
    employee_cpf = StringField('employee_cpf', validators=[DataRequired()])
    employee_email = StringField('employee_email', validators=[DataRequired()])
    employee_name = StringField('employee_name', validators=[DataRequired()])

    # must be cpf for default, user must change the password in first access
    employee_password_hash = PasswordField('employee_password_hash', validators=[DataRequired()])

class UpdateEmployeeForm(FlaskForm):
    # select employee (selectfield)
    employee_cpf = StringField('employee_cpf')
    employee_email = StringField('employee_email')
    employee_name = StringField('employee_name')

    # must change the actual password to employee_cpf
    employee_first_access = BooleanField('employee_first_access')

class DeleteEmployeeForm(FlaskForm):
    # select employee (selectfield)
    pass

class CreateClockForm(FlaskForm):
    clock_input = DateTimeField('clock_input', validators=[DataRequired()])
    clock_output = DateTimeField('clock_output', validators=[DataRequired()])
    clock_extra = BooleanField('clock_extra')

class UpdateClockForm(FlaskForm):
    # select clock (clock_id)
    clock_input = DateTimeField('clock_input')
    clock_output = DateTimeField('clock_output')
    clock_extra = BooleanField('clock_extra')

class ReadClockAll(FlaskForm):
    # select all registers, with pagination
    pass

class ReadClockSingleForm(FlaskForm):
    # select employee registers (selectfield)
    pass

class ReadClockWithFilters(FlaskForm):
    # select employee (selectfield) (all, one or many)
    # select first_date
    # select last_date
    # select extra
    pass
