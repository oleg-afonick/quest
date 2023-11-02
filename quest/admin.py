from django.contrib import admin
from .models import *


class MarksInline(admin.TabularInline):
    model = StudentMarks
    extra = 1


class StudentAdmin(admin.ModelAdmin):
    model = Student
    inlines = (MarksInline,)


admin.site.register(Student, StudentAdmin)
admin.site.register(Groups)
admin.site.register(Subjects)
admin.site.register(Curators)
admin.site.register(Marks)

