from django.shortcuts import render
from school.models.student import Student
from school.forms import StudentForm
from django.contrib.auth.decorators import login_required

@login_required 
def edit_student(request, student_id):
    if request.method == 'POST':
        student = Student.objects.get(pk=student_id)
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('students'))
    else:
        student = Student.objects.get(pk=student_id)
        fields = model_to_dict(student)
        form = StudentForm(initial=fields, instance=student)
    context = {
        'form': form,
        'type': 'edit',
    }
    return render(request, 'student_form.html', context=context)
