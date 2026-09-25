import random
import string
from models import Booking

class BookingEngine:
    """Handles reservation rules, taxes, promo codes, and collision checks."""
    TAX_RATE = 0.18  # 18% Tax

    def __init__(self, storage):
        self.storage = storage

    def generate_booking_id(self):
        return "TKT-" + "".join(random.choices(string.ascii_uppercase + string.digits, k=6))

    def create_booking(self, show_id, customer_name, requested_seat_ids, promo_code=None):
        shows = self.storage.load_shows()
        bookings = self.storage.load_bookings()

        if show_id not in shows:
            return False, "Invalid Show ID selected.", None

        show = shows[show_id]
        clean_seats = [s.upper().strip() for s in requested_seat_ids]

        for sid in clean_seats:
            if sid not in show.seats or show.seats[sid].is_reserved:
                return False, f"Seat {sid} is no longer available.", None

        unit_price = show.price
        subtotal = unit_price * len(clean_seats)
        
        discount = 0.0
        if promo_code and promo_code.upper() == "WELCOME10":
            discount = subtotal * 0.10
        
        taxable_amount = subtotal - discount
        tax = taxable_amount * self.TAX_RATE
        total = taxable_amount + tax

        for sid in clean_seats:
            show.seats[sid].is_reserved = True
            show.seats[sid].reserved_by = customer_name

        booking_id = self.generate_booking_id()
        new_booking = Booking(
            booking_id=booking_id,
            show_id=show_id,
            customer_name=customer_name,
            seat_ids=clean_seats,
            subtotal=round(subtotal, 2),
            tax=round(tax, 2),
            total=round(total, 2)
        )

        bookings[booking_id] = new_booking
        self.storage.save_shows(shows)
        self.storage.save_bookings(bookings)

        return True, "Booking successful!", new_booking