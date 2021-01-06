from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from school.models.teacher_id import TeacherId
from school.forms import TeacherIdForm
 
def add_teacher_id(request):
    if request.method == 'POST':
        form = TeacherIdForm(request.POST)
        if form.is_valid():
            form.save()  # directly save the form
            return HttpResponseRedirect(reverse('teacherid_add'))
    else:
        form = TeacherIdForm()
 
    context = {
        'form': form
    }
    return render(request, 'tid_form.html', context=context)

