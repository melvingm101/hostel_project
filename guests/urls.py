from django.conf.urls import url
from django.urls import path, include

from . import views

urlpatterns=[
    #path('guestsInserted',views.guestHome,name='guest'),
    path('<int:guest_id>',views.guest_detail,name='guestDetail'),
    path('insertGuests',views.insert_guest,name='insertGuest'),
    path('home', views.guestHome, name='guestHome'),
    path('home#',views.generateGuestSummary,name='generateGuestsSummary')
]