from django.shortcuts import render, redirect
from web.models import Patient, Newsletter, Department, Doctor, User, Appointment
from .serializers import PatientSerializers, NewsletterSerializers, DepartmentSerializers, DoctorSerializers, AppointmentSerializers, UserSerializers
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, CreateAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter
from rest_framework.permissions import AllowAny, IsAuthenticated


#generic class based views


#Patient Basic Registration and List 
class patient_basic_form(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    permission_classes =[AllowAny]

class patient_basic_list(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    pagination_class = PageNumberPagination
    filter_backends = [SearchFilter]
    search_fields = ["username"]
    permission_classes =[IsAuthenticated]


# Patient Complete Registration, Fully Registered and Individual Detail
class patient_complete_form(CreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializers
    permission_classes =[AllowAny]


class patient_complete_list(ListAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializers
    pagination_class = PageNumberPagination
    filter_backends = [SearchFilter]
    search_fields = ["username", "health_status"]
    permission_classes =[IsAuthenticated]


class patient_detail(RetrieveUpdateDestroyAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializers
    lookup_field = "pk"
    permission_classes =[IsAuthenticated]


#Home Newsletters
class homenewsletter_page(ListAPIView):
    queryset = Newsletter.objects.all()
    serializer_class = NewsletterSerializers
    pagination_class = PageNumberPagination
    filter_backends = [SearchFilter]
    search_fields = ["email"]
    permission_classes =[IsAuthenticated]


class homenewsletter_create_page(CreateAPIView):
    queryset = Newsletter.objects.all()
    serializer_class = NewsletterSerializers
    permission_classes =[AllowAny]

    

#Departments
class department_page(ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializers
    permission_classes =[AllowAny]
    
        
#DOctors
class doctor_page(ListCreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializers
    permission_classes =[AllowAny]


#Appointments to be connected to API
class appointment_create_page(CreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializers
    permission_classes =[AllowAny]
    

class appointment_page(ListAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializers
    pagination_class = PageNumberPagination
    filter_backends = [SearchFilter]
    search_fields = ["full_name", "email"]
    permission_classes =[IsAuthenticated]








