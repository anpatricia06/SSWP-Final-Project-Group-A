#buat bagian home dan ada tampilan bagian session
from django.shortcuts import render
from school.models.student import Student

#ini buat sementara doang, aslinya dipkein session yg isinya num_students, num_teacher, total_visit
def index(request):
    students= Student.objects.all()
    context = {
        'students': students,
    }
    return render(request, 'index.html', context=context)
