from django.conf.urls import url
from django.urls import path, include

from . import views

urlpatterns = [
    path('home', views.front_page, name='studentHome'),
    #path('guestsInserted',views.guest,name='guest'),
    path('insertStudents', views.insertStudents, name='insertStudents'),
    #path('guest/<int:guest_id>/',views.guest_detail,name='guestDetail'),
    #path('insertGuests',views.insert_guest,name='insertGuest'),
    url('uploadComplete', views.upload_excel, name="uploadComplete"),
    #path('', include('django.contrib.auth.urls'), name='front'),
    path('<int:student_id>', views.studentDetail, name='studentDetail'),
    #path('guest', views.guest, name='guest'),
    path('home#',views.generateStudentSummary,name='generateStudentSummary')
]


