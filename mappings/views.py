
from rest_framework import generics, permissions
from .models import Mapping
from .serializers import *

class MappingCreateView(generics.ListCreateAPIView):
    serializer_class = PatientDoctorSerializer
    permission_classes = [permissions.IsAuthenticated]

class MappingListView(generics.ListAPIView):
    serializer_class = PatientDoctorSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Mapping.objects.all()

class MappingPatientView(generics.ListAPIView):
    serializer_class = PatientDoctorSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Mapping.objects.filter(patient_id=self.kwargs['patient_id'])

class MappingDeleteView(generics.DestroyAPIView):
    queryset = Mapping.objects.all()
    serializer_class = PatientDoctorSerializer
    permission_classes = [permissions.IsAuthenticated]