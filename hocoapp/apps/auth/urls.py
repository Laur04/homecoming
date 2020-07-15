from django.urls import path
from django.contrib.auth.views import LogoutView

from . import views

app_name = "auth"

urlpatterns = [
    path("login/", views.login, name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
]
