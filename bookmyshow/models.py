import random
import string

from django.utils import timezone

from django.db import models


# Create your models here.
# base model.
class BaseModel(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    id = models.BigAutoField(primary_key=True)

    class Meta:
        abstract = True


# model 2
class User(BaseModel):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)


# model 3
class Region(BaseModel):
    name = models.CharField(max_length=50)


# model 4
class Theatre(BaseModel):
    name = models.CharField(max_length=50)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)


# model 5
class Feature(BaseModel):
    name = models.CharField(max_length=50)


# model 6
class Screen(BaseModel):
    name = models.CharField(max_length=50)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    theatre = models.ForeignKey(Theatre, on_delete=models.CASCADE)


# model 7
class ScreenFeature(BaseModel):
    screen = models.ForeignKey(Screen, on_delete=models.CASCADE)
    feature = models.ForeignKey(Feature, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('screen', 'feature'),)


# model 8
class Movie(BaseModel):
    title = models.CharField(max_length=50)
    release_date = models.DateField()
    director = models.CharField(max_length=50)
    actors = models.CharField(max_length=50)


# model 9
class Show(BaseModel):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    start_time = models.TimeField()
    end_time = models.TimeField()
    screen = models.ForeignKey(Screen, on_delete=models.CASCADE)
    feature = models.ForeignKey(Feature, on_delete=models.CASCADE)


# model 10
class SeatType(models.TextChoices):
    GOLD = 'GOLD', 'Gold'
    SILVER = 'SILVER', 'Silver'
    PLATINUM = 'PLATINUM', 'Platinum'


# model 11
class Seat(BaseModel):
    row_number = models.IntegerField()
    col_number = models.IntegerField()
    number = models.IntegerField()  # max_length is not needed for IntegerField
    seat_type = models.CharField(max_length=50, choices=SeatType.choices)  # Use .choices


# model 12
class ShowSeatStatus(models.TextChoices):
    AVAILABLE = 'AVAILABLE', 'Available'
    MAINTENANCE = 'MAINTENANCE', 'Maintenance'
    RESERVED = 'RESERVED', 'Reserved'
    LOCKED = 'LOCKED', 'Locked'
    FEMALEONLY = 'FEMALEONLY', 'FemaleOnly'


# model 13
class ShowSeat(BaseModel):
    show = models.ForeignKey(Show, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    show_seat_status = models.CharField(max_length=50, choices=ShowSeatStatus.choices)


# model 14
class ShowSeatType(BaseModel):
    show = models.ForeignKey(Show, on_delete=models.CASCADE)
    seat_type = models.CharField(max_length=50, choices=SeatType.choices)  # Changed ForeignKey to CharField
    price = models.IntegerField()


# model 15
class BookingStatus(models.TextChoices):
    PENDING = 'PENDING', 'Pending'
    CONFIRMED = 'CONFIRMED', 'Confirmed'
    WAITING = 'WAITING', 'Waiting'
    CANCELLED = 'CANCELLED', 'Cancelled'


# model 16
class PaymentMode(models.TextChoices):
    UPI = 'UPI', 'UPI'
    CREDIT_CARD = 'CREDIT_CARD', 'Credit Card'
    DEBIT_CARD = 'DEBIT_CARD', 'Debit Card'
    NET_BANKING = 'NET_BANKING', 'Net Banking'
    CASH = 'CASH', 'Cash'


# model 17
class PaymentStatus(models.TextChoices):
    PENDING = 'PENDING', 'Pending'
    CONFIRMED = 'CONFIRMED', 'Confirmed'
    WAITING = 'WAITING', 'Waiting'
    CANCELLED = 'CANCELLED', 'Cancelled'
    REFUNDED = 'REFUNDED', 'Refunded'


# model 18
class Ticket(BaseModel):
    ticket_number = models.CharField(max_length=12, unique=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    show = models.ForeignKey(Show, on_delete=models.CASCADE)
    show_seats = models.ManyToManyField(ShowSeat)
    amount = models.IntegerField()
    booking_status = models.CharField(max_length=50, choices=BookingStatus.choices)

    def generate_ticket_number(self):
        """Generate a unique ticket number"""
        while True:
            ticket_number = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
            if not Ticket.objects.filter(ticket_number=ticket_number).exists():
                return ticket_number

    def save(self, *args, **kwargs):
        if not self.ticket_number:
            self.ticket_number = self.generate_ticket_number()
        super().save(*args, **kwargs)


# model 19
class Payment(BaseModel):
    ref_number = models.IntegerField()
    amount = models.IntegerField()
    mode = models.CharField(max_length=50, choices=PaymentMode.choices)
    status = models.CharField(max_length=50, choices=PaymentStatus.choices)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
