from django.urls import path
from basic_app import views


app_name = 'basic_app'

urlpatterns = [
    path('user_login/',views.user_login, name='user_login'),
    path('register/',views.reg,name = "reg"),
    path('special/',views.special,name='special')
]
