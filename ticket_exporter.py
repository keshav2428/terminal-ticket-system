import os

TICKETS_DIR = "tickets"

class TicketExporter:
    """Handles receipt file generation and booking cancellation processing."""
    def __init__(self, storage):
        self.storage = storage
        os.makedirs(TICKETS_DIR, exist_ok=True)

    def generate_receipt(self, booking):
        shows = self.storage.load_shows()
        show = shows.get(booking.show_id)
        show_title = show.title if show else "N/A"
        show_time = show.time if show else "N/A"

        filename = os.path.join(TICKETS_DIR, f"ticket_{booking.booking_id}.txt")
        ticket_text = f"""
==================================================
           TERMINAL TICKET RESERVATION            
==================================================
Booking Reference : {booking.booking_id}
Customer Name     : {booking.customer_name}
Date & Time       : {booking.timestamp}
Status            : {booking.status}
--------------------------------------------------
Show Title        : {show_title}
Show Time         : {show_time}
Seats Reserved    : {', '.join(booking.seat_ids)}
--------------------------------------------------
Subtotal          : INR {booking.subtotal:.2f}
Tax (18%)         : INR {booking.tax:.2f}
TOTAL PAID        : INR {booking.total:.2f}
==================================================
        Thank you for booking with us!            
==================================================
"""
        with open(filename, "w") as f:
            f.write(ticket_text)
        return filename

    def cancel_booking(self, booking_id):
        bookings = self.storage.load_bookings()
        shows = self.storage.load_shows()

        if booking_id not in bookings:
            return False, "Booking ID not found."

        booking = bookings[booking_id]
        if booking.status == "CANCELLED":
            return False, "Booking is already cancelled."

        show = shows.get(booking.show_id)
        if show:
            for sid in booking.seat_ids:
                if sid in show.seats:
                    show.seats[sid].is_reserved = False
                    show.seats[sid].reserved_by = None

        booking.status = "CANCELLED"
        self.storage.save_shows(shows)
        self.storage.save_bookings(bookings)
        self.generate_receipt(booking)

        return True, f"Booking {booking_id} cancelled successfully. Refund of INR {booking.total:.2f} processed."