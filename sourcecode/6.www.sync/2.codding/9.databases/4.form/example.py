from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Person(Base):
    __tablename__ = 'person'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

    def __repr__(self):
        return "<{}>".format(self.name)

from colanderalchemy import SQLAlchemySchemaNode
person = SQLAlchemySchemaNode(Person)

from deform import Form
form = Form(person, buttons=('submit',))
print(form.render())
