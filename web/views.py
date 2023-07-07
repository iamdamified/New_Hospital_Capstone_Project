from django.shortcuts import render, redirect
# from django.contrib import auth
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Newsletter, Department, Doctor, User, Patient, Appointment
from django.http import HttpResponse
from .forms import UserForm, PatientForm, AppointmentForm


# Create your views here.

# def login_user(request):
#     return render(request, "web/login.html")

def web_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")
        
        else:
            return redirect("login")
    return render(request, "web/login.html")
    

def web_logout(request):
    logout(request)
    return redirect("home")





def HomePage(request):
    if request.method == "POST":
        new_subscriber = request.POST.get("email")# request.POST("email") # OR request.POST.get["email"] OR request.POST.get("name")
        Newsletter.objects.create(email=new_subscriber)
        return HttpResponse("You have subscribed sucessfully")
    else:
        doctors = Doctor.objects.all()
        patients = Patient.objects.all()
        context = {
        'doctors': doctors,
        'patients': patients
    }

    
    return render(request, "web/index.html", context)



def DepartmentsPage(request):
    departments = Department.objects.all()# request.POST("email") # OR request.POST.get["email"] OR request.POST.get("name")
    context = {
        'departments': departments
    }
    return render(request, "web/service.html", context)



def DoctorsPage(request):
    doctors = Doctor.objects.all()# request.POST("email") # OR request.POST.get["email"] OR request.POST.get("name")
    context = {
        'doctors': doctors
    }
    return render(request, "web/team.html", context)


def RegisterPage(request):
    if  request.method == "POST": #CVS
        form = UserForm(request.POST, instance=request.user)#collect
        patient_form = PatientForm(request.POST, instance=request.user.patient)#collect
        if form.is_valid() and patient_form.is_valid():#validate
            form.save()#save
            patient_form.save()#save
            return HttpResponse("You have been created successfully")

    else: 
        form = UserForm()
        patient_form = PatientForm()

    context = {
        "form": form,
        "patient_form": patient_form
    }


    return render(request, "web/register.html", context)




def PatientsPage(request):
    patients = Patient.objects.all()# just to make the querry more effective.

    context = {
        'patients': patients
    }
    return render(request, "web/patients.html", context)


def DetailPatientPage(request, pk):
    user = User.objects.get(pk=pk)
    context = {
        'user': user
    }
    return render(request, "web/detail.html", context)



def AppointmentPage(request):
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("You have booked an appointment sucessfully")#redirect will be best to a url which holds the Appointment API connected data
            
    else:
        form = AppointmentForm()

    context = {
        "form": form
    }
    
    return render(request, "web/appointment.html", context)

