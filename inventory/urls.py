from django.conf.urls import url
from django.urls import path, include

from . import views

urlpatterns=[
    path('home', views.inventoryHome, name='inventoryHome'),
    path('insertInventory', views.insertInventory, name='insertInventory'),
    path('home#',views.generateInventorySummary,name='generateInventorySummary')
]