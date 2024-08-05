from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status,generics
from .models import Teacher,Student,Course,CourseCategory
from .serializers import TeacherSerializer,StudentSerializer,CourseSerializer,CourseCategorySerializer


class TeacherList(generics.ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class TeacherDetail(generics.RetrieveDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


# Create your views here.
