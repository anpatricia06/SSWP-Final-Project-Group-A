from django.shortcuts import render
from school.models.student import Student
from school.models.teacher import Teacher

def index(request):
  
    num_visit= request.session.get('num_visit', 1)
    request.session['num_visit']= num_visit + 1
    
    num_student = Student.objects.all().count()
    num_teacher = Teacher.objects.all().count()
    context = {
        'num_student': num_student,
        'num_teacher': num_teacher,
        'total_visit': num_visit,
        
    
    }
    return render(request, 'index.html', context=context)
