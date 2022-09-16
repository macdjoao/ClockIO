from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, DateTimeField
from wtforms.validators import DataRequired


#'BooleanField', 'DecimalField', 'DateField', 'DateTimeField', 'FieldList',
#'FloatField', 'FormField', 'IntegerField', 'RadioField', 'SelectField',
#'SelectMultipleField', 'StringField', 'TimeField'

class LoginForm(FlaskForm):
    user_cpf = StringField('cpf', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])

class NewPassword(FlaskForm):
    # when first_access is true, the user must redefine his password
    pass

class CreateUserForm(FlaskForm):
    user_cpf = StringField('user_cpf', validators=[DataRequired()])
    user_name = StringField('user_name', validators=[DataRequired()])

    # must be cpf for default, user must change the password in first access
    user_password = PasswordField('user_password', validators=[DataRequired()])

class UpdateUserForm(FlaskForm):
    # select user (selectfield)
    user_cpf = StringField('user_cpf')
    user_name = StringField('user_name')

    # must change the actual password to user_cpf
    user_first_access = BooleanField('user_first_access')
    user_status = BooleanField('user_status')

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

class ReadClockWithFilters(FlaskForm):
    # select user (selectfield) (all, one or many)
    # select first_date
    # select last_date
    # select extra
    pass
