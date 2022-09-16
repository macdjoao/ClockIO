from datetime import datetime
from . import db
from werkzeug.security import generate_password_hash, check_password_hash

# Migrate updates to the database
# $ flask db stamp head
# $ flask db migrate
# $ flask db upgrade

class User(db.Model):
    __tablename__ = 'users'

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_cpf = db.Column(db.String(11), nullable=False, unique=True)
    user_name = db.Column(db.String(255), nullable=False)
    user_password = db.Column(db.String(255), nullable=False)
    user_first_access = db.Column(db.Boolean, nullable=False, default=True)
    user_status = db.Column(db.Boolean, nullable=False, default=True)
    user_is_admin = db.Column(db.Boolean, nullable=False, default=False)

    def __init__(self, user_cpf, user_name, user_password, user_first_access, user_status, user_is_admin):
        self.user_cpf = user_cpf
        self.user_name = user_name
        self.user_password = generate_password_hash(user_password)
        self.user_first_access = user_first_access
        self.user_status = user_status
        self.user_is_admin = user_is_admin

    def __repr__(self):
        return f'<user_id: {self.user_id}, user_cpf: {self.user_cpf}, user_name: {self.user_name}, user_first_access: {self.user_first_access}, user_status: {self.user_status}, user_is_admin: {self.user_is_admin}>'

    def to_json(self):
        return {"user_id": self.user_id, "user_cpf": self.user_cpf, "user_name": self.user_name, "user_first_access": self.user_first_access, "user_status": self.user_status, "user_is_admin": self.user_is_admin}

    def verify_password(self, user_password):
        return check_password_hash(self.user_password, user_password)

class UserLogs(db.Model):
    __tablename__ = 'userlogs'

    userlogs_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    userlogs_datetime = db.Column(db.DateTime, default=datetime.utcnow)
    userlogs_type = db.Column(db.String(255), nullable=False)
    userlogs_user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    userlogs_action = db.Column(db.Text, nullable=False)

    # user = db.relationship('users', foreign_keys=userlogs_user_id)

    def __init__(self, userlogs_type, userlogs_user_id, userlogs_action):
        self.userlogs_type = userlogs_type
        self.userlogs_user_id = userlogs_user_id
        self.userlogs_action = userlogs_action

    def __repr__(self):
        return f'<userlogs_id: {self.userlogs_id}, userlogs_datetime: {self.userlogs_datetime}, userlogs_type: {self.userlogs_type}, userlogs_user_id: {self.userlogs_user_id}, userlogs_action: {self.userlogs_action}>'

    def to_json(self):
        return {"userlogs_id": self.userlogs_id, "userlogs_datetime": self.userlogs_datetime, "userlogs_type": self.userlogs_type, "userlogs_user_id": self.userlogs_user_id, "userlogs_action": self.userlogs_action}

class Clock(db.Model):
    __tablename__ = 'clocks'

    clock_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    clock_user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    clock_input = db.Column(db.DateTime, nullable=False)
    clock_output = db.Column(db.DateTime, nullable=False)
    clock_extra = db.Column(db.Boolean, default=False)

    # user = db.relationship('user', foreign_keys=clock_user_id)

    def __init__(self, clock_user_id, clock_input, clock_output, clock_extra):
        self.clock_user_id = clock_user_id
        self.clock_input = clock_input
        self.clock_output = clock_output
        self.clock_extra = clock_extra

    def __repr__(self):
        return f'<clock_id: {self.clock_id}, clock_user_id: {self.clock_user_id}, clock_input: {self.clock_input}, clock_output: {self.clock_output}, clock_extra: {self.clock_extra}>'

    def to_json(self):
        return {"clock_id": self.clock_id, "clock_user_id": self.clock_user_id, "clock_input": self.clock_input, "clock_output": self.clock_output, "clock_extra": self.clock_extra}

class ClockLogs(db.Model):
    __tablename__ = 'clocklogs'

    clocklogs_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    clocklogs_clock_id = db.Column(db.Integer, db.ForeignKey("clocks.clock_id"))
    clocklogs_datetime = db.Column(db.DateTime, default=datetime.utcnow)
    clocklogs_type = db.Column(db.String(255), nullable=False)
    clocklogs_user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))

    # user = db.relationship('user', foreign_keys=clocklogs_user_id)
    # clock = db.relationship('clock', foreign_keys=clocklogs_clock_id)

    def __init__(self, clocklogs_clock_id, clocklogs_type, clocklogs_user_id):
        self.clocklogs_clock_id = clocklogs_clock_id
        self.clocklogs_type = clocklogs_type
        self.clocklogs_user_id = clocklogs_user_id

    def __repr__(self):
        return f'<userlogs_id: {self.userlogs_id}, clocklogs_clock_id: {self.clocklogs_clock_id}, clocklogs_datetime: {self.clocklogs_datetime}, clocklogs_type: {self.clocklogs_type}, clocklogs_user_id: {self.clocklogs_user_id}>'

    def to_json(self):
        return {"userlogs_id": self.userlogs_id, "clocklogs_clock_id": self.clocklogs_clock_id, "clocklogs_datetime": self.clocklogs_datetime, "userlogs_type": self.clocklogs_type, "clocklogs_user_id": self.clocklogs_user_id}
