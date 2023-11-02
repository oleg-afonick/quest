from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Student(models.Model):
    Student_ID_number = models.AutoField(auto_created = True, primary_key = True)
    Full_name = models.CharField(max_length=50)
    Group_number = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.Full_name}'


class Groups(models.Model):
    Course_number = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(1), MaxValueValidator(4)])
    Group_number = models.CharField(max_length=50, primary_key = True)

    def __str__(self):
        return f'{self.Course_number}, {self.Group_number}'


class Subjects(models.Model):
    Name = models.CharField(max_length=50)
    Group_number = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.Name}, {self.Group_number}'


class Curators(models.Model):
    Full_name = models.CharField(max_length=50)
    Group_number = models.CharField(max_length=50, primary_key=True)

    def __str__(self):
        return f'{self.Full_name}, {self.Group_number}'

