from django import forms
from .models import Assignment, CampusEvent, ClassSchedule, Course, Note


class StyledForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'input'


class CourseForm(StyledForm):
    class Meta:
        model = Course
        fields = ['name', 'code', 'instructor', 'color']
        widgets = {'color': forms.TextInput(attrs={'type': 'color'})}


class ScheduleForm(StyledForm):
    class Meta:
        model = ClassSchedule
        fields = ['course', 'day', 'start_time', 'end_time', 'room']
        widgets = {'start_time': forms.TimeInput(attrs={'type': 'time'}), 'end_time': forms.TimeInput(attrs={'type': 'time'})}


class AssignmentForm(StyledForm):
    class Meta:
        model = Assignment
        fields = ['title', 'course', 'due_date', 'status', 'details']
        widgets = {'due_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}), 'details': forms.Textarea(attrs={'rows': 3})}


class NoteForm(StyledForm):
    class Meta:
        model = Note
        fields = ['title', 'course', 'content']
        widgets = {'content': forms.Textarea(attrs={'rows': 6})}


class EventForm(StyledForm):
    class Meta:
        model = CampusEvent
        fields = ['title', 'date', 'location', 'description']
        widgets = {'date': forms.DateTimeInput(attrs={'type': 'datetime-local'}), 'description': forms.Textarea(attrs={'rows': 3})}
