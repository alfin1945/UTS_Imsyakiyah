from django.contrib import admin
from django.urls import path, include
from UtsApp.views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('Jadwal/', jadwalViews)


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
