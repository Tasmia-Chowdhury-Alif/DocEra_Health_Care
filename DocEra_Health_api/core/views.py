from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.reverse import reverse
from drf_spectacular.utils import extend_schema

class ApiRootView(APIView):
    @extend_schema(exclude=True)  # Excludes from schema
    def get(self, request, format=None):
        return Response({
            'appointment': reverse('appointment:appointment-list', request=request, format=format),
            'contact_us': reverse('contact_us:contact-list', request=request, format=format),
            'doctor': reverse('doctor:doctor-list', request=request, format=format),
            'patient': reverse('patient:patient-list', request=request, format=format),
            'service': reverse('service:service-list', request=request, format=format),
        })