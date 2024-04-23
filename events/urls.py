from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('events/add/', views.add_event, name='add_event'),
    path('events/<str:title>/', views.event_detail, name='event_detail'),
]
