# Parking Lot System

A Python implementation of a parking lot management system demonstrating core domain modeling, spot allocation, ticketing, and fare calculation.

## 🚗 Project Overview

This module models a parking lot that supports multiple spot types, floors, vehicles, and fee rules. It is designed to demonstrate:

- Object-oriented design and modeling of real-world entities.
- Separation of concerns between lot management, spot tracking, and fare calculation.
- Simple CLI-style sample execution.

## 📁 Directory Contents

- `config.py`: Static system configuration values (rates, slot counts, etc.).
- `floor.py`: Represents a parking floor containing multiple spots.
- `parking_spot.py`: Spot types and occupancy operations.
- `vehicle.py`: Vehicle types and identifiers.
- `ticket.py`: Ticket creation including entry/exit times and assigned spot.
- `fare.py`: Fare computation on exit, including time-based pricing.
- `parking_lot.py`: Main business logic for parking/unparking vehicles and status.
- `main.py`: Example scenario runner + basic usage.

## ▶️ How to run

1. Install Python 3.8+.
2. Execute sample flow:

```bash
cd parking_lot
python main.py
```

3. Observe output for park/unpark actions and fare summary.

## 🧩 Sample usage (script)

The `main.py` file includes a sample driver:

- Create parking lot instance
- Park vehicles of different types
- Generate ticket and free spot on exit
- Print total fare

## ✅ Learning outcomes

- floor/spot allocation logic
- ticket-based entry/exit tracking
- fare calculation with time checks
- scalable design for new vehicle/spot types

## 🔧 Extending the system

- Add reservations and prebooking
- Add scoring for EV charging and time-limits
- Integrate database persistence
- Add REST API interface (Flask/FastAPI)

## 📜 License

MIT License (or your own preferred license)
