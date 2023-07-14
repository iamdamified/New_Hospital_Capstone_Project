from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', HomePage , name='home'),
    path('departments/', DepartmentsPage , name='departments'),
    path('doctors/', DoctorsPage , name='doctors'),
    path('register/', RegisterPage , name='register'),
    path('patient_register/', PatientRegisterPage , name='patient_register'),
    path('patients/', PatientsPage, name='patients'),
    path('<int:pk>/', DetailPatientPage, name='detail'),
    path('appointments/', AppointmentPage, name='appointments'),
    # path("login/", LoginView.as_view(template_name="web/login.html"), name="login"),  #NOTE LoginView is a class in django and to use it as a page function we must add "as_view"
    path('login/', web_login, name='login'),
    path('logout/', web_logout, name='logout'),
    # path("logout/", LogoutView.as_view(template_name="Main/logout.html"), name="logout"),
]