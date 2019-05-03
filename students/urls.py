from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    path('next', views.front_page, name='next'),
    path('insert', views.insert_excel, name='insert'),
    url('', views.login_page),
]


