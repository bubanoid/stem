from django.shortcuts import render
from django.views.generic.base import View
from django.shortcuts import get_object_or_404
from .models import Student, StudentSchedule, StudentHW

# class StudentListView(View):
#     def get(self, request):
#         students_all = Students.objects.all()
#         return render(request, '')

class StudentView(View):
    def get(self,request, slug):
        student = get_object_or_404(Student, slug=slug)

        student_schedule = StudentSchedule.objects.all()
        student_schedule = student_schedule.filter(group__name = student.group).order_by('date').order_by('week_day')

        student_hw = StudentHW.objects.filter(student__name = student.name).order_by('-pub_date').order_by('subject')
        context = {
            'student':student,
            'student_schedule':student_schedule,
            'student_hw':student_hw,
        }
        return render(request, 'cabinet/student.html',context)