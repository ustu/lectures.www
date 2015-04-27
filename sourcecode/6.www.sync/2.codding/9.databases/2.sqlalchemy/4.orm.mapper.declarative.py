# -*- coding: utf-8 -*-
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    password = Column(String)

    addresses = relationship("Address", backref="user",
                             order_by="Address.id")


class Address(Base):
    __tablename__ = 'address'

    id = Column(Integer, primary_key=True)
    user_id = Column(ForeignKey('user.id'))
    email_address = Column(String)

address1 = Address(email_address="vas@example.com")
address2 = Address(email_address="vas2@example.com")
address3 = Address(email_address="vasya@example.com")

print("Mapper relationship: " + str(User.__mapper__.relationships))
print("Mapper columns: " + str(User.__mapper__.c.items()))
print

user1 = User(name="Вася")
user1.addresses = [address1, address2, address3]
print("User1 columns: " + str(user1.__table__.c.items()))
print
print(address1.user.name)
