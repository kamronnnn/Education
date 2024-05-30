from django.shortcuts import render
from .models import Courses, Student, Teachers, Experience, Status
from rest_framework import generics
from .serializers import (CoursesSerializer, StatusSerializer, ExperienceSerializer,
                          TeacherSerializer, StudentSerializer)

from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated


# Create your views here.


def index(request):
    context = {
        'course': Courses.objects.all()
    }
    return render(request, 'it/index.html', context)


class CourseList(generics.ListCreateAPIView):
    serializer_class = CoursesSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        return Courses.objects.filter(published=True)


class CourseUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Courses.objects.filter(published=True)
    serializer_class = CoursesSerializer
    permission_classes = [IsAdminUser]


# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


class StatusList(generics.ListCreateAPIView):
    serializer_class = StatusSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        return Status.objects.filter(published=True)


class StatusUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Status.objects.filter(published=True)
    serializer_class = StatusSerializer
    permission_classes = [IsAdminUser]


# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


class ExperienceList(generics.ListCreateAPIView):
    serializer_class = ExperienceSerializer

    def get_queryset(self):
        return Experience.objects.filter(published=True)


class ExperienceUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Experience.objects.filter(published=True)
    serializer_class = ExperienceSerializer


# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


class TeacherList(generics.ListCreateAPIView):
    serializer_class = TeacherSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        return Teachers.objects.filter(published=True)


class TeacherUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Teachers.objects.filter(published=True)
    serializer_class = TeacherSerializer
    permission_classes = [IsAdminUser]


# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


class StudentList(generics.ListCreateAPIView):
    serializer_class = StudentSerializer

    def get_queryset(self):
        return Student.objects.filter(published=True)


class StudentUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.filter(published=True)
    serializer_class = StudentSerializer
