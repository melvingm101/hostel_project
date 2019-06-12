from django.conf.urls import url
from django.urls import path, include

from . import views

urlpatterns = [
    path('next', views.front_page, name='next'),
    path('guestsInserted',views.guest,name='guest'),
    path('insert', views.insert_excel, name='insert'),
    path('guest/<int:guest_id>/',views.guest_detail,name='guestDetail'),
    path('insertGuests',views.insert_guest,name='insertGuest'),
    url('uploadComplete', views.upload_excel, name="uploadComplete"),
    path('', include('django.contrib.auth.urls'), name='front'),
    path('student/<int:student_id>/',views.detail,name='studentDetail'),
    path('guest', views.guest, name='guest')
]


