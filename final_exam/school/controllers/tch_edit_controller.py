from django.shortcuts import render
from school.models.teacher import Teacher
from school.forms import TeacherForm

def edit_teacher(request, teacher_id):
    if request.method == 'POST':
        teacher = Teacher.objects.get(pk=teacher_id)
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('teachers'))
    else:
        teacher = Teacher.objects.get(pk=teacher_id)
        fields = model_to_dict(teacher)
        form = TeacherForm(initial=fields, instance=teacher)
    context = {
        'form': form,
        'type': 'edit',
    }
    return render(request, 'teacher_form.html', context=context)
