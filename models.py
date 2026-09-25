import uuid
from datetime import datetime

class Seat:
    """Represents a single seat in a venue."""
    def __init__(self, seat_id, is_reserved=False, reserved_by=None):
        self.seat_id = seat_id
        self.is_reserved = is_reserved
        self.reserved_by = reserved_by

    def to_dict(self):
        return {
            "seat_id": self.seat_id,
            "is_reserved": self.is_reserved,
            "reserved_by": self.reserved_by
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["seat_id"], data["is_reserved"], data.get("reserved_by"))


class Show:
    """Represents a scheduled show/event with seat layout."""
    def __init__(self, show_id, title, time, price, rows=4, cols=6, seats=None):
        self.show_id = show_id
        self.title = title
        self.time = time
        self.price = price
        self.rows = rows
        self.cols = cols
        self.seats = seats if seats is not None else self._init_seats()

    def _init_seats(self):
        seats = {}
        for r in range(self.rows):
            row_letter = chr(65 + r)
            for c in range(1, self.cols + 1):
                seat_id = f"{row_letter}{c}"
                seats[seat_id] = Seat(seat_id)
        return seats

    def to_dict(self):
        return {
            "show_id": self.show_id,
            "title": self.title,
            "time": self.time,
            "price": self.price,
            "rows": self.rows,
            "cols": self.cols,
            "seats": {sid: s.to_dict() for sid, s in self.seats.items()}
        }

    @classmethod
    def from_dict(cls, data):
        seats = {sid: Seat.from_dict(sdata) for sid, sdata in data["seats"].items()}
        return cls(data["show_id"], data["title"], data["time"], data["price"], data["rows"], data["cols"], seats)


class Booking:
    """Represents a completed reservation."""
    def __init__(self, booking_id, show_id, customer_name, seat_ids, subtotal, tax, total, timestamp=None, status="CONFIRMED"):
        self.booking_id = booking_id
        self.show_id = show_id
        self.customer_name = customer_name
        self.seat_ids = seat_ids
        self.subtotal = subtotal
        self.tax = tax
        self.total = total
        self.timestamp = timestamp or datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.status = status

    def to_dict(self):
        return self.__dict__

    @classmethod
    def from_dict(cls, data):
        return cls(**data)