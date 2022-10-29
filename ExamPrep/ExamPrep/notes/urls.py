from django.urls import path

from ExamPrep.notes.views import index, add_note, edit_note, delete_note, details_note, profile, delete_profile

urlpatterns = [
    path('', index, name='home page'),
    path('add/', add_note, name='add note'),
    path('edit/<int:pk>/', edit_note, name='edit note'),
    path('delete/<int:pk>/', delete_note, name='delete note'),
    path('details/<int:pk>/', details_note, name='details note'),
    path('profile/', profile, name='profile'),
    path('delete_profile/', delete_profile, name='delete profile'),
]