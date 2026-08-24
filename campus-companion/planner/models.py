from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=120)
    code = models.CharField(max_length=20, blank=True)
    instructor = models.CharField(max_length=100, blank=True)
    color = models.CharField(max_length=7, default='#6C63FF')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f'{self.code} — {self.name}' if self.code else self.name


class ClassSchedule(models.Model):
    DAYS = [(i, day) for i, day in enumerate(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])]
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='classes')
    day = models.PositiveSmallIntegerField(choices=DAYS)
    start_time = models.TimeField()
    end_time = models.TimeField()
    room = models.CharField(max_length=80, blank=True)

    class Meta:
        ordering = ['day', 'start_time']


class Assignment(models.Model):
    STATUS = [('todo', 'To do'), ('doing', 'In progress'), ('done', 'Done')]
    title = models.CharField(max_length=150)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, blank=True, related_name='assignments')
    due_date = models.DateTimeField()
    status = models.CharField(max_length=10, choices=STATUS, default='todo')
    details = models.TextField(blank=True)

    class Meta:
        ordering = ['due_date']


class Note(models.Model):
    title = models.CharField(max_length=150)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, blank=True, related_name='notes')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']


class CampusEvent(models.Model):
    title = models.CharField(max_length=150)
    date = models.DateTimeField()
    location = models.CharField(max_length=120, blank=True)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ['date']

# Create your models here.
