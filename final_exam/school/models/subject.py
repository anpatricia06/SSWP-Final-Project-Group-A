from django.db import models

class Subject(models.Model):
    name= models.CharField(max_length=20, default='SOME STRING')

    class Meta:
        app_label= 'school'

    def __str__(self):
        return f'{self.name}'
