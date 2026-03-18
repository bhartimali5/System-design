from abc import ABC, abstractmethod


# ─── Strategy Interface ───────────────────────────────────────
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount: float) -> bool:
        pass


# ─── Concrete Strategies ──────────────────────────────────────
class CreditCardPayment(PaymentStrategy):
    def __init__(self, card_number: str, cvv: str):
        self._card_number = card_number
        self._cvv = cvv

    def pay(self, amount: float) -> bool:
        print(f"Paid ₹{amount} using Credit Card ending {self._card_number[-4:]}")
        return True


class UPIPayment(PaymentStrategy):
    def __init__(self, upi_id: str):
        self._upi_id = upi_id

    def pay(self, amount: float) -> bool:
        print(f"Paid ₹{amount} using UPI ID {self._upi_id}")
        return True


class WalletPayment(PaymentStrategy):
    def __init__(self, wallet_balance: float):
        self._balance = wallet_balance

    def pay(self, amount: float) -> bool:
        if self._balance < amount:
            print(f"Insufficient wallet balance!")
            return False
        self._balance -= amount
        print(f"Paid ₹{amount} from Wallet. Remaining: ₹{self._balance}")
        return True


class NetBankingPayment(PaymentStrategy):
    def __init__(self, bank_name: str, account_id: str):
        self._bank = bank_name
        self._account = account_id

    def pay(self, amount: float) -> bool:
        print(f"Paid ₹{amount} via {self._bank} Net Banking")
        return True


# ─── Context ──────────────────────────────────────────────────
class ShoppingCart:
    def __init__(self):
        self._items = []
        self._payment_strategy = None

    def add_item(self, item: str, price: float):
        self._items.append({"item": item, "price": price})

    def set_payment_strategy(self, strategy: PaymentStrategy):
        self._payment_strategy = strategy   # swap payment method

    def checkout(self):
        if not self._payment_strategy:
            raise ValueError("No payment method selected!")

        total = sum(item["price"] for item in self._items)
        print(f"\nOrder Summary:")
        for item in self._items:
            print(f"  {item['item']} — ₹{item['price']}")
        print(f"Total: ₹{total}")

        success = self._payment_strategy.pay(total)
        if success:
            print("Order confirmed!")
        else:
            print("Payment failed!")


# ─── Usage ────────────────────────────────────────────────────
if __name__ == "__main__":
    cart = ShoppingCart()
    cart.add_item("iPhone 15", 79999)
    cart.add_item("AirPods", 14999)

    # Pay with UPI
    cart.set_payment_strategy(UPIPayment("rahul@upi"))
    cart.checkout()

    # Change mind — pay with wallet instead
    cart.set_payment_strategy(WalletPayment(wallet_balance=100000))
    cart.checkout()

    # Insufficient wallet
    cart.set_payment_strategy(WalletPayment(wallet_balance=5000))
    cart.checkout()