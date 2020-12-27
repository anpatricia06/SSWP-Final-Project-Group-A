from django.urls import path
from school.controllers import index_controller, student_controller, teacher_controller, stdclass_controller, subject_controller

urlpatterns= [
    path('', index_controller.index, name='index'),
    path('students/', student_controller.list_students, name='students'),
    path('teachers/', teacher_controller.list_teachers, name='teachers'),
    path('classes/', stdclass_controller.list_classes, name='classes'),
    path('subjects/', subject_controller.list_subjects, name='subjects'),
]