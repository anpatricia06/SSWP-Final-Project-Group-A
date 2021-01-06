from django.urls import path

from school.controllers import index_controller, sid_controller,  sid_add_controller, student_controller, tid_controller, tid_add_controller, teacher_controller, subject_controller, std_add_controller, std_edit_controller, std_del_controller, tch_add_controller, tch_edit_controller, tch_del_controller, registration_controller, oxford_dict_controller, extracurricular_controller

urlpatterns= [
    path('', index_controller.index, name='index'),
    path('studentid/', sid_controller.list_student_ids, name='studentid'),
    path('studentid/add/', sid_add_controller.add_student_id, name='studentid_add'),
    path('students/', student_controller.list_students, name='students'),
    path('student/add', std_add_controller.add_student, name='add_student'),
    path('student/edit/<int:student_id>', std_edit_controller.edit_student, name='edit_student'),
    path('student/delete/<int:student_id>', std_del_controller.delete_student, name='delete_student'),
    path('teacherid/', tid_controller.list_teacher_ids, name='teacherid'),
    path('teacherid/add/', tid_add_controller.add_teacher_id, name='teacherid_add'),
    path('teachers/', teacher_controller.list_teachers, name='teachers'),
    path('teacher/add', tch_add_controller.add_teacher, name='add_teacher'),
    path('teacher/edit/<int:teacher_id>', tch_edit_controller.edit_teacher, name='edit_teacher'),
    path('teacher/delete/<int:teacher_id>', tch_del_controller.delete_teacher, name='delete_teacher'),
    path('subjects/', subject_controller.list_subjects, name='subjects'),
    path('register', registration_controller.index, name='register'),
    path('oxforddict', oxford_dict_controller.oxford, name='oxford'),
    path('extracurricular', extracurricular_controller.list_extracurriculars, name='extracurricular'),
]
