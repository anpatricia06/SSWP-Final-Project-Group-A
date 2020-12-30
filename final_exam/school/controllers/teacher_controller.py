from django.shortcuts import render
from school.models.teacher import Teacher
from school.forms import TeacherForm

def list_teachers(request):
    teachers= Teacher.objects.all()
    context={
        'teachers':teachers,
    }
    return render(request, 'teacher.html', context=context)
