from django.urls import path

from . import views

app_name = "usersapp"

urlpatterns = [
    path('register/', views.register, name="register")
]