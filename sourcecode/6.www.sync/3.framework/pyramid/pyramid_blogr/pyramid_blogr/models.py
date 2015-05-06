import datetime

from pyramid_sqlalchemy import BaseObject, Session
from paginate_sqlalchemy import SqlalchemyOrmPage
from sqlalchemy import Column, DateTime, Integer, Unicode, UnicodeText, desc


class User(BaseObject):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(Unicode(255), unique=True, nullable=False)
    password = Column(Unicode(255), nullable=False)
    last_logged = Column(DateTime, default=datetime.datetime.utcnow)


class Article(BaseObject):
    __tablename__ = 'articles'
    id = Column(Integer, primary_key=True)
    title = Column(Unicode(255), unique=True, nullable=False)
    content = Column(UnicodeText, default=u'')
    created = Column(DateTime, default=datetime.datetime.utcnow)
    edited = Column(DateTime, default=datetime.datetime.utcnow)

    @classmethod
    def get_paginator(cls, request, page=1):
        query = Session.query(Article).order_by(desc(Article.created))
        query_params = request.GET.mixed()

        def url_maker(link_page):
            query_params['page'] = link_page
            return request.current_route_url(_query=query_params)
        return SqlalchemyOrmPage(query, page, items_per_page=5,
                                 url_maker=url_maker)
