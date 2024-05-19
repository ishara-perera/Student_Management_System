from django.urls import path
from . import views


urlpatterns = [
    path('subjects/', views.get_subjects, name='get_subjects'),
    path('subjects/create/', views.create_subject, name='create_subject'),
    path('subjects/<int:subject_id>/', views.get_subject, name='get_subject'),
    path('subjects/<int:subject_id>/update/', views.update_subject, name='update_subject'),
    path('subjects/<int:subject_id>/delete/', views.delete_subject, name='delete_subject'),

    path('students/create/', views.create_student, name='create_student'),
    path('students/', views.get_students, name='get_students')
]
