from django.urls import path
from . import views

urlpatterns = [
    path('', views.chat_list, name='chat_list'),
    path('new/', views.chat_create, name='chat_create'),
    path('delete/<int:pk>/', views.chat_delete, name='chat_delete'),
]
