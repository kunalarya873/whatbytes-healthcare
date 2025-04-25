from django.urls import path
from .views import *

urlpatterns = [
    path('', MappingCreateView.as_view()),
    path('<int:patient_id>/', MappingPatientView.as_view()),
    path('<int:pk>/', MappingDeleteView.as_view()),
]
