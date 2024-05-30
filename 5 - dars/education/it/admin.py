from django.contrib import admin
from .models import Courses, Student, Status, Experience, Teachers

# Register your models here.

admin.site.register(Courses)
admin.site.register(Status)
admin.site.register(Student)
admin.site.register(Experience)
admin.site.register(Teachers)
