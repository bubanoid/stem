from django.shortcuts import render, get_object_or_404
from django.views.generic.base import View
from .models import  Alumni, Teacher, Project, Specialty, ProjectImage

class TeachersView(View):
    def get(self, request):
        teacher_list = Teacher.objects.all()
        context = {'teacher_list':teacher_list}
        return render(request,'persons/teachers_list.html', context)


class TeacherDatailView(View):
    def get(self, request, slug):
        teacher = get_object_or_404(Teacher, slug = slug)
        return render(request, 'persons/teacher.html', {'teacher':teacher})