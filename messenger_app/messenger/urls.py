from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('write_message/', views.write_message, name='write_message'),
    path('write_message/<int:message_id>/', views.write_message, name='edit_draft'),
    path('sent_messages/', views.sent_messages, name='sent_messages'),
    path('draft_messages/', views.draft_messages, name='draft_messages'),
    path('delete_message/<int:message_id>/', views.delete_message, name='delete_message'),
    path('delete_draft/<int:draft_id>/', views.delete_draft, name='delete_draft'),
]
