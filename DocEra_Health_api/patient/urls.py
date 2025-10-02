from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'patient'

router = DefaultRouter()

router.register('', views.PatientViewset, basename='patient')

urlpatterns = [
    path('', include(router.urls)),
]
