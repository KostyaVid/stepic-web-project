from django.contrib import admin
from django.urls import path
from qa.views import question
from qa.views import createQuestion

urlpatterns = [
    path('new/', createQuestion, name='create-question'),
    path('<int:id>/', question, name='question')
]
