from rest_framework import serializers
from bookings.models import Appointment, MedicalNote


class AppointmentSerializer(serializers.ModelSerializer):

    doctor = serializers.PrimaryKeyRelatedField(read_only=True)
    patient = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Appointment
        fields = ['appointments_date', 'appointments_date','appointments_time',
                  'notes', 'status', 'patient', 'doctor']


class MedicarNoteSerializer(serializers.ModelSerializer):

    appointment = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = MedicalNote
        fields = ['note', 'date', 'appintment']
