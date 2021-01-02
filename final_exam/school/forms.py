from django.forms import ModelForm
from django.core.exceptions import ValidationError
from school.models.student import Student
from school.models.teacher import Teacher
from school.models.student_id import StudentId
from school.models.teacher_id import TeacherId
from school.models.subject import Subject
from school.models.position import TeacherPosition

class StudentForm(ModelForm):
    class Meta:
        model= Student
        fields= ['student_id', 's_name', 's_dob', 's_address', 's_phonenum', 's_email', 'teacher_id']

class TeacherForm(ModelForm):
    class Meta:
        model= Teacher
        fields=['teacher_id', 't_name', 'subject', 't_dob', 't_address', 't_phonenum', 't_email', 'position']
