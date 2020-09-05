from django.contrib import admin
from .models import Teacher, Alumni, Project, ProjectImage, Specialty

admin.site.register(Teacher)
admin.site.register(Alumni)
admin.site.register(Specialty)
admin.site.register(Project)
admin.site.register(ProjectImage)
