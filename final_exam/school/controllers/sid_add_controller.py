from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from school.models.student_id import StudentId
from school.forms import StudentIdForm
 
def add_student_id(request):
    if request.method == 'POST':
        form = StudentIdForm(request.POST)
        if form.is_valid():
            form.save()  # directly save the form
            return HttpResponseRedirect(reverse('studentid_add'))
    else:
        form = StudentIdForm()
 
    context = {
        'form': form
    }
    return render(request, 'sid_form.html', context=context)
