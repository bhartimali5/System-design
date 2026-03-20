# System Design

A collection of design pattern samples and a sample parking lot system implemented in Python. This repository is designed to help developers learn and evaluate architecture patterns and object-oriented design with straightforward examples.

## 🚀 Project Overview

- `design_patterns/`: Classic software design pattern implementations.
- `parking_lot/`: End-to-end parking lot system with ticketing and fare rules.

## 📁 Repository Structure

### design_patterns/

- `builder_pattern/`:
  - `burger_builder/`: builder pattern for constructing burger objects.
  - `http_request/`: builder pattern example for HTTP request composition.

- `decorator_pattern/`:
  - `coffee_menu.py`: coffee beverages with decorators to add condiments.
  - `text_formatter.py`: text formatting chain using decorators.
  - `request_handler.py`: HTTP request handling with decorator-style middleware.

- `factory_pattern/`:
  - `vehicle_rental_system.py`: factory pattern to create rental vehicles.

- `observer_pattern/`:
  - `stock_price_alert.py`: observer pattern for stock price subscription.
  - `youtube_channel_notification.py`: notification system for channel subscribers.

- `singleton_pattern/`:
  - `application_logger.py`, `logger.py`, `db_connection.py`, `config_parser.py`: singleton examples for shared resources.

- `strategy_pattern/`:
  - `payment_strategy.py`, `payment_stratey_with_factory.py`: payment method strategies.
  - `file_compressor.py`: file compression strategies.
  - `sorter.py`: sorting algorithm strategy pattern.

### parking_lot/

- `config.py`: system constants and settings.
- `floor.py`: floor-level parking management.
- `parking_spot.py`: spot classification and status.
- `vehicle.py`: vehicle entity.
- `ticket.py`: ticket generation and details.
- `fare.py`: fare calculations.
- `parking_lot.py`: parking lot service operations.
- `main.py`: script entrypoint / sample usage.

## 🧪 How to run

1. Clone repository:

```bash
git clone https://github.com/<your-org>/system-design.git
cd system-design
```

2. Run sample parking lot scenario:

```bash
python parking_lot/main.py
```

3. Explore pattern samples individually by executing relevant files in `design_patterns/`.

## ✅ What you can learn

- Builder pattern for gradual object construction and method chaining
- Decorator pattern for extensible behavior wrapping
- Factory pattern for dynamic object creation
- Observer pattern for event-driven updates
- Singleton pattern for global shared instances
- Strategy pattern for algorithmic interchangeability
- Practical domain modeling in the parking lot system

## 🧩 Contributing

1. Fork the repo.
2. Create feature branch (`git checkout -b feature/<name>`).
3. Add tests and update README if needed.
4. Commit and open a PR.

## 📄 License

MIT License (or your chosen license)


