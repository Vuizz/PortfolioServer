from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('projects/', views.get_projects, name='get_projects'),
    path('work/', views.get_work, name='get_work'),
]
