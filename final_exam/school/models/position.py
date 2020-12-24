from django.db import models

class TeacherPosition(models.Model):
    position: models.CharField(max_length=30)

    class Meta:
        app_label= 'school'

    def __str__(self):
        return f'{self.position}'