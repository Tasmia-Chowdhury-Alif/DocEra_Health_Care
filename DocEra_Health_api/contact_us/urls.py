from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'contact_us'

router = DefaultRouter()

router.register('', views.ContactUsViewset, basename='contact')

urlpatterns = [
    path('', include(router.urls)),
]
