from . import views
from django.urls import path

urlpatterns = [
    path("",views.firstlogin),
    path('login.html',views.login),
    path('index.html',views.index),
    path('registerindex.html',views.register),
    path('CATALOGUE SEEING.HTML',views.catalogue_seeing),
    path('contact.html',views.address),
    path('harmonyindex.html',views.harmonyindex),
    path('logincopy.html',views.login_copy),
    path('registerindex copy.html',views.register_index_copy),
    path('CATALOGUE.HTML',views.catalogue_add),
    path('CATALOGUESEEINGcopy.HTML',views.catalogue_seeing_copy),
    
]
