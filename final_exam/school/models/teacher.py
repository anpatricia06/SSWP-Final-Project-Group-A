from django.db import models
from school.models.subject import Subject
from school.models.position import TeacherPosition
from school.models.teacher_id import TeacherId

class Teacher(models.Model):
    teacher_id= models.OneToOneField(TeacherId, on_delete=models.CASCADE)
    t_name= models.CharField('Name',max_length=30)
    subject= models.ManyToManyField(Subject)
    t_dob= models.DateField('Date of Birth',null=True)
    t_address= models.CharField('Address',max_length=50)
    t_phonenum= models.CharField('Phone Number:',max_length=20)
    t_email= models.CharField('E-mail',max_length=30)
    position= models.ForeignKey(TeacherPosition, on_delete=models.CASCADE)

    class Meta:
        app_label= 'school'

    def __str__(self):
        return f'{self.t_name}'
