from django.shortcuts import render
from school.models.teacher import Teacher
from school.forms import TeacherForm

def add_teacher(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()  # directly save the form
            return HttpResponseRedirect(reverse('teachers'))
    else:
        form = TeacherForm()

    context = {
        'form': form
    }
    return render(request, 'teacher_form.html', context=context)
