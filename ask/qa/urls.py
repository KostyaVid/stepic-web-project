from django.contrib import admin
from django.urls import path
from qa.views import test

urlpatterns = [
    path('<int:id>/', test, name='qa')
]
