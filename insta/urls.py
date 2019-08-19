from django.urls import path
from . import views

App_name = 'insta'

urlpatterns = [
    path('',views.main, name ='main'),
    path('new/', views.new, name='new'),
]