from pyramid.view import view_config
from .models import Article


@view_config(route_name='blog',
             renderer='blog/index.jinja2')
def index_page(request):
    page = int(request.params.get('page', 1))
    paginator = Article.get_paginator(request, page)
    return {'paginator': paginator}


@view_config(route_name='blog_article', renderer='blog/read.jinja2')
def blog_view(request):
    return {}


@view_config(route_name='blog_action', match_param='action=create',
             renderer='blog/edit.jinja2')
def blog_create(request):
    return {}


@view_config(route_name='blog_action', match_param='action=edit',
             renderer='blog/edit.jinja2')
def blog_update(request):
    return {}


@view_config(route_name='auth', match_param='action=in', renderer='string',
             request_method='POST')
@view_config(route_name='auth', match_param='action=out', renderer='string')
def sign_in_out(request):
    return {}
