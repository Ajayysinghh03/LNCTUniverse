from django.contrib import admin
from .models import StudentProfile
# Register your models here.
admin.site.register(StudentProfile)
from django.contrib import admin
from .models import Timetable, Announcement

admin.site.register(Timetable)
admin.site.register(Announcement)
