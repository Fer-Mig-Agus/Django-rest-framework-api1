from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import DoctorSerializer
from .models import Doctor

class DoctorViewSet(viewsets.ModelViewSet):
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()
    
    @action(['POST'], detail=True)
    def toggle_vacation(self, requests, pk):
        
        doctor = self.get_object()
        if doctor.is_on_vacation:
            doctor.is_on_vacation = False
        else:
            doctor.is_on_vacation = True
        doctor.save()
        
        return Response('Doctor was update')
            