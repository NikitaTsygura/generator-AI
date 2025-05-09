"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('knitting/', TemplateView.as_view(template_name="knitting_page.html"), name='knitting'),
    path('3D_prints/', TemplateView.as_view(template_name="3D_prints_page.html"), name='3D_prints'),
    path('main/', TemplateView.as_view(template_name="front_page.html"), name='main'),
    path('arduino/', TemplateView.as_view(template_name="arduino_page.html"), name='arduino'),

]
