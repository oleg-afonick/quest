from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Groups(models.Model):
    Course_number = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(1), MaxValueValidator(4)])
    Group_number = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f'{self.Group_number}'


class Marks(models.Model):
    name_subject = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name_subject}'


class Student(models.Model):
    full_name = models.CharField(max_length=50)
    group_number = models.ForeignKey(Groups, on_delete=models.CASCADE)
    subject_mark = models.ManyToManyField(Marks, through='StudentMarks')

    @property
    def marks(self):
        return StudentMarks.objects.filter(student=self.pk)

    def __str__(self):
        return f'{self.full_name}'


class StudentMarks(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    marks = models.ForeignKey(Marks, on_delete=models.CASCADE)
    student_marks = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return f'{self.student.full_name} - {self.marks.name_subject}: {self.student_marks}'


class Subjects(models.Model):
    ID_subjects = models.AutoField(auto_created=True, primary_key=True)
    Name = models.CharField(max_length=50)
    Group_number = models.ForeignKey(Groups, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.Name}'


class Curators(models.Model):
    Full_name = models.CharField(max_length=50)
    Group_number = models.CharField(max_length=50, primary_key=True)

    def __str__(self):
        return f'{self.Full_name}, {self.Group_number}'
