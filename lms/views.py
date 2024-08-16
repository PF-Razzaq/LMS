from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status,generics,permissions
from .models import Teacher,Student,Course,CourseCategory
from .serializers import TeacherSerializer
from django.http import JsonResponse


class TeacherList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    def get(self, request, *args, **kwargs):
        try:
            return self.list(request, *args, **kwargs)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request, *args, **kwargs):
        try:
            return self.create(request, *args, **kwargs)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class TeacherDetail(generics.RetrieveDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

