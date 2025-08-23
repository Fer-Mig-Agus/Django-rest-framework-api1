from .serializers import PatientSerializer
from .models import Patient
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.decorators import api_view
from rest_framework import status

# GET /api/patients => Listar
# POST /api/patients => Crear
# GET /api/patients/<pk>/ => Detalle
# PUT /api/patients/<pk>/ => Modificacion
# DELETE /api/patients/<pk>/ => Eliminar

# @api_view(['GET', 'POST'])
# def list_patients(request):
#     if request.method == 'GET':
#         patients = Patient.objects.all()
#         serializer = PatientSerializer(patients, many=True)
#         return Response(serializer.data)

#     if request.method == 'POST':
#         serializer = PatientSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(status=status.HTTP_201_CREATED)


class ListPatientsView(ListAPIView, CreateAPIView):
    allowed_methods = ['GET','POST']
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()
    
    # def get(self, request):
    #     patients = Patient.objects.all()
    #     serializer = PatientSerializer(patients, many=True)
    #     return Response(serializer.data)

    # def post(self, request):
    #     serializer = PatientSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(status=status.HTTP_201_CREATED)

# @api_view(['POST'])
# def create_patient(request):

#     serializer = PatientSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
        
#         return Response(serializer.data, status=status.HTTP_201_CREATED)

#     return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class DetailPatientsView(RetrieveUpdateDestroyAPIView):
    allowed_methods = ['GET', 'PUT', 'DELETE']
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()


# @api_view(['GET', 'PUT', 'DELETE'])
# def detail_patient(request, pk):

#     try:
#         patient = Patient.objects.get(id=pk)
#     except Patient.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
    
#     if request.method == 'GET':
#         serializer = PatientSerializer(patient)
#         return Response(serializer.data)

#     if request.method == 'PUT':
#         serializer = PatientSerializer(patient, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     if request.method == 'DELETE':
#         patient.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# class DetailPatientView(APIView):
#     allowed_methods = ['GET', 'PUT', 'DELETE']
    
#     def get(self, request):
#         serializer = PatientSerializer(patient)
#         return Response(serializer.data)
    
#     def put(self, request):
#         serializer = PatientSerializer(patient, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_200_OK)
     
#     def delete(self,request):
#         patient.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
