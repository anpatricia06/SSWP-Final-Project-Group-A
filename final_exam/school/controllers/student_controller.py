from django.shortcuts import render
from school.models.student import Student
from school.forms import StudentForm

def list_students(request):
    if request.method == 'POST':
        req = request.POST.dict()
        s_name = req['s_name']
        students = Student.objects.filter(name__contains=s_name)
    else:
        students= Student.objects.all()
    context = {
        'students': students,
    }
    return render(request, 'student.html', context=context)
