from django.shortcuts import render
from school.models.student import Student
from school.forms import StudentForm

def list_students(request):
    students= Student.objects.all()
    context = {
        'students': students,
    }
    return render(request, 'student.html', context=context)
