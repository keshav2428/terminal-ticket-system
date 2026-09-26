Terminal Ticket Reservation SystemA menu-driven Python application that manages event showtimes, real-time ASCII seat maps, booking subtotals, promo discounts, 18% GST tax calculation, automated receipt exports, and cancellations.Table of ContentsOverviewFeaturesTechnologies UsedInstallationHow to RunHow to UseTestingPricing & Tax RulesProject StructureAuthorOverviewMovie theaters and event venues require accurate real-time seat availability tracking, automated price/tax calculation, promo discount logic, prevention of double bookings, and instant ticket receipt generation. Doing these operations manually or across unstructured spreadsheets is slow and error-prone.This project solves that problem with a simple command-line tool written in pure Python (standard library only). It lets a user browse active shows, view interactive ASCII seat grids, reserve seats, compute taxes and promo discounts, generate formatted plain-text ticket receipts, and process cancellations. All records are stored in local JSON files so data persists reliably between sessions.FeaturesShow & Seat Management: Browse available showtimes, ticket prices, and open seat counts.ASCII Seat Layout Map: Renders real-time visual grid maps ([O] = Available, [X] = Booked).Booking Engine: Full input validation with double-booking collision prevention.Automated Price Computation: Calculates subtotal, applies promo code discounts (WELCOME10), and adds 18% GST tax.Ticket Receipt Exporter: Generates formatted plain-text receipts saved inside a dedicated tickets/ directory.Cancellation Module: Cancels active bookings, calculates refunds, and immediately frees up reserved seats.Persistent Storage: Saves all state updates atomically to local JSON files (data/shows.json, data/bookings.json).Unit Test Suite: Comprehensive test coverage using Python's built-in unittest framework.Technologies UsedCategoryTool / LibraryLanguagePython 3.8+Standard Libraryjson, os, sys, datetime, random, stringTestingunittestVersion ControlGit & GitHubIDE (optional)VS Code / IDLEInstallationClone the repository:Bashgit clone https://github.com/keshav2428/terminal-ticket-system.git
cd terminal-ticket-system
Check Python version (must be 3.8 or higher):Bashpython --version
How to RunFrom the project root folder:Bashpython main.py
You will see a menu like this:Plaintext============================================================
TERMINAL TICKET RESERVATION SYSTEM
============================================================
1. View Shows & Seat Availability
2. Book Tickets
3. View Booking Details / Ticket
4. Cancel Booking
5. List All Active Bookings
6. Exit
------------------------------------------------------------
Select an option (1-6):
How to UseFollow this order when using the app:StepMenu OptionWhat to Do11View available showtimes, ticket prices, and ASCII seat grid maps22Reserve seats by entering Show ID, customer name, seats (e.g. A1, A2), and optional promo code33View a specific booking's breakdown and verify exported receipt file status44Cancel a reservation using the unique Booking Reference ID (frees up seats)55View a list of all active reservations currently in the system66Save all state updates and exit the program safelyExample WalkthroughPlaintextSelect an option (1-6): 2

Enter Show ID: SHOW-101
Enter Customer Name: Keshav Saini

      [1] [2] [3] [4] [5] [6]
 [A]  [O] [O] [O] [O] [O] [O]
 [B]  [O] [O] [O] [O] [O] [O]
 Legend: [O] = Available | [X] = Reserved

Enter seat numbers (comma-separated, e.g., A1, A2): A1, A2
Enter Promo Code (Press Enter to skip): WELCOME10

------------------------------------------------------------
Booking Summary:
Subtotal: INR 500.00
Promo Discount (10%): -INR 50.00
Tax (GST 18%): +INR 81.00
TOTAL AMOUNT PAID: INR 531.00
------------------------------------------------------------
Booking Reference ID: TKT-A81K9L
Receipt generated successfully in tickets/TKT-A81K9L.txt
TestingRun the full unit test suite from the project root:Bashpython -m unittest discover -s tests -v
The expected output should be:Plaintexttest_valid_booking_updates_seat_map ... ok
test_double_booking_prevention ... ok
test_promo_code_discount_calculation ... ok
test_cancellation_frees_seats ... ok
----------------------------------------------------------------------
Ran 4 tests in 0.012s
OK
The suite covers:Double-booking prevention and seat matrix status validationSubtotal, 18% GST tax calculation, and promo code logicCancellation workflows and seat state restorationJSON storage load/save persistence round-tripsPricing & Tax Rules$$\text{Discounted Subtotal} = \text{Subtotal} - \text{Promo Discount}$$$$\text{Tax (GST 18\%)} = \text{Discounted Subtotal} \times 0.18$$$$\text{Total Paid} = \text{Discounted Subtotal} + \text{Tax}$$ParameterRule / ValueGST Tax Rate18% applied to discounted subtotalPromo Code WELCOME10Grants 10% discount on base subtotalSeat Grid Symbols[O] = Available for selection | [X] = Reserved / UnavailableProject StructurePlaintextterminal-ticket-system/
├── README.md              # Project documentation
├── statement.md           # Problem statement and system scope
├── .gitignore             # Files excluded from Git tracking
├── main.py                # Command-line interface and menu router
│
├── src/                   # Core application source code
│   ├── __init__.py        # Package marker
│   ├── models.py          # Data models (Seat, Show, Booking)
│   ├── seat_manager.py    # ASCII seat matrix renderer
│   ├── booking_engine.py  # Pricing, tax, and promo calculation
│   ├── storage_handler.py # Local JSON storage persistence
│   └── ticket_exporter.py # Plain-text receipt writer & cancellation logic
│
├── tests/                 # Unit test suite
│   ├── __init__.py
│   └── test_booking.py    # System logic and persistence tests
│
├── data/                  # Runtime persistence directory
│   ├── shows.json         # Active showtimes and seat grids
│   └── bookings.json      # Reservation registry
│
└── tickets/               # Export directory for text receipts (.txt)
AuthorName: Keshav SainiRoll Number: 26MEI10046Course: Python EssentialsCollege: Vellore Institute of TechnologySubmission: September 2026
