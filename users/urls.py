from django.urls import path

from users import views

app_name = 'users'

urlpatterns = [
    path('login/', views.loginuser, name='loginuser'),
    path('registration/', views.registration, name='registration'),
    path('logout/', views.logoutuser, name='logoutuser'),
]
