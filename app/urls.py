# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_list, name='user_list'),
    path('create/', views.user_create, name='user_create'),
    path('update/<int:id>/', views.user_update, name='user_update'),
    path('delete/<int:id>/', views.user_delete, name='user_delete'),
]
