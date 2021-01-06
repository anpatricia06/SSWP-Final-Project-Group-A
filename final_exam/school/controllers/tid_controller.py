from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from school.models.teacher_id import TeacherId
from school.forms import TeacherIdForm
 
def list_teacher_ids(request):
    teacher_ids= TeacherId.objects.all()
    context = {
        'teacher_ids': teacher_ids,
    }
    return render(request, 'tid.html', context=context)
