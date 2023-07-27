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



# @api_view(["GET"])
# @permission_classes([IsAuthenticated])

#Patient Basic Registration and List 
#class based view
class user_form(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = UserSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Success": "You are now a Member! proceed to patient registration."}, status=status.HTTP_201_CREATED)
        return Response("Invalid entery")


#generic class based views
class user_list(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    pagination_class = PageNumberPagination
    filter_backends = [SearchFilter]
    search_fields = ["username"]
    permission_classes =[IsAuthenticated]


# Patient Complete Registration, Fully Registered and Individual Detail
#class based view
# class patient_form(APIView):
#     permission_classes = [AllowAny]
#     def post(self, request):
#         serializer = PatientSerializers(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"Success": "Your patient registration was successful!!!"}, status=status.HTTP_201_CREATED)
#         return Response("Invalid entery")
    
class patient_form(CreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializers
    permission_classes =[AllowAny]

#generic class based view
class patient_list(ListAPIView):
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

#Appointments to be connected to API
#class based view
class appointment_create_page(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = AppointmentSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Success": "You have successfully booked an appointment."}, status=status.HTTP_201_CREATED)
        return Response("Invalid entery")
    
#generic class based view
class appointment_page(ListAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializers
    pagination_class = PageNumberPagination
    filter_backends = [SearchFilter]
    search_fields = ["full_name", "email"]
    permission_classes =[IsAuthenticated]



#Home Newsletters

#class based view
class homenewsletter_create_page(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = NewsletterSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Success": "You have successfully enrolled for our periodic newsletters."}, status=status.HTTP_201_CREATED)
        return Response("Invalid entery")
    

class homenewsletter_page(ListAPIView):
    queryset = Newsletter.objects.all()
    serializer_class = NewsletterSerializers
    pagination_class = PageNumberPagination
    filter_backends = [SearchFilter]
    search_fields = ["email"]
    permission_classes =[IsAuthenticated]


    

#Departments
class department_page(ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializers
    permission_classes =[AllowAny]
    
        
#Doctors
class doctor_page(ListCreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializers
    permission_classes =[AllowAny]











