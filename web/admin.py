from django.contrib import admin
from .models import Newsletter, Department, Doctor, Patient, Appointment

# Register your models here.

admin.site.register(Newsletter)
admin.site.register(Department)
admin.site.register(Patient)
admin.site.register(Appointment)

class DoctorAdmin(admin.ModelAdmin):
    list_display = ["name", "age", "email", "gender", "department"] # For selecting list of Fields to be displayed 

admin.site.register(Doctor, DoctorAdmin)

# class PatientAdmin(admin.ModelAdmin):
#     list_display = ["email", "age", "gender"] # For selecting list of Fields to be displayed 

# admin.site.register(Patient, PatientAdmin)


