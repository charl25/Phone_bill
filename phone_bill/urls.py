"""phone_bill URL Configuration

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
from django.urls import path
from calculate_bill import views as cb_views
from text_input_bill import views as tib_views
from radio_button_bill import views as rbb_views
from bill_with_settings import views as bws_views

urlpatterns = [
    path('', cb_views.index, name='index'),
    path('admin/', admin.site.urls),
    path('calculate_bill/', cb_views.form_name_view, name='calculate_bill'),
    path('text_input_bill/', tib_views.form_name_view, name='text_input_bill'),
    path('radio_button_bill/', rbb_views.form_name_view, name='radio_button_bill'),
    path('bill_with_settings/', bws_views.form_name_view, name='bill_with_settings'),
]
