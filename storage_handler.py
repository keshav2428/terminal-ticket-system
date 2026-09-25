import json
import os
from models import Show, Booking

DATA_DIR = "data"
SHOWS_FILE = os.path.join(DATA_DIR, "shows.json")
BOOKINGS_FILE = os.path.join(DATA_DIR, "bookings.json")

class StorageHandler:
    """Handles persistent data storage using local JSON files."""
    def __init__(self):
        os.makedirs(DATA_DIR, exist_ok=True)
        self._ensure_default_data()

    def _ensure_default_data(self):
        if not os.path.exists(SHOWS_FILE):
            default_shows = [
                Show("S101", "Interstellar (IMAX)", "18:00", 250.0).to_dict(),
                Show("S102", "Inception (2D)", "21:00", 200.0).to_dict(),
                Show("S103", "The Dark Knight", "15:00", 180.0).to_dict()
            ]
            with open(SHOWS_FILE, "w") as f:
                json.dump(default_shows, f, indent=4)
        if not os.path.exists(BOOKINGS_FILE):
            with open(BOOKINGS_FILE, "w") as f:
                json.dump([], f, indent=4)

    def load_shows(self):
        with open(SHOWS_FILE, "r") as f:
            data = json.load(f)
        return {item["show_id"]: Show.from_dict(item) for item in data}

    def save_shows(self, shows_dict):
        data = [show.to_dict() for show in shows_dict.values()]
        with open(SHOWS_FILE, "w") as f:
            json.dump(data, f, indent=4)

    def load_bookings(self):
        with open(BOOKINGS_FILE, "r") as f:
            data = json.load(f)
        return {item["booking_id"]: Booking.from_dict(item) for item in data}

    def save_bookings(self, bookings_dict):
        data = [b.to_dict() for b in bookings_dict.values()]
        with open(BOOKINGS_FILE, "w") as f:
            json.dump(data, f, indent=4)