import sys
from storage_handler import StorageHandler
from seat_manager import SeatManager
from booking_engine import BookingEngine
from ticket_exporter import TicketExporter

def print_menu():
    print("\n" + "="*45)
    print("  TERMINAL TICKET RESERVATION SYSTEM")
    print("="*45)
    print("1. View Schedules & Seat Availability")
    print("2. Book Seats")
    print("3. View My Booking Details")
    print("4. Cancel Reservation")
    print("5. Exit")
    print("="*45)

def view_schedules(storage):
    shows = storage.load_shows()
    print("\n--- AVAILABLE SHOWS ---")
    for sid, show in shows.items():
        avail_seats = sum(1 for s in show.seats.values() if not s.is_reserved)
        total_seats = len(show.seats)
        print(f"[{sid}] {show.title:<22} | Time: {show.time} | Price: INR {show.price:.2f} | Available: {avail_seats}/{total_seats}")

def main():
    storage = StorageHandler()
    booking_engine = BookingEngine(storage)
    ticket_exporter = TicketExporter(storage)

    while True:
        print_menu()
        choice = input("Enter choice (1-5): ").strip()

        if choice == "1":
            view_schedules(storage)
            sid = input("\nEnter Show ID to inspect seat grid (or press Enter to return): ").strip().upper()
            shows = storage.load_shows()
            if sid in shows:
                SeatManager.render_seat_map(shows[sid])
            elif sid != "":
                print("Error: Invalid Show ID.")

        elif choice == "2":
            view_schedules(storage)
            sid = input("\nEnter Show ID to book: ").strip().upper()
            shows = storage.load_shows()

            if sid not in shows:
                print("Error: Invalid Show ID.")
                continue

            show = shows[sid]
            SeatManager.render_seat_map(show)

            name = input("Enter Customer Name: ").strip()
            if not name:
                print("Error: Name cannot be empty.")
                continue

            seats_input = input("Enter Seat IDs separated by comma (e.g. A1, A2): ").strip()
            if not seats_input:
                print("Error: No seats selected.")
                continue

            requested_seats = [s.strip().upper() for s in seats_input.split(",")]
            invalid, reserved = SeatManager.validate_seat_selection(show, requested_seats)

            if invalid or reserved:
                if invalid:
                    print(f"Error: Invalid seat numbers: {', '.join(invalid)}")
                if reserved:
                    print(f"Error: Seats already reserved: {', '.join(reserved)}")
                continue

            promo = input("Enter Promo Code (Press Enter if none, try 'WELCOME10'): ").strip()

            success, message, booking = booking_engine.create_booking(sid, name, requested_seats, promo)
            if success:
                ticket_file = ticket_exporter.generate_receipt(booking)
                print(f"\nSuccess: {message}")
                print(f"Total Amount Paid: INR {booking.total:.2f}")
                print(f"Receipt exported to: {ticket_file}")
            else:
                print(f"\nError: {message}")

        elif choice == "3":
            bid = input("Enter Booking Reference ID (e.g. TKT-XXXXXX): ").strip().upper()
            bookings = storage.load_bookings()
            if bid in bookings:
                b = bookings[bid]
                ticket_exporter.generate_receipt(b)
                print(f"\nBooking Details Found:")
                print(f"ID: {b.booking_id} | Name: {b.customer_name} | Status: {b.status} | Total: INR {b.total:.2f}")
                print("Receipt updated in tickets/ directory.")
            else:
                print("Error: Booking ID not found.")

        elif choice == "4":
            bid = input("Enter Booking Reference ID to cancel: ").strip().upper()
            success, message = ticket_exporter.cancel_booking(bid)
            if success:
                print(f"\nSuccess: {message}")
            else:
                print(f"\nError: {message}")

        elif choice == "5":
            print("\nThank you for using the Terminal Ticket Reservation System!")
            sys.exit(0)

        else:
            print("Error: Invalid selection. Please enter 1-5.")

if __name__ == "__main__":
    main()