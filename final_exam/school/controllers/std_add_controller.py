from django.shortcuts import render
from school.models.student import Student
from school.forms import StudentForm
from django.contrib.auth.decorators import login_required

@login_required 
def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()  # directly save the form
            return HttpResponseRedirect(reverse('students'))
    else:
        form = StudentForm()

    context = {
        'form': form
    }
    return render(request, 'student_form.html', context=context)
