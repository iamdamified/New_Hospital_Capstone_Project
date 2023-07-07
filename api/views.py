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




# class api_patient_list_page(ListAPIView):
#     queryset = Patient.objects.all()
#     serializer_class = PatientSerializers
#     pagination_class = PageNumberPagination
#     filter_backends = [SearchFilter]
#     search_fields = ["age", "status", "gender", "username", "job", "health_status"]
#     permission_classes =[IsAuthenticated]


# class api_patient_create_page(CreateAPIView):
#     queryset = Patient.objects.all()
#     serializer_class = PatientSerializers
#     pagination_class = PageNumberPagination
#     filter_backends = [SearchFilter]
#     search_fields = ["age", "status", "gender", "username", "job", "health_status"]
#     permission_classes =[IsAuthenticated]


class api_patient_page(ListCreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializers
    pagination_class = PageNumberPagination
    filter_backends = [SearchFilter]
    search_fields = ["username", "health_status"]
    permission_classes =[IsAuthenticated]


class api_patient_detail(RetrieveUpdateDestroyAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializers
    lookup_field = "pk"
    permission_classes =[IsAuthenticated]



class api_home_page(ListCreateAPIView):
    queryset = Newsletter.objects.all()
    serializer_class = NewsletterSerializers
    


class api_department_page(ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializers
        

class api_doctor_page(ListCreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializers


# to be connected to API
class api_appointment_page(ListCreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializers
    pagination_class = PageNumberPagination
    filter_backends = [SearchFilter]
    search_fields = ["full_name", "email"]
    








