from django.shortcuts import render
from school.models.extracurricular import Extracurricular
 
def list_extracurriculars(request):
    extracurriculars= Extracurricular.objects.all()
    context={
        'extracurriculars':extracurriculars,
    }
    return render(request, 'extracurricular.html', context=context)
