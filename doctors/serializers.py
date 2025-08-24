from rest_framework import serializers
from doctors.models import Doctor, Department, DoctorAvailable, MedicalNote


class DoctorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Doctor
        fields = ['first_name', 'last_name', 'qualification',
                  'contact_number', 'email', 'address', 'biography']
    
    def validate_email(self, value):
        if "@example.com" in value:
            return value
        
        raise serializers.ValidationError('El correo debe de incluir @example.com')

    def validate(self, attrs):
        if len(attrs['contact_number']) < 10 and attrs['is_on_vacation']==True:
            raise serializers.ValidationError('Por favor ingresa un numero valido antes de irte de vacaciones')
        return super().validate(attrs)


class DeparmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Department
        fields = ['name', 'description']


class DoctorAvailableSerializer(serializers.ModelSerializer):

    doctor = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = DoctorAvailable
        fields = ['start_date', 'start_time', 'doctor']


class MedicalNoteSerializer(serializers.ModelSerializer):

    doctor = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = MedicalNote
        fields = ['note', 'date', 'doctor']
