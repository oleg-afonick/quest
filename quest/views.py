from django.views.generic import *
from .models import *
from .filters import *


class StudentList(ListView):
    model = Student
    ordering = 'Student_ID_number'
    template_name = 'quest/index.html'
    context_object_name = 'students'
    paginate_by = 1

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = StudentFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context