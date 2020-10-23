from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'customers'
urlpatterns = [
    path('', views.customers, name='customers'),
 #   url(r'^my/datatable/data/$', views.customersJson.as_view(), name='customersJson'),
    path('data/', views.customersJson, name='customersJson'),
]