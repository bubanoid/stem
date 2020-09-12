from django.urls import path
from . import views

urlpatterns = [
    path('<slug:slug>/', views.EventDatailView.as_view(), name = 'events_detail'),
    path('', views.EventView.as_view(), name='events')
]