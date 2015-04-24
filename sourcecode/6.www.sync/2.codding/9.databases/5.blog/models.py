# -*- coding: utf-8 -*-
from jinja2.utils import generate_lorem_ipsum
from sqlalchemy import Column, Integer, String, Text, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Articles(Base):
    __tablename__ = 'articles'

    id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=False)
    content = Column(Text, nullable=False)

    def __repr__(self):
        return "<{}>".format(self.name)


engine = create_engine('sqlite:///foo.db')

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
dbsession = Session()

for id, article in enumerate(range(100), start=1):
    title = generate_lorem_ipsum(
        n=1,         # Одно предложение
        html=False,  # В виде обычного текста
        min=2,       # Минимум 2 слова
        max=5        # Максимум 5
    )
    content = generate_lorem_ipsum()
    article = Articles(**{'id': id, 'title': title, 'content': content})
    dbsession.add(article)
dbsession.commit()
dbsession.close()
