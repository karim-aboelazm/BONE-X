from django.conf.urls import url
from django.urls import path,include
from . import views
app_name='Doctors'
urlpatterns = [
    path('',views.doctors,name='doc'),
]

