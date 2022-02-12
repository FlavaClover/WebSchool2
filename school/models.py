from django.db import models
from django.contrib.auth.models import User
from school.validators import validate_age


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    student_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    patronymic = models.CharField(max_length=50, null=True)
    age = models.IntegerField(validators=[validate_age])

    @property
    def full_name(self):
        """ Return the student's full name """
        return self.surname + ' ' + self.name + ' ' + self.patronymic

    def __str__(self):
        return f'Id: {self.student_id}, {self.full_name}, Возраст: {self.age}, Логин: {self.user.username}'

    class Meta:
        ordering = ['name', 'surname', 'patronymic']

