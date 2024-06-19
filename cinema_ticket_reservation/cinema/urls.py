from django.urls import path
from .views import cinemas_list, cinema_detail

app_name = 'cinema'

urlpatterns = [
    path('', cinemas_list, name='cinemas_list'),
    path('detail/<int:cinema_id>/', cinema_detail, name='cinema_detail'),
]
