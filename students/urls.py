from django.conf.urls import url
from django.urls import path, include

from . import views

urlpatterns = [
    path('next', views.front_page, name='next'),
    path('insert', views.insert_excel, name='insert'),
    url('uploadComplete', views.upload_excel, name="uploadComplete"),
    path('', include('django.contrib.auth.urls'), name='front'),
]


