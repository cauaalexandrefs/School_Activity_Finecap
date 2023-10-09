from django.urls import path
from .views import login_view as login, logout_view, register

urlpatterns = [

    path('', login,name='login'),
    path('logout/', logout_view,name='logout'),
    path('register/', register, name='register')

]