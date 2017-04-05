# coding: utf-8
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^add', views.entry_add, name='blogs_entry_add'),
    url(r'^(?P<id>\d+)', views.entry_detail, name='blogs_entry_detail'),
    url(r'', views.entry_index, name='blogs_entry_index'),
]
