from django.contrib import admin
from .models import Ticket


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('Ticket_ID', 'display_seats', 'user', 'schedule_id', 'time_on_reserve', 'is_canceled')
    list_filter = ('schedule_id__cinema', 'schedule_id__movie', 'time_on_reserve', 'is_canceled')
    search_fields = ('seat__row', 'seat__column', 'customer_profile__user__username', 'schedule_id__cinema__title',
                     'schedule_id__movie__title')

    def display_seats(self, obj):
        return ", ".join([f"{seat.row}-{seat.column}" for seat in obj.seats.all()])

    display_seats.short_description = 'Seats'
