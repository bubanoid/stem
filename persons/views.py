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

class AlumnisView(View):
    def get(self, request):
        alumni_list = Alumni.objects.all()
        context = {'alumni_list':alumni_list}
        return render(request, 'persons/alumni_list.html', context)

class AlumniDetailView(View):
    def get(self, request, slug):
        alumni = get_object_or_404(Alumni, slug=slug)
        return render(request,'persons/alumni.html', {'alumni':alumni} )