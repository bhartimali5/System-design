from abc import ABC, abstractmethod
from typing import List


# ─── Abstract Observer ────────────────────────────────────────
class Observer(ABC):
    @abstractmethod
    def update(self, data: dict) -> None:
        pass


# ─── Abstract Subject ─────────────────────────────────────────
class Subject(ABC):
    @abstractmethod
    def subscribe(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def unsubscribe(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def notify(self, data: dict) -> None:
        pass


# ─── Concrete Subject ─────────────────────────────────────────
class Stock(Subject):
    def __init__(self, name: str, initial_price: float):
        self._name = name
        self._price = initial_price          # initial price set
        self._observers: List[Observer] = []

    def subscribe(self, observer: Observer) -> None:
        if observer not in self._observers:
            self._observers.append(observer)

    def unsubscribe(self, observer: Observer) -> None:
        if observer in self._observers:
            self._observers.remove(observer)

    def notify(self, data: dict) -> None:
        for observer in self._observers:
            observer.update(data)

    def update_price(self, new_price: float) -> None:
        change = abs(new_price - self._price)    #  correct change calculation
        print(f"\nPrice changed: {self._name} {self._price} → {new_price} (change: {change})")
        self._price = new_price
        self.notify({
            "stock": self._name,
            "new_price": new_price,
            "change": change                     # change passed in data
        })


# ─── Concrete Observers ───────────────────────────────────────
class EmailAlert(Observer):
    def __init__(self, name: str, email: str, threshold: float):  #  injected
        self.name = name
        self._email = email
        self._threshold = threshold

    def update(self, data: dict) -> None:
        if data["change"] >= self._threshold:    #  checks change not price
            print(
                f"EMAIL to {self._email}: "
                f"{data['stock']} moved {data['change']} "
                f"— now {data['new_price']}"
            )


class SMSAlert(Observer):
    def __init__(self, name: str, phone: str, threshold: float):  #  injected
        self.name = name
        self._phone = phone
        self._threshold = threshold

    def update(self, data: dict) -> None:
        if data["change"] >= self._threshold:    #  checks change
            print(
                f"SMS to {self._phone}: "
                f"{data['stock']} moved {data['change']} "
                f"— now {data['new_price']}"
            )


class AppAlert(Observer):
    def __init__(self, name: str, threshold: float):              #  injected
        self.name = name
        self._threshold = threshold

    def update(self, data: dict) -> None:
        if data["change"] >= self._threshold:    #  checks change
            print(
                f"APP ALERT for {self.name}: "
                f"{data['stock']} moved {data['change']} "
                f"— now {data['new_price']}"
            )


# ─── Usage ────────────────────────────────────────────────────
if __name__ == "__main__":
    apple_stock = Stock("AAPL", 150.0)          #  initial price

    trader1 = EmailAlert("Rahul", "rahul@gmail.com", threshold=5.0)
    trader2 = SMSAlert("Priya", "+91-9876543210", threshold=2.0)
    trader3 = AppAlert("Arjun", threshold=10.0)

    apple_stock.subscribe(trader1)
    apple_stock.subscribe(trader2)
    apple_stock.subscribe(trader3)

    apple_stock.update_price(155.0)
    apple_stock.update_price(158.0)
    apple_stock.update_price(170.0)

    print("\n--- Priya unsubscribes ---")
    apple_stock.unsubscribe(trader2)
    apple_stock.update_price(175.0)
