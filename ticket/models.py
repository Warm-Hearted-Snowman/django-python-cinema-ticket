from django.db import models

from account.models import Profile
from cinema.models import Seat, Hall
from django.db.models.signals import pre_delete
from django.dispatch import receiver


class Ticket(models.Model):
    Ticket_ID = models.AutoField(primary_key=True)
    seats = models.ManyToManyField(Seat)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    schedule_id = models.ForeignKey(Hall, on_delete=models.CASCADE)
    time_on_reserve = models.DateTimeField(auto_now_add=True)
    is_canceled = models.BooleanField(default=False)

    def __str__(self):
        seat_numbers = ', '.join([f"{seat.row}-{seat.column}" for seat in self.seats.all()])
        return f"Ticket {self.Ticket_ID} - Seats {seat_numbers} - {self.schedule_id.cinema.title} - {self.schedule_id.movie.title}"

    def cancel(self):
        if not self.is_canceled:
            for seat in self.seats.all():
                seat.seat_recovery()
            self.is_canceled = True
            self.save()


@receiver(pre_delete, sender=Ticket)
def cancel_ticket_on_delete(sender, instance, **kwargs):
    """
    This signal handler marks the ticket as canceled before it's deleted.
    """
    if not instance.is_canceled:
        instance.is_canceled = True
        instance.save()
