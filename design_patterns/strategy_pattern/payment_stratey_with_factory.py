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
            print("Insufficient wallet balance!")
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


# ─── Payment Factory ──────────────────────────────────────────
class PaymentFactory:
    @staticmethod
    def create(payment_type: str, **kwargs) -> PaymentStrategy:
        factories = {
            "upi":         lambda: UPIPayment(
                               kwargs.get("upi_id")        ## using lambda so don't need to create obj immidiately
                           ),
            "credit_card": lambda: CreditCardPayment(
                               kwargs.get("card_number"),
                               kwargs.get("cvv")
                           ),
            "wallet":      lambda: WalletPayment(
                               kwargs.get("balance", 0.0)
                           ),
            "netbanking":  lambda: NetBankingPayment(
                               kwargs.get("bank_name"),
                               kwargs.get("account_id")
                           ),
        }

        creator = factories.get(payment_type.lower())
        if not creator:
            raise ValueError(
                f"Unknown payment type: {payment_type}. "
                f"Available: {list(factories.keys())}"
            )
        return creator()   # factory creates right strategy


# ─── Context ──────────────────────────────────────────────────
class ShoppingCart:
    def __init__(self):
        self._items = []
        self._payment_strategy = None

    def add_item(self, item: str, price: float):
        self._items.append({"item": item, "price": price})

    def set_payment_strategy(self, strategy: PaymentStrategy):
        self._payment_strategy = strategy

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

    # Factory creates right strategy — cart doesn't know concrete class
    upi = PaymentFactory.create("upi", upi_id="rahul@upi")
    cart.set_payment_strategy(upi)
    cart.checkout()

    # Swap to wallet 
    wallet = PaymentFactory.create("wallet", balance=100000)
    cart.set_payment_strategy(wallet)
    cart.checkout()

    # Swap to credit card 
    card = PaymentFactory.create("credit_card", card_number="1234567890123456", cvv="123")
    cart.set_payment_strategy(card)
    cart.checkout()

    # Swap to netbanking 
    netbanking = PaymentFactory.create("netbanking", bank_name="HDFC", account_id="ACC123")
    cart.set_payment_strategy(netbanking)
    cart.checkout()

    # Invalid payment type
    try:
        invalid = PaymentFactory.create("crypto")
    except ValueError as e:
        print(f"\nCaught error: {e}")