from django.db import models

class Dictionary(models.Model):
    word= models.CharField(max_length=100)


    class Meta:
        app_label= 'school'

    def __str__(self):
        return f'{self.word}'
