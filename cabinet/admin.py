from django.contrib import admin
from .models import StudentInfo, Group, StudentHW, Subject

admin.site.register(StudentHW)
admin.site.register(StudentInfo)
admin.site.register(Group)
admin.site.register(Subject)