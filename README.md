##### **#Terminal Ticket Reservation System**



A menu-driven Python application that manages event showtimes, real-time ASCII seat maps, booking subtotals, promo discounts, 18% GST tax calculation, automated receipt exports, and cancellations.



**#Table of Contents**


1.Overview
2.Features
3.Technologies Used
4.Installation
5.How to Run
6.How to Use
7.Testing
8.Pricing \& Tax Rules
9.Project Structure
10.Author



##### **#Overview**



Movie theaters and event venues require accurate real-time seat availability tracking, automated price/tax calculation, promo discount logic, prevention of double bookings, and instant ticket receipt generation. Doing these operations manually or across unstructured spreadsheets is slow and error-prone.

This project solves that problem with a simple command-line tool written in pure Python (standard library only). It lets a user browse active shows, view interactive ASCII seat grids, reserve seats, compute taxes and promo discounts, generate formatted plain-text ticket receipts, and process cancellations. All records are stored in local JSON files so data persists reliably between sessions.



\#Features

---

* **Show \& Seat Management: Browse available showtimes, ticket prices, and open seat counts.**
* **ASCII Seat Layout Map: Renders real-time visual grid maps (\[O] = Available, \[X] = Booked).**
* **Booking Engine: Full input validation with double-booking collision prevention.**
* **Automated Price Computation: Calculates subtotal, applies promo code discounts (WELCOME10), and adds 18% GST tax.**
* **Ticket Receipt Exporter: Generates formatted plain-text receipts saved inside a dedicated tickets/ directory.**
* **Cancellation Module: Cancels active bookings, calculates refunds, and immediately frees up reserved seats.**
* **Persistent Storage: Saves all state updates atomically to local JSON files (data/shows.json, data/bookings.json).**
* **Unit Test Suite: Comprehensive test coverage using Python's built-in unittest framework.**


##### **#Technologies Used**


       

|Category|Tool / Library|
|-|-|
|Language|Python 3.8+|
|Standard Library|json, os, sys, datetime, random, string|
|Testing|unittest|
|Version Control|Git \& GitHub|


#Installation
---


1.Clone the repository:


git clone https://github.com/keshav2428/terminal-ticket-system.git
cd terminal-ticket-system


2.Check Python version(must be 3.8 or higher):

python --version



##### \#How to Run



From the project root folder:
python main.py



You will see a menu like this:

============================================================

TERMINAL TICKET RESERVATION SYSTEM

============================================================

1\. View Shows \& Seat Availability

2\. Book Tickets

3\. View Booking Details / Ticket

4\. Cancel Booking

5\. List All Active Bookings

6\. Exit

\------------------------------------------------------------

Select an option (1-6):



##### \#How to Use


Follow this order when using the app:

|                            Step|                        Menu Option|                         What to Do|
|-|-|-|
|                             1|                            1|View available showtimes, ticket prices, and ASCII seat grid maps|
|                             2|                            2      |Reserve seats by entering Show ID, customer name, seats (e.g. A1, A2), and optional promo code|
|                             3|                            3|View a specific booking's breakdown and verify exported receipt file status|
|                             4|                            4|Cancel a reservation using the unique Booking Reference ID (frees up seats)|
|                             5|                            5|View a list of all active reservations currently in the system|
|                             6|                            6|Save all state updates and exit the program safely|


#Example Walkthrough
---


Select an option (1-6): 2



Enter Show ID: SHOW-101

Enter Customer Name: Keshav Saini



&#x20;     \[1] \[2] \[3] \[4] \[5] \[6]

&#x20;\[A]  \[O] \[O] \[O] \[O] \[O] \[O]

&#x20;\[B]  \[O] \[O] \[O] \[O] \[O] \[O]

&#x20;Legend: \[O] = Available | \[X] = Reserved



Enter seat numbers (comma-separated, e.g., A1, A2): A1, A2

Enter Promo Code (Press Enter to skip): WELCOME10



\------------------------------------------------------------

Booking Summary:

Subtotal: INR 500.00

Promo Discount (10%): -INR 50.00

Tax (GST 18%): +INR 81.00

TOTAL AMOUNT PAID: INR 531.00

\------------------------------------------------------------

Booking Reference ID: TKT-A81K9L

Receipt generated successfully in tickets/TKT-A81K9L.txt



\#Testing

---

Run the full unit test suite from the project root:

python -m unittest discover -s tests -v



The expected output should be:
test\_valid\_booking\_updates\_seat\_map ... ok

test\_double\_booking\_prevention ... ok

test\_promo\_code\_discount\_calculation ... ok

test\_cancellation\_frees\_seats ... ok

\----------------------------------------------------------------------

Ran 4 tests in 0.012s

OK



The suite covers:


* Double-booking prevention and seat matrix status validation
* Subtotal, 18% GST tax calculation, and promo code logic
* Cancellation workflows and seat state restoration
* JSON storage load/save persistence round-trips



##### \#Project Structure


terminal-ticket-system/

├── README.md              # Project documentation

├── statement.md           # Problem statement and system scope

├── .gitignore             # Files excluded from Git tracking

├── main.py                # Command-line interface and menu router

│

├── src/                   # Core application source code

│   ├── \_\_init\_\_.py        # Package marker

│   ├── models.py          # Data models (Seat, Show, Booking)

│   ├── seat\_manager.py    # ASCII seat matrix renderer

│   ├── booking\_engine.py  # Pricing, tax, and promo calculation

│   ├── storage\_handler.py # Local JSON storage persistence

│   └── ticket\_exporter.py # Plain-text receipt writer \& cancellation logic

│

├── tests/                 # Unit test suite

│   ├── \_\_init\_\_.py

│   └── test\_booking.py    # System logic and persistence tests

│

├── data/                  # Runtime persistence directory

│   ├── shows.json         # Active showtimes and seat grids

│   └── bookings.json      # Reservation registry

│

└── tickets/               # Export directory for text receipts (.txt)



Author Name: Keshav Saini
Roll Number: 26MEI10046
Course: Python Essentials
College: Vellore Institute of Technology
Submission: September 2026

