# urls.py
from django.urls import path
from .views import reserve_ticket, reservation_success, cancel_ticket

app_name = 'ticket'

urlpatterns = [
    path('choose-seat/<int:schedule_id>/', reserve_ticket, name='reserve_ticket'),
    path('detail/<int:ticket_id>/', reservation_success, name='detail'),
    path('cancel/', cancel_ticket, name='cancellation'),
]
