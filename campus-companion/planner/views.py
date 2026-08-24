from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from .forms import AssignmentForm, CourseForm, EventForm, NoteForm, ScheduleForm
from .models import Assignment, CampusEvent, ClassSchedule, Course, Note

FORMS = {'course': (CourseForm, 'Course'), 'schedule': (ScheduleForm, 'Class'), 'assignment': (AssignmentForm, 'Assignment'), 'note': (NoteForm, 'Note'), 'event': (EventForm, 'Event')}
MODELS = {'course': Course, 'schedule': ClassSchedule, 'assignment': Assignment, 'note': Note, 'event': CampusEvent}


def dashboard(request):
    now = timezone.now()
    assignments = Assignment.objects.filter(status__in=['todo', 'doing'])
    context = {
        'assignments': assignments[:6], 'events': CampusEvent.objects.filter(date__gte=now)[:5],
        'notes': Note.objects.all()[:5], 'classes': ClassSchedule.objects.all(), 'courses': Course.objects.all(),
        'assignment_count': assignments.count(), 'course_count': Course.objects.count(),
        'event_count': CampusEvent.objects.filter(date__gte=now).count(), 'today': now.weekday(),
    }
    return render(request, 'planner/dashboard.html', context)


def add_item(request, model):
    if model not in FORMS:
        return redirect('dashboard')
    form_class, label = FORMS[model]
    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'{label} saved.')
            return redirect('dashboard')
    else:
        form = form_class()
    return render(request, 'planner/form.html', {'form': form, 'label': label})


def toggle_assignment(request, pk):
    item = get_object_or_404(Assignment, pk=pk)
    item.status = 'done' if item.status != 'done' else 'todo'
    item.save()
    return redirect('dashboard')


def delete_item(request, model, pk):
    if model in MODELS:
        get_object_or_404(MODELS[model], pk=pk).delete()
        messages.success(request, 'Item deleted.')
    return redirect('dashboard')

# Create your views here.
