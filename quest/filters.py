from django_filters import FilterSet, ModelChoiceFilter
from .models import *


class StudentFilter(FilterSet):
    Student = ModelChoiceFilter(
        field_name='Full_name',
        queryset=Student.objects.all(),
        label='ФИО студента',
        empty_label=None
    )