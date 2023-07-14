from django.urls import path
from .views import homenewsletter_page, homenewsletter_create_page, patient_complete_form, patient_complete_list, patient_detail, doctor_page, department_page, appointment_page, appointment_create_page, patient_basic_form, patient_basic_list 

urlpatterns = [
    path('newsletter/', homenewsletter_page.as_view(), name='apinewsletter'),
    path('create_newsletter/', homenewsletter_create_page.as_view(), name='apicreate_newsletter'),
    path("doctor/", doctor_page.as_view(), name="apidoctor"),
    path("department/", department_page.as_view(), name="apidepartment"),
    path("create_basic_patient/", patient_basic_form.as_view(), name="apicreate_basic_patient"),
    path("basic_patient/", patient_basic_list.as_view(), name="apibasic_patient/"),
    path("patient/", patient_complete_form.as_view(), name="apipatient"),
    path("create_patient/", patient_complete_list.as_view(), name="apicreate_patient"),
    path('<int:pk>/', patient_detail.as_view(), name='apidetail'),
    path("appointment/", appointment_page.as_view(), name="apiappointment"),
    path("create_appointment/", appointment_create_page.as_view(), name="apiappointment")
]
