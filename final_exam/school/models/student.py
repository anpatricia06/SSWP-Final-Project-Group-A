from django.db import models
from school.models.student_id import StudentId
from school.models.teacher_id import TeacherId

class Student(models.Model):
    student_id= models.OneToOneField(StudentId, on_delete=models.CASCADE)
    s_name= models.CharField('Name',max_length=30)
    s_dob= models.DateField('Date of Birth',null=True)
    s_address= models.CharField('Address',max_length=50)
    s_phonenum= models.CharField('Phone Number:',max_length=20)
    s_email= models.CharField('E-mail',max_length=30)
    teacher_id= models.ForeignKey(TeacherId, on_delete=models.CASCADE)
    
    class Meta:
        app_label= 'school'

    def __str__(self):
        return f'{self.s_name}'