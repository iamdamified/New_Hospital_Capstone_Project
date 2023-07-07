from django.urls import path
from .views import api_home_page, api_patient_page, api_patient_detail, api_doctor_page, api_department_page, api_appointment_page

urlpatterns = [
    path('newsletter/', api_home_page.as_view(), name='apihome'),
    path("doctor/", api_doctor_page.as_view(), name="apidoctor"),
    path("department/", api_department_page.as_view(), name="apidepartment"),
    path("patient/", api_patient_page.as_view(), name="apipatient"),
    # path("list_patient/", api_patient_list_page.as_view(), name="list_patient"),
    # path("create_patient/", api_patient_create_page.as_view(), name="create_patient"),
    path('<int:pk>/', api_patient_detail.as_view(), name='apidetail'),
    path("appointment/", api_appointment_page.as_view(), name="apiappointment")
]
