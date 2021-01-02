from django.contrib import admin
from school.models import subject,position,teacher_id,teacher,student_id,student
# Register your models here.

admin.site.register(subject.Subject)
admin.site.register(position.TeacherPosition)
admin.site.register(teacher_id.TeacherId)
admin.site.register(teacher.Teacher)
admin.site.register(student_id.StudentId)
admin.site.register(student.Student)