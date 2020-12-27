from django.shortcuts import render
from school.models.teacher import Teacher
#buat naro form di bagian sini

def list_teachers(request):
    teachers= Teacher.objects.all()
    context={
        'teachers':teachers,
    }
    return render(request, 'teacher.html', context=data)