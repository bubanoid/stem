from django.contrib import admin
from .models import Student, Group, StudentHW, Subject

admin.site.register(StudentHW)
admin.site.register(Student)
admin.site.register(Group)
admin.site.register(Subject)