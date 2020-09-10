from django.urls import path
from . import views

urlpatterns = [
    path('teachers/', views.TeachersView.as_view(), name='teachers'),
    path('teacher/<slug:slug>/', views.TeacherDatailView.as_view(), name='teacher_datail'),
    path('alumni/', views.AlumnisView.as_view(), name='alumnis'),
    path('alumni/<slug:slug>/', views.AlumniDetailView.as_view(), name='alumni_detail')
]
