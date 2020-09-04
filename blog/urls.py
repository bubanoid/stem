from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about, name='about'),
    path('<slug:slug>/', views.DetailView.as_view(), name='datail'),
    path('', views.ArticlesView.as_view(), name='blog'),
]
