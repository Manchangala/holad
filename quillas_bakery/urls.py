# quillas_bakery/urls.py
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('gestion/', include('gestion.urls')),
]


