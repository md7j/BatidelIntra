from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from . import views

app_name = 'SAV'
router = routers.DefaultRouter()
router.register(r'SAV', views.SAVViewSet)
router.register(r'customers', views.CustomerViewSet)


urlpatterns = [
    url('^api/', include(router.urls)),
    url('^$', views.index, name='SAV')
]

