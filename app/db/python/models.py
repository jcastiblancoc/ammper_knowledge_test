from sqlalchemy.ext.hybrid import hybrid_property

from sqlalchemy.sql.functions import now

from connection import Base, session
from sqlalchemy import Column, String, Table, ForeignKey, LargeBinary, Integer, func, DateTime, Float
from sqlalchemy.orm import relationship, column_property


class User(Base):
    __tablename__ = 'users'

    id = Column(String, primary_key=True)
    created_at = Column(DateTime, default=now())
    first_name = Column(String)
    last_name = Column(String)
    full_name = column_property(first_name + " " + last_name)
    nickname = Column(String)
    email = Column(String)
    birthdate = Column(String)
    phone = Column(String)
    country = Column(String)
    state = Column(String)
    city = Column(String)
    street_address = Column(String)
    postal_code = Column(String)
