from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Person(Base):
    __tablename__ = 'person'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

    def __repr__(self):
        return "<{}>".format(self.name)

engine = create_engine('sqlite:///sqlalchemy_example.db')

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

DBSession = sessionmaker(bind=engine)
session = DBSession()

for i in range(100):
    new_person = Person(name='new person #%s' % i)
    session.add(new_person)
session.commit()

query = session.query(Person)
print(query.count())  # 100
print

from paginate_sqlalchemy import SqlalchemyOrmPage

page = SqlalchemyOrmPage(query, page=5, items_per_page=8)
print(page)
print(page.items)
print(page.items[6].name)
print(page.page_count)
