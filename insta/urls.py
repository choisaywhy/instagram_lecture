from django.urls import path
from . import views

App_name = 'insta'

urlpatterns = [
    path('',views.index, name ='index'),
]