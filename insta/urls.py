from django.urls import path
from . import views

App_name = 'insta'

urlpatterns = [
    path('',views.main, name ='main'),
    path('new/', views.new, name='new'),
    path('<int:post_pk>/comment/', views.create_comment, name='create_comment'),
]