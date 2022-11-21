"""ask URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from ask.views import index
from qa.views import mainPage
from qa.views import ask
from qa.views import popular, signup, loginPage, LogoutPage

urlpatterns = [
    path('', mainPage),
    path('login/', loginPage),
    path('logout/', LogoutPage),
    path('signup/', signup),
    path('question/',include('qa.urls')),
    path('ask/', ask, name = 'ask'),
    path('popular/', popular, name = 'popular')
]
