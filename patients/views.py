from django.shortcuts import render
from rest_framework import generics, permissions
from django.contrib.auth.models import User
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import Patient
from .serializers import PatientSerializer
from healthcare.permissions import IsPatiendOwner
from rest_framework.response import Response
from rest_framework import status


class PatientListCreateView(generics.ListCreateAPIView):
    serializer_class = PatientSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Patient.objects.all()
    
    def perform_create(self, serializer):
        if Patient.objects.filter(created_by=self.request.user).exists():
            return Response({'error': 'You already have a patient profile.'}, status=status.HTTP_400_BAD_REQUEST)
        serializer.save(created_by=self.request.user)

class PatientDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PatientSerializer
    permission_classes = [permissions.IsAuthenticated, IsPatiendOwner]
    queryset = Patient.objects.all()