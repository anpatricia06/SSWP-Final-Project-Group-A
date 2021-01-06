from django.shortcuts import render
from school.models.teacher_id import TeacherId
from school.forms import TeacherIdForm
 
def list_teacher_ids(request):
    teacher_ids= TeacherId.objects.all()
    context = {
        'teacher_ids': teacher_ids,
    }
    return render(request, 'tid.html', context=context)
