from django.urls import path
from . import views

App_name = 'insta'

urlpatterns = [
    path('',views.main, name ='main'),
    path('<int:post_pk>/like/', views.like, name='like'),
    path('new/', views.new, name='new'), 
    path('<int:post_pk>/edit/', views.edit, name='edit'),
    path('<int:post_pk>/delete/', views.delete, name='delete'),
    path('<int:post_pk>/comment/', views.create_comment, name='create_comment'),
]




