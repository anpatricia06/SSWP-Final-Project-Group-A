from django.db import models

class TeacherId(models.Model):
    t_id= models.CharField(max_length=10)
    
    class Meta:
        app_label= 'school'

    def __str__(self):
        return f'{self.t_id}'