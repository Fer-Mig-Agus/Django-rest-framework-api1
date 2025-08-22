from rest_framework import serializers
from patients.models import Patient, Insurance, MedicalRecord


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

    insurances = InsuranceSerializer(many=True, read_only=True)
    medical_records = MedicalRecordSerializer(many=True, read_only=True)

    class Meta:
        model = Patient
        # No es bueno colocar __all__ en su lugar se deben definir
        # #que campos quieres que se envien
        fields = '__all__'
