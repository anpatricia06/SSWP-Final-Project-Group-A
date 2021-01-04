from django.shortcuts import render
from school.models.teacher import Teacher
from school.forms import TeacherForm

def list_teachers(request):
    if request.method == 'POST':
        req = request.POST.dict()
        t_name = req['t_name']
        teachers = Teacher.objects.filter(name__contains=t_name)
    else:
        teachers= Teacher.objects.all()
    context={
        'teachers':teachers,
    }
    return render(request, 'teacher.html', context=context)
