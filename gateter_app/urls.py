from django.urls import path, include
from .views import dashboard, profile_list, profile, register

app_name = "gateter_app"

urlpatterns = [
    path("accounts/", include("django.contrib.auth.urls")),
    path("register/", register, name="register"),
    path("", dashboard, name="dashboard"),
    path("profile_list/", profile_list, name="profile_list"),
    path("profile/<int:pk>", profile, name="profile"),
]
