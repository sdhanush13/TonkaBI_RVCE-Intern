from django.urls import path
from . import views as core_views
from . import views
from django.conf.urls import url
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.addInsuranceView, name='home'),
]