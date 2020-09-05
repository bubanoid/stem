from django.urls import path
from . import views

urlpatterns = [
    path('teachers/', views.TeachersView.as_view(), name='teachers'),
    path('teacher/<slug:slug>/', views.TeacherDatailView.as_view(), name='datail'),
    # path('alumni/')
]
