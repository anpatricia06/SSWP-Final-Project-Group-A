from django.db import models

class StudentClass(models.Model):
    name= models.CharField(max_length=10)
    floor= models.IntegerField()

    class Meta:
        app_label= 'school'

    def __str__(self):
        return f'{self.name}, {self.floor}'
