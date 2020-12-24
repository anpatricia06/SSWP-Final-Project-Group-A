from django.db import models

class StudentId(models.Model):
    s_id= models.CharField(max_length=10)
    
    class Meta:
        app_label= 'school'

    def __str__(self):
        return f'{self.s_id}'