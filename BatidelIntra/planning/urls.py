from django.urls import path
from . import views

app_name = 'planning'
urlpatterns = [
    path('', views.planning, name='planning'),
    path('coords/', views.coords, name='coords'),
]