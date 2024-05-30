from rest_framework import serializers
from .models import Courses, Student, Experience, Teachers, Status


class CoursesSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    price = serializers.IntegerField(default=0)
    duration = serializers.CharField(max_length=50)
    published = serializers.BooleanField(default=True)

    def create(self, validated_data):
        return Courses.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.price = validated_data.get('price', instance.price)
        instance.duration = validated_data.get('duration', instance.duration)
        instance.published = validated_data.get('published', instance.published)
        instance.save()
        return instance


# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


class StatusSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    published = serializers.BooleanField(default=True)

    def create(self, validated_data):
        return Status.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.published = validated_data.get('published', instance.published)
        instance.save()
        return instance


# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


class ExperienceSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=150)
    published = serializers.BooleanField(default=True)

    def create(self, validated_data):
        return Experience.objects.filter(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.published = validated_data.get('published', instance.published)
        instance.save()
        return instance


# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


class TeacherSerializer(serializers.Serializer):
    courses_id = serializers.IntegerField()
    fullname = serializers.CharField(max_length=150)
    status_id = serializers.IntegerField()
    experience_id = serializers.IntegerField()
    published = serializers.BooleanField(default=True)

    def create(self, validated_data):
        return Teachers.objects.filter(**validated_data)

    def update(self, instance, validated_data):
        instance.courses_id = validated_data.get('course_id', instance.courses_id)
        instance.fullname = validated_data.get('fullname', instance.fullname)
        instance.status_id = validated_data.get('status_id', instance.status_id)
        instance.experience_id = validated_data.get('experience_id', instance.experience_id)
        instance.published = validated_data.get('published', instance.published)
        instance.save()
        return instance


# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


class StudentSerializer(serializers.Serializer):
    courses_id = serializers.IntegerField()
    teacher_id = serializers.IntegerField()
    fullname = serializers.CharField(max_length=150)
    phonenumber = serializers.IntegerField(max_value=13)
    parentsphonenumber = serializers.IntegerField(max_value=13)
    telegramlink = serializers.CharField(max_length=100)
    published = serializers.BooleanField(default=True)

    def create(self, validated_data):
        return Student.objects.filter(**validated_data)

    def update(self, instance, validated_data):
        instance.courses_id = validated_data.get('course_id', instance.courses_id)
        instance.teacher_id = validated_data.get('teacher_id', instance.teacher_id)
        instance.fullname = validated_data.get('fullname', instance.fullname)
        instance.phonenumber = validated_data.get('phonenumber', instance.phonenumber)
        instance.parentsphonenumber = validated_data.get('parentsphonenumber', instance.parentsphonenumber)
        instance.telegramlink = validated_data.get('telegramlink', instance.telegramlink)
        instance.published = validated_data.get('published', instance.published)
        instance.save()
        return instance
