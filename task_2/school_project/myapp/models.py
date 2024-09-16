from django.db import models
from django.core.validators import EmailValidator, MinValueValidator, MaxValueValidator

class UserRole(models.TextChoices):
    STUDENT = 'student'
    TEACHER = 'teacher'

class Class(models.Model):
    name = models.CharField(max_length=3, unique=True)
    subjects = models.ManyToManyField('Subject', related_name='classes')

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, unique=True, validators=[EmailValidator()])
    password_hash = models.CharField(max_length=255)
    role = models.CharField(max_length=10, choices=UserRole.choices)
    class_id = models.ForeignKey(Class, null=True, blank=True, on_delete=models.SET_NULL, related_name='students')
    subjects = models.ManyToManyField('Subject', related_name='teachers')

class Subject(models.Model):
    name = models.CharField(max_length=30)

class Grade(models.Model):
    grade = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    date = models.DateField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey(User, related_name='teacher_grades', on_delete=models.CASCADE)
    student = models.ForeignKey(User, related_name='student_grades', on_delete=models.CASCADE)
