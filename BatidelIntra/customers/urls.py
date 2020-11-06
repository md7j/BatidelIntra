from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from . import views

app_name = 'customers'
router = routers.DefaultRouter()
router.register(r'customers', views.CustomerViewSet)


urlpatterns = [
    url('^api/', include(router.urls)),
    url('^$', views.index, name='customers')
]


#app_name = 'customers'
#urlpatterns = [
#    path('', views.customers, name='customers'),
 #   url(r'^my/datatable/data/$', views.customersJson.as_view(), name='customersJson'),
#    path('data/', views.customersJson, name='customersJson'),
#]