from django.shortcuts import render
from django.views.generic.base import View
from django.shortcuts import get_object_or_404
from .models import Student

# class StudentListView(View):
#     def get(self, request):
#         students_all = Students.objects.all()
#         return render(request, '')

class StudentView(View):
    def get(self,request, slug):
        student = get_object_or_404(Student, slug=slug)
        return render(request, 'cabinet/student.html',{'student':student})