from django.shortcuts import render
from school.models.teacher import Teacher
from school.forms import TeacherForm

def delete_teacher(request, teacher_id):
    teacher = Teacher.objects.get(pk=teacher_id)
    if request.method == 'POST':
        teacher.delete()
        return HttpResponseRedirect(reverse('teachers'))
    context = {
        'teacher': teacher
    }
    return render(request, 'teacher_delete_form.html', context=context)
