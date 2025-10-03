from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'doctor'

router = DefaultRouter()

router.register('', views.DoctorViewset, basename='doctor')
router.register('designations', views.DesignationViewset, basename='designation')
router.register('specializations', views.SpecializationViewset, basename='specialization')
router.register('available-times', views.AvailableTimeViewset, basename='available_time')
router.register('reviews', views.ReviewViewset, basename='review')


urlpatterns = [
    path('', include(router.urls)),
]
