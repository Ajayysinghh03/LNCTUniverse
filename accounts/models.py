from django.contrib.auth.models import AbstractUser
from django.db import models

class StudentProfile(AbstractUser):
    enrollment_number = models.CharField(max_length=20, unique=True)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')])
    course = models.CharField(max_length=100)
    year = models.IntegerField(null=True, blank=True)
    semester = models.IntegerField(null=True, blank=True)
    cgpa = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    department = models.CharField(max_length=50,choices=[
        ('CSE', 'Computer Science and Engineering'),
        ('ECE', 'Electronics and Communication Engineering'),
        ('ME', 'Mechanical Engineering'),
        ('CE', 'Civil Engineering'),
        ('EE', 'Electrical Engineering'),
        ('IT', 'Information Technology'),
    ], default='CSE')

    def __str__(self):
        return f"{self.username} ({self.enrollment_number})"


from django.db import models
from django.contrib.auth.models import User

# Timetable Model
class Timetable(models.Model):
    day = models.CharField(max_length=10, choices=[
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
    ])
    subject = models.CharField(max_length=100)
    time = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.subject} ({self.day} at {self.time})"

# Announcement Model
class Announcement(models.Model):
    title = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
