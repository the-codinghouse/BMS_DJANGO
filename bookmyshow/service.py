from bookmyshow.models import User, Show, ShowSeat, ShowSeatStatus, Ticket, BookingStatus
import random
import string


def generate_ticket_number():
    """Generate a unique ticket number"""
    while True:
        ticket_number = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
        if not Ticket.objects.filter(ticket_number=ticket_number).exists():
            return ticket_number


def create_booking(user_id, show_seat_ids, show_id):
    if len(show_seat_ids) > 10:
        raise ValueError("Show seat id must be less than 10")
    try:
        user = User.objects.get(id=user_id)
        if user is None:
            raise User.DoesNotExist

        show = Show.objects.get(id=show_id)
        if show is None:
            raise Show.DoesNotExist

        show_seats = ShowSeat.objects.filter(id__in=show_seat_ids)
        for show_seat in show_seats:
            if show_seat.show_seat_status != ShowSeatStatus.AVAILABLE:
                raise ValueError('Show seat status is not available')

        for show_seat in show_seats:
            show_seat.show_seat_status = ShowSeatStatus.LOCKED
            show_seat.save()

        # create booking
        booking = Ticket(
            user=user,
            show=show,
            amount=100,
            booking_status=BookingStatus.PENDING,
            ticket_number=generate_ticket_number(),
            # show_seat=show_seats
        )
        booking.save()

        # create payment

        for show_seat in show_seats:
            show_seat.show_seat_status = ShowSeatStatus.RESERVED
            show_seat.save()

        booking.show_seats = show_seats
        booking.save()
        return booking

    except Exception as e:
        print(e)


class BookShowService:
    pass
