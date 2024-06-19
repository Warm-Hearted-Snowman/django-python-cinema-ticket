# cinema/models.py

from django.db import models


class Cinema(models.Model):
    Cinema_ID = models.AutoField(primary_key=True)
    city = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    info = models.TextField(blank=True)
    rating = models.FloatField()
    image = models.ImageField(upload_to='cinemas/', null=True, blank=True)  # Add this line

    def __str__(self):
        return self.title


class Hall(models.Model):
    Schedule_ID = models.AutoField(primary_key=True)
    cinema = models.ForeignKey(Cinema, related_name='halls', on_delete=models.CASCADE)
    movie = models.ForeignKey('movie.Movie', on_delete=models.CASCADE)
    hall_id = models.CharField(max_length=255)
    time = models.DateTimeField()

    def __str__(self):
        return f"{self.cinema.title} - Hall {self.hall_id} - {self.movie.title} ({self.time})"


class Seat(models.Model):
    @classmethod
    def book_seat(cls, seat_id, schedule):
        # Update the status of selected seats to 'Reserved' or 'Booked'
        seats_to_book = cls.objects.filter(schedule=schedule, Seat_ID=seat_id, status='قابل خرید')
        seats_to_book.update(status='Booked')  # You can use 'Booked' here if you prefer

    def seat_recovery(self):
        self.status = 'قابل خرید'
        self.save()

    Seat_ID = models.AutoField(primary_key=True)
    schedule = models.ForeignKey(Hall, on_delete=models.CASCADE)
    row = models.IntegerField()
    column = models.IntegerField()
    status = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Seat {self.row}-{self.column} ({self.status})"
