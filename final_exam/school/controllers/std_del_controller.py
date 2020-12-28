from django.shortcuts import render
from school.models.student import Student
#ini bagian buat import dari form

def delete_student(request, student_id):
    student = Student.objects.get(pk=student_id)
    if request.method == 'POST':
        student.delete()
        return HttpResponseRedirect(reverse('students'))
    context = {
        'student': student
    }
    return render(request, 'student_delete_form.html', context=context)
