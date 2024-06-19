from django.contrib import admin
from .models import Cinema, Hall, Seat


@admin.register(Cinema)
class CinemaAdmin(admin.ModelAdmin):
    list_display = ('Cinema_ID', 'title', 'city', 'address', 'info')


@admin.register(Hall)
class HallAdmin(admin.ModelAdmin):
    list_display = ('Schedule_ID', 'cinema', 'movie', 'hall_id', 'time')
    list_filter = ('cinema', 'movie', 'time')


@admin.register(Seat)
class SeatAdmin(admin.ModelAdmin):
    list_display = ('Seat_ID', 'schedule', 'row', 'column', 'status', 'price')
    list_filter = ('schedule', 'status')
