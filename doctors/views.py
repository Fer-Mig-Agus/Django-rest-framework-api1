from .serializers import DoctorSerializer
from .models import Doctor
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView


class ListDoctorsView(ListAPIView, CreateAPIView):
    allowed = ['GET','POST']
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()
    
    
class DetailDoctorsView(RetrieveUpdateDestroyAPIView):
    allowed = ['GET','PUT','DELETE']
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()