from pony.orm import Database, Required, Optional
from datetime import datetime
from flask_login import UserMixin
db = Database()


class User(db.Entity, UserMixin):
    login = Required(str, unique=True)
    password = Required(str)
    last_login = Optional(datetime)


class Company(db.Entity):
    name = Required(str)
