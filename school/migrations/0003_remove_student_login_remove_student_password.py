# Generated by Django 4.0.2 on 2022-02-10 13:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_student_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='login',
        ),
        migrations.RemoveField(
            model_name='student',
            name='password',
        ),
    ]
