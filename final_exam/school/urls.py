from django.urls import path
from school.controllers import index_controller, student_controller, teacher_controller, subject_controller, std_add_controller, std_edit_controller, std_del_controller, tch_add_controller, tch_edit_controller, tch_del_controller

urlpatterns= [
    path('', index_controller.index, name='index'),
    path('students/', student_controller.list_students, name='students'),
    path('student/add', std_add_controller.add_student, name='add_student'),
    path('student/edit/<int:student_id>', std_edit_controller.edit_student, name='edit_student'),
    path('student/delete/<int:student_id>', std_del_controller.delete_student, name='delete_student'),
    path('teachers/', teacher_controller.list_teachers, name='teachers'),
    path('teacher/add', tch_add_controller.add_teacher, name='add_teacher'),
    path('teacher/edit/<int:teacher_id>', tch_edit_controller.edit_teacher, name='edit_teacher'),
    path('teacher/delete/<int:teacher_id>', tch_del_controller.delete_teacher, name='delete_teacher'),
    path('subjects/', subject_controller.list_subjects, name='subjects'),
]
