class SeatManager:
    """Manages seat map visualization and user selection validation."""
    @staticmethod
    def render_seat_map(show):
        print(f"\n--- SEAT MAP: {show.title} ({show.time}) ---")
        header = "      " + " ".join([f"[{c}]" for c in range(1, show.cols + 1)])
        print(header)
        
        for r in range(show.rows):
            row_letter = chr(65 + r)
            row_str = f" [{row_letter}] "
            for c in range(1, show.cols + 1):
                seat_id = f"{row_letter}{c}"
                seat = show.seats[seat_id]
                row_str += " [X]" if seat.is_reserved else " [O]"
            print(row_str)
        print("\n  Legend: [O] = Available | [X] = Reserved\n")

    @staticmethod
    def validate_seat_selection(show, seat_ids):
        invalid_seats = []
        reserved_seats = []

        for sid in seat_ids:
            sid = sid.upper().strip()
            if sid not in show.seats:
                invalid_seats.append(sid)
            elif show.seats[sid].is_reserved:
                reserved_seats.append(sid)

        return invalid_seats, reserved_seats