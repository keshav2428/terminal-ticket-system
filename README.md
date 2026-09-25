\# Terminal Ticket Reservation System



An interactive command-line application designed for browsing showtimes, inspecting real-time seat maps, booking seats with tax/discount support, and generating printable text-file receipts.



\## Technologies Used

\- \*\*Language:\*\* Python 3.8+

\- \*\*Libraries:\*\* Standard Library (`json`, `os`, `sys`, `datetime`, `random`, `string`)



\## Functional Modules

1\. \*\*Schedule \& Seat Layout Manager:\*\* Displays available shows, calculates open seats, and displays interactive ASCII seat maps.

2\. \*\*Booking Engine:\*\* Calculates subtotals, taxes (18%), promo codes (e.g., `WELCOME10`), and blocks double-booking.

3\. \*\*Ticket Exporter \& Cancellation Engine:\*\* Generates plain-text receipt files in `tickets/` and processes cancellations.



\## Installation \& Setup

1\. Clone the repository:

&#x20;  ```bash

&#x20;  git clone \[https://github.com/keshav2428/terminal-ticket-system]
&#x20;  cd {terminal-ticket-system}

