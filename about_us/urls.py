from django.conf.urls import url
from django.urls import path,include
from . import views
app_name='about_us'
urlpatterns = [
    path('',views.about,name='about_us'),
]

