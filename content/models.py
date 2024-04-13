from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone

class Movie(models.Model):
    title = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    release_date = models.DateField()
    duration = models.PositiveIntegerField()  # Duration in minutes
    synopsis = models.TextField()

    def __str__(self):
        return self.title
    

class Theater(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    capacity = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Showtime(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    theater = models.ForeignKey(Theater, on_delete=models.CASCADE)
    date_and_time = models.DateTimeField()
    available_seats = models.PositiveIntegerField()

    def clean(self):
        if self.date_and_time <= timezone.now():
            raise ValidationError("Showtime date and time must be in the future.")

    def __str__(self):
        return f"{self.movie.title} - {self.theater.name} - {self.date_and_time}"
    


class Reserve(models.Model):
    name = models.CharField(max_length=225)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    theater = models.ForeignKey(Theater, on_delete=models.CASCADE, related_name='reservations_at_theater')
    showtime = models.ForeignKey(Showtime, on_delete=models.CASCADE, related_name='reservations_at_showtime')
    reserve = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.movie.title} - {self.theater.name} - {self.showtime.available_seats}"

class Purchase(models.Model):
    name = models.CharField(max_length=225)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    theater = models.ForeignKey(Theater, on_delete=models.CASCADE, related_name='purchase_at_theater')
    showtime = models.ForeignKey(Showtime, on_delete=models.CASCADE, related_name='purchase_at_showtime')
    reserve = models.ForeignKey(Reserve, on_delete=models.CASCADE, related_name='purchase_at_showtime')
    purchase = models.DecimalField(max_digits=5, decimal_places=2)


    def __str__(self):
        return f"{self.movie.title} - {self.theater.name} - {self.showtime.available_seats} - {self.reserve.reserve}"

