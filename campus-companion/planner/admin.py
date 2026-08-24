from django.contrib import admin
from .models import Assignment, CampusEvent, ClassSchedule, Course, Note

admin.site.register([Course, ClassSchedule, Assignment, Note, CampusEvent])

# Register your models here.
