from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('dashboard.urls')),
    path('authentication/', include('authentication.urls')),
    path('planning/', include('planning.urls')),
    path('customers/', include('customers.urls')),
    path('SAV/', include('SAV.urls')),
    path('admin/', admin.site.urls),
]