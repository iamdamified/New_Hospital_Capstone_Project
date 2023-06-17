from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', HomePage , name='home'),
    path('departments', DepartmentsPage , name='departments'),
    path('doctors', DoctorsPage , name='doctors'),
    path('register', RegisterPage , name='register'),
    path('patients', PatientsPage, name='patients'),
    # path("login/", LoginView.as_view(template_name="Main/login.html"), name="login"),  #NOTE LoginView is a class in django and to use it as a page function we must add "as_view"
    # path("logout/", LogoutView.as_view(template_name="Main/logout.html"), name="logout"),
]