from django import forms
from .models import *


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = {
            'Full_Name',  #: ['exact'],
        }
