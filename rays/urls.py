from django.conf.urls import url
from django.urls import path,include
from . import views
app_name='rays'
urlpatterns = [
    path('',views.rays,name='rays'),
]

