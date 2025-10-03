from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'service'

router = DefaultRouter()

router.register('', views.ServiceViewset, basename='service')

urlpatterns = [
    path('', include(router.urls))
]
