from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Newsletter(models.Model):
    email = models.EmailField()


    def __str__(self):
        return self.email
    

SERVICE_CHOICES = (
    ("CARDIOLOGY", "CARDIOLOGY"),
    ("DIAGNOSIS", "DIAGNOSIS"),
    ("SURGERY", "SURGERY"),
    ("FIRST AID", "FIRST AID"),
    ("INTENSIVE CARE", "INTENSIVE CARE"),
    ("GYNAECOLOGY", "GYNAECOLOGY"),
    ("NURSING", "NURSING"),
    ("PHARMACY", "PHARMACY"),
    ("DIALYSIS", "DIALYSIS"),
    ("ORTHOPAEDICS", "ORTHOPAEDICS")
)



class Department(models.Model):
    service = models.CharField(choices=SERVICE_CHOICES, max_length=25)
    image = models.ImageField(upload_to='service_image')
    description = models.TextField()

    def __str__(self):
        return self.service
    

GENDER_CHOICES = (
    ("M", "Male"),
    ("F", "Female")
)

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10)
    address = models.CharField(max_length=100)
    image = models.ImageField(upload_to='doctor_image')
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    position = models.CharField(max_length=50)
    about = models.TextField()
    date_joined = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.name
    



HEALTH_CHOICES = (
    ("S", "Sick"),
    ("R", "Recovering"),
    ("H", "Healthy")
)

GENDER_CHOICES = (
    ("M", "Male"),
    ("F", "Female")
)

STATUS_CHOICES = (
    ("M", "Married"),
    ("S", "Single")
)



# # INBUILT USER EXTENSION MODEL FOR COLLECTIMG NEW USERS
class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # This line link registers a user
    job = models.CharField(max_length=20, blank=True)
    phone = models.BigIntegerField(null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=15, blank=True)
    status = models.CharField(choices=STATUS_CHOICES, max_length=15, blank=True)
    sickness_type = models.CharField(max_length=20, blank=True)
    sickness_description = models.TextField(blank=True)
    health_status = models.CharField(choices=HEALTH_CHOICES, max_length=15, blank=True)
    height = models.CharField(max_length=10, blank=True)
    image = models.ImageField(upload_to='patient_image', blank=True)
    address = models.CharField(max_length=100, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return str(self.user) #f"{self.user} patience"
    

@receiver(post_save, sender=User)
def create_user_patient(sender, instance, created, **kwargs):
    if created:
        Patient.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_patient(sender, instance, **kwargs):
    instance.patient.save()


# # connecting API
# class Appointment(models.Model):
#     name = models.CharField(max_length=100)
#     phone = models.BigIntegerField()
#     email = models.EmailField()
#     department = models.ForeignKey(Department, on_delete=models.CASCADE)
#     doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
#     purpose = models.TextField()
#     date_requested = models.DateField(auto_now_add=True)
    


#     def __str__(self):
#         return self.name