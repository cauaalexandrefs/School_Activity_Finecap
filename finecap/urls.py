from django.urls import path
from .views import index, remove_reserva, detail, create_reserva
urlpatterns = [
    path('index/', index, name='index'),
    path('remove/<int:id>', remove_reserva, name='remove_reserva'),
    path('detalhar/<int:id>', detail, name='detalhar'),
    path('create/', create_reserva, name='create_reserva'),
]