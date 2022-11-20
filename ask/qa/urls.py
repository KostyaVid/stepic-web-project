from django.contrib import admin
from django.urls import path
from qa.views import question


urlpatterns = [
    path('<int:id>/', question, name = "question")
]
