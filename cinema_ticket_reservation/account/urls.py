from django.urls import path, reverse_lazy, include
from .views import register, edit, dashboard, user_login, log_out, dashboard_info, dashboard_tickets

app_name = 'account'

urlpatterns = [
    path('login/', user_login, name='login'),
    path('logout/', log_out, name='login'),
    path('', include('django.contrib.auth.urls')),
    path('register/', register, name='register'),
    path('', dashboard, name='dashboard'),
    path('user-info/', dashboard_info, name='userinfo'),
    path('user-tickets/', dashboard_tickets, name='user-tickets'),
    path('edit/', edit, name='edit')
]
