from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from school.models.student_id import StudentId
from school.forms import StudentIdForm
 
def list_student_ids(request):
    student_ids= StudentId.objects.all()
    context = {
        'student_ids': student_ids,
    }
    return render(request, 'sid.html', context=context)
