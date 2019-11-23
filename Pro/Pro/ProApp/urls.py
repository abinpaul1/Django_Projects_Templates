from django.urls import path
from ProApp import views

urlpatterns = [
    path('',views.disp_form,name="user")
]
