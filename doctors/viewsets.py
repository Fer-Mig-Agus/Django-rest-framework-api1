from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import DoctorSerializer
from .models import Doctor
from .permissions import IsDoctor

class DoctorViewSet(viewsets.ModelViewSet):
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()
    
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    #Esto no es recomendable porque cambiamos el estado pero podriamos perder el valor
    #Para ello se va a realizar dos funciones, una para cada accion
    
    # @action(['POST'], detail=True)
    # def toggle_vacation(self, requests, pk):
        
    #     doctor = self.get_object()
    #     if doctor.is_on_vacation:
    #         doctor.is_on_vacation = False
    #     else:
    #         doctor.is_on_vacation = True
    #     doctor.save()
        
    #     return Response('Doctor was update')
    
    @action(["POST"], detail=True, url_path='set-on-vacation')
    def set_on_vacation(self, requests, pk):
        
        doctor = self.get_object()
        doctor.is_on_vacation = True
        doctor.save()
        
        return Response({"status":"El doctor esta en vacaciones"})
    
    @action(['POST'], detail=True, url_path='set-off-vacation')
    def set_off_vacation(self, requests, pk):
        
        doctor = self.get_object()
        doctor.is_on_vacation = False
        doctor.save()
        
        return Response({"status":"El doctor no esta en vacaciones"})
    
    
            