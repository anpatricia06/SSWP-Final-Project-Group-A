from django.shortcuts import render
from school.models.student import Student
from school.forms import StudentForm
from django.contrib.auth.decorators import login_required

@login_required 
def delete_student(request, student_id):
    student = Student.objects.get(pk=student_id)
    if request.method == 'POST':
        student.delete()
        return HttpResponseRedirect(reverse('students'))
    context = {
        'student': student
    }
    return render(request, 'student_delete_form.html', context=context)
