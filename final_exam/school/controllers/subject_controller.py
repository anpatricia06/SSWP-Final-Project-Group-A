from django.shortcuts import render
from school.models.subject import Subject

def list_subjects(request):
    subjects= Subject.objects.all()
    context={
        'subjects':subjects,
    }
    return render(request, 'subject.html', context=data)