# -*- coding: utf-8 -*-
from sqlalchemy import Table, MetaData, Column, Integer, String, ForeignKey
from sqlalchemy.orm import mapper, relationship

metadata = MetaData()

user = Table('user', metadata,
             Column('id', Integer, primary_key=True),
             Column('name', String(50)),
             Column('fullname', String(50)),
             Column('password', String(12))
             )


address = Table('address', metadata,
                Column('id', Integer, primary_key=True),
                Column('user_id', Integer, ForeignKey('user.id')),
                Column('email_address', String(50))
                )


class User(object):
    pass


class Address(object):
    pass

print(dir(User))

mapper(
    User, user,
    properties={
        'addresses': relationship(Address, backref='user',
                                  order_by=address.c.id)
    })

print(dir(User))

mapper(Address, address)
