from django.urls import path
from .views import *

urlpatterns = [
    path('', PatientListCreateView.as_view()),
    path('<int:pk>/', PatientDetailView.as_view()),

]
