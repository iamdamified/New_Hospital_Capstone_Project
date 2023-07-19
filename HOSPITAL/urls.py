"""
URL configuration for HOSPITAL project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt import views as jwt_views
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hospital/', include('web.urls')),
    path('api/', include('api.urls')),
    # path('logins/', include('django.contrib.auth.urls')),
    path('auth/', include('djoser.urls')),# endpoints from here handles path to Djoser that makes testing API in DRF easier
    path('auth/', include('djoser.urls.jwt')), #Djoser JWT specific Authentication Testing paths
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'), #JWT only specific Authentication Generating paths - POSTMAN
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'), #JWT only specific Authentication Testing paths - POSTMAN
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),# from this path down is for Swagger documantation download
    path("api/schema/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc",),# Not tried yet
    path("api/schema/swagger-ui/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"), #View and Edit# new

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

