from django.contrib import admin
from django.urls import path
from .views import student_list

urlpatterns = [
    path('studentview/',student_list),
]