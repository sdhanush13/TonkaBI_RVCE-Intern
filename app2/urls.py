from django.contrib import admin 
from django.urls import path
from . import views as core_views
from . import views 
from django.conf.urls import url
# importing views from views..py 
from . views import viewData
  
urlpatterns = [ 
    path('',views.viewData,name="viewData"),
] 