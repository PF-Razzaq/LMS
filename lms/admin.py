from django.contrib import admin
from .models import Teacher, CourseCategory, Course, Student

admin.site.register((Teacher, CourseCategory, Course, Student))
# Register your models here.
