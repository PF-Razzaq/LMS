from django.db import models

class Teacher(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    qualification = models.CharField(max_length=100)
    mobile_no = models.CharField(max_length=11)
    address =  models.TextField()

    class Meta:
        db_table = 'Teacher'
        verbose_name_plural = "1. Teachers"
    def __str__(self):
        return self.full_name
        

class CourseCategory(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        db_table = 'CourseCategory'
        verbose_name_plural = "2. Course Category"
    def __str__(self):
        return self.title

class Course(models.Model):
    category = models.ForeignKey(CourseCategory, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        db_table = 'Course'
        verbose_name_plural = "3. Courses"
    def __str__(self):
        return self.category
class Student(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    qualification = models.CharField(max_length=100)
    mobile_no = models.CharField(max_length=11)
    address =  models.TextField()
    interested_categories = models.TextField()

    class Meta:
        db_table = 'Student'
        verbose_name_plural = "4. Students"
    def __str__(self):
        return self.full_name
# Create your models here.
