from django.contrib import admin
from django.urls import path
from login import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login, name="login"),
    path('otp_verify/', views.otp_verify, name="otp_verify"),
    path('home/', views.home, name="home"),
]
