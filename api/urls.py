from django.urls import path
from .views import homenewsletter_page, homenewsletter_create_page, user_form, user_list, patient_detail, doctor_page, department_page, appointment_page, appointment_create_page, patient_form, patient_list 

urlpatterns = [
    path('newsletter/', homenewsletter_page.as_view(), name='apinewsletter'),
    path('create_newsletter/', homenewsletter_create_page.as_view(), name='apicreate_newsletter'),
    path("doctor/", doctor_page.as_view(), name="apidoctor"),
    path("department/", department_page.as_view(), name="apidepartment"),
    path("user_form/", user_form.as_view(), name="user_form"),
    path("user_list/", user_list.as_view(), name="user_list"),
    path("patient_form/", patient_form.as_view(), name="patient_form"),
    path("patient_list/", patient_list.as_view(), name="patient_list"),
    path('<int:pk>/', patient_detail.as_view(), name='apidetail'),
    path("appointment/", appointment_page.as_view(), name="apiappointment"),
    path("create_appointment/", appointment_create_page.as_view(), name="apiappointment")
]
