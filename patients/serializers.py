from rest_framework import serializers
from patients.models import Patient, Insurance, MedicalRecord
from bookings.serializers import AppointmentSerializer

from datetime import date

class InsuranceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Insurance
        fields = ['provider', 'policy_number', 'expiration_date']


class MedicalRecordSerializer(serializers.ModelSerializer):
    doctor = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = MedicalRecord
        fields = ['note', 'date', 'doctor']


class PatientSerializer(serializers.ModelSerializer):
    
    appointments = AppointmentSerializer(many=True, read_only=True)

    insurances = InsuranceSerializer(many=True, read_only=True)
    medical_records = MedicalRecordSerializer(many=True, read_only=True)
    
    age = serializers.SerializerMethodField()

    class Meta:
        model = Patient
        # No es bueno colocar __all__ en su lugar se deben definir
        # #que campos quieres que se envien
        #fields = '__all__'
        
        fields = [
            'id',
            'first_name',
            'last_name',
            'age',
            'date_of_birth',
            'contact_number',
            'email',
            'address',
            'medical_history',
            'medical_records',
            'appointments',
            'insurances'
        ]

    def get_age(self, obj):
        days= (date.today() - obj.date_of_birth).days
        return days // 365