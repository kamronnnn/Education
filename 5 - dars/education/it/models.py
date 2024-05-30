from django.db import models


# Create your models here.


class Courses(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    duration = models.CharField(max_length=50)
    published = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Status(models.Model):
    name = models.CharField(max_length=50)
    published = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Experience(models.Model):
    name = models.CharField(max_length=150)
    published = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Teachers(models.Model):
    courses = models.ForeignKey(Courses, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=150)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    experience = models.ForeignKey(Experience, on_delete=models.CASCADE)
    published = models.BooleanField(default=True)

    def __str__(self):
        return self.fullname


class Student(models.Model):
    courses = models.ForeignKey(Courses, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teachers, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=150)
    phonenumber = models.CharField(max_length=13)
    parentsphonenumber = models.CharField(max_length=13)
    telegramlink = models.CharField(max_length=100)
    published = models.BooleanField(default=True)

    def __str__(self):
        return self.fullname
