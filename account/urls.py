from django.contrib import admin
from django.urls import path
from account.views import *

urlpatterns = [
    path('register/',Registerview.as_view()),
    path('login/',LoginView.as_view())
]