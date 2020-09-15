from django.contrib import admin
from .models import Student, Group, StudentHW, Subject, StudentSchedule

admin.site.register(Student)
admin.site.register(Group)
admin.site.register(Subject)


@admin.register(StudentHW)
class AdminStudentHW(admin.ModelAdmin):
    list_display = ('subject','student','done_task', 'mark', 'passed', 'name')

@admin.register(StudentSchedule)
class AdminStudentSchedule(admin.ModelAdmin):
    list_display = ('subject','group','week_day', 'date', 'teacher')