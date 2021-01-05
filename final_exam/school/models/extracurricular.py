from django.db import models
 
class Extracurricular(models.Model):
    name= models.CharField(max_length=30, default='SOME STRING')
    
    class Meta:
        app_label= 'school'
 
    def __str__(self):
        return f'{self.name}'
