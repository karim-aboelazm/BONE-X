from django.conf.urls import url
from django.urls import path,include
from . import views
app_name='home'
urlpatterns = [
    path('',views.main_page,name='home_page'),
]

