from rest_framework.exceptions import ValidationError
from rest_framework import generics, permissions
from django.contrib.auth.models import User
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import Doctor
from .serializers import *
from healthcare.permissions import IsOwner
from rest_framework.response import Response
from rest_framework import status

class DoctorListCreateView(generics.ListCreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        if Doctor.objects.filter(user=self.request.user).exists():
            return Response({'error': 'You already have a doctor profile.'}, status=status.HTTP_400_BAD_REQUEST)
        serializer.save(user=self.request.user)

        return Response({'message': 'Doctor profile created successfully', 'doctor': Doctor.objects.get(user=self.request.user).user.pk}, status=status.HTTP_201_CREATED)

class DoctorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [permissions.IsAuthenticated]
