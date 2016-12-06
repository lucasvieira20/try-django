from django.conf.urls import url
from django.contrib import admin

from .views import(
	posts_create,
	posts_detail,
	posts_update,
	posts_delete,
)

urlpatterns = [
    url(r'^$', "posts.views.posts_list"),
    url(r'^create/$', posts_create),
    url(r'^detail/$', posts_detail),
    url(r'^update/$', posts_update),
    url(r'^delete/$', posts_delete),
    # url(r'^posts/$', "<appname>.views.<function_name>"),
]
