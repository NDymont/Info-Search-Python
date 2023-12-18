from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('universities/add', views.universities_add),
    path('universities', views.universities_view),
    path('universities/<int:pk>/update', views.UniversitiesUpdateView.as_view(), name='universities-update'),
    path('universities/<int:pk>/delete', views.UniversitiesDeleteView.as_view(), name='universities-delete'),

    path('students', views.students_view),
    path('students/add', views.students_add),
    path('students/<int:pk>/update', views.StudentsUpdateView.as_view(), name='students-update'),
    path('students/<int:pk>/delete', views.StudentsDeleteView.as_view(), name='students-delete'),

]


