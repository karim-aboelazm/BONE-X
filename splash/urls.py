from django.conf.urls import url
from django.urls import path,include
from . import views
app_name='splash'
urlpatterns = [
    path('',views.splash,name='splash'),
]

