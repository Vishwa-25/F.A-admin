from django.db import models


# Create your models here.


class face(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=20)
    email = models.EmailField()
    number = models.IntegerField()
    emp_id = models.TextField(auto_created=True)


class gender(models.Model):
    GENDER_CHOICES = (('M', 'Male'), ('F', 'Female'))
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)


def __str__(self):
    return self.name
