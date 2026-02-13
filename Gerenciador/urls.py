from django.contrib import admin
from django.urls import path, include
from . import views # Importando os endpoints e as condições de requests: GET, POST, PUT, DELETE...

urlpatterns = [
    path('', views.index, name="index")
]
