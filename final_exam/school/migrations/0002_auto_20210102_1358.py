# Generated by Django 3.1.2 on 2021-01-02 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='name',
            field=models.CharField(default='SOME STRING', max_length=20),
        ),
        migrations.AddField(
            model_name='teacherposition',
            name='position',
            field=models.CharField(default='SOME STRING', max_length=30),
        ),
    ]
