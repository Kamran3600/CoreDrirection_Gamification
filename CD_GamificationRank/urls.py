from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core_direction.urls')),
    path('django-rq/', include('django_rq.urls')),
]
