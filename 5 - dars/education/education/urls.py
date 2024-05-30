"""
URL configuration for education project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from it.views import (index, CourseList, CourseUpdateDelete, StatusList, StatusUpdateDelete,
                      ExperienceList, ExperienceUpdateDelete, TeacherList, TeacherUpdateDelete, StudentList,
                      StudentUpdateDelete)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('course-list/', CourseList.as_view()),
    path('course-update/<int:pk>/', CourseUpdateDelete.as_view()),
    path('status-list/', StatusList.as_view()),
    path('status-update/<int:pk>/', StatusUpdateDelete.as_view()),
    path('experience-list/', ExperienceList.as_view()),
    path('experience-update/<int:pk>/', ExperienceUpdateDelete.as_view()),
    path('teacher-list/', TeacherList.as_view()),
    path('teacher-update/<int:pk>/', TeacherUpdateDelete.as_view()),
    path('student-list/', StudentList.as_view()),
    path('student-update/<int:pk>/', StudentUpdateDelete.as_view()),
]
