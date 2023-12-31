from rest_framework import serializers
from web.models import *

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = ["id", "name", "price", "description", "category", "image"]
        fields = ["id", "username", "first_name", "last_name", "email", "password"]

class PatientSerializers(serializers.ModelSerializer):
    class Meta:
        model = Patient
        
        fields = ["id", "user", "job", "phone", "age", "gender", "status", "height", "health_status", "address", "image", "testimonials"]


class DoctorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = "__all__"


class DepartmentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = "__all__"


class AppointmentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = "__all__"

class NewsletterSerializers(serializers.ModelSerializer):
    class Meta:
        model = Newsletter
        fields = ["email"]


