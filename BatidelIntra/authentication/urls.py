from django.urls import path

from . import views


app_name = 'authentication'
urlpatterns = [
    path('', views.login_view, name='login'),
    path('authenticate/', views.authenticate_user, name='authenticate'),
]