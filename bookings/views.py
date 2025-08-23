from .serializers import AppointmentSerializer, MedicarNoteSerializer
from .models import Appointment, MedicalNote
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView


class ListAppointmentsView(ListAPIView, CreateAPIView):
    allowed = ['GET','POST']
    serializer_class = AppointmentSerializer
    queryset = Appointment.objects.all()
    
class DetailsAppointmentsView(RetrieveUpdateDestroyAPIView):
    allowed = ['GET','PUT','DELETE']
    serializer_class = AppointmentSerializer
    queryset = Appointment.objects.all()
    
    
    

class ListMedicalNotesView(ListAPIView, CreateAPIView):
    allowed = ['GET','POST']
    serializer_class = MedicarNoteSerializer
    queryset = MedicalNote.objects.all()
    
    
class DetailMedicalViewsView(RetrieveUpdateDestroyAPIView):
    allowed = ['GET','PUT','DELETE']
    serializer_class = MedicarNoteSerializer
    queryset = MedicalNote.objects.all()