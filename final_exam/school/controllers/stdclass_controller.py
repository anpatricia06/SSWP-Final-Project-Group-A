from django.shortcuts import render
from school.models.student_class import StudentClass

def list_classes(request):
    classes= StudentClass.objects.all()
    context={
        'classes':classes,
    }
    return render(request, 'stdclass.html', context=data)