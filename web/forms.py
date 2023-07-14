from django import forms
from django.contrib.auth.models import User
from .models import Patient, Appointment
from django.contrib.auth.forms import UserCreationForm


# class UserForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password', 'first_name', 'last_name']

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name']


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ["user", "job", "phone", "age", "gender", "status", "height", "health_status", "address", "image"]



class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = "__all__"