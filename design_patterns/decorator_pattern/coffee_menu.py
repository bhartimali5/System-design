from abc import ABC, abstractmethod


# ─── Abstract Component ───────────────────────────────────────
class Coffee(ABC):
    @abstractmethod
    def get_cost(self) -> float:
        pass

    @abstractmethod
    def get_description(self) -> str:
        pass


# ─── Concrete Component ───────────────────────────────────────
class SimpleCoffee(Coffee):
    def get_cost(self) -> float:
        return 50.0

    def get_description(self) -> str:
        return "Simple Coffee"


# ─── Abstract Decorator ───────────────────────────────────────
class CoffeeDecorator(Coffee):
    def __init__(self, coffee: Coffee):
        self._coffee = coffee          # wraps existing coffee ✅

    def get_cost(self) -> float:
        return self._coffee.get_cost() # delegates to wrapped coffee

    def get_description(self) -> str:
        return self._coffee.get_description()


# ─── Concrete Decorators ──────────────────────────────────────
class MilkDecorator(CoffeeDecorator):
    def get_cost(self) -> float:
        return self._coffee.get_cost() + 10.0   # adds milk cost

    def get_description(self) -> str:
        return self._coffee.get_description() + " + Milk"


class SugarDecorator(CoffeeDecorator):
    def get_cost(self) -> float:
        return self._coffee.get_cost() + 5.0

    def get_description(self) -> str:
        return self._coffee.get_description() + " + Sugar"


class VanillaDecorator(CoffeeDecorator):
    def get_cost(self) -> float:
        return self._coffee.get_cost() + 15.0

    def get_description(self) -> str:
        return self._coffee.get_description() + " + Vanilla"


class WhipDecorator(CoffeeDecorator):
    def get_cost(self) -> float:
        return self._coffee.get_cost() + 8.0

    def get_description(self) -> str:
        return self._coffee.get_description() + " + Whip"


# ─── Usage ────────────────────────────────────────────────────
if __name__ == "__main__":

    # Plain coffee
    coffee = SimpleCoffee()
    print(f"{coffee.get_description()} = ₹{coffee.get_cost()}")
    # Simple Coffee = ₹50.0

    # Add milk
    coffee = MilkDecorator(coffee)
    print(f"{coffee.get_description()} = ₹{coffee.get_cost()}")
    # Simple Coffee + Milk = ₹60.0

    # Add sugar
    coffee = SugarDecorator(coffee)
    print(f"{coffee.get_description()} = ₹{coffee.get_cost()}")
    # Simple Coffee + Milk + Sugar = ₹65.0

    # Add vanilla
    coffee = VanillaDecorator(coffee)
    print(f"{coffee.get_description()} = ₹{coffee.get_cost()}")
    # Simple Coffee + Milk + Sugar + Vanilla = ₹80.0

    # Add double milk — decorators can be applied multiple times ✅
    coffee = MilkDecorator(coffee)
    print(f"{coffee.get_description()} = ₹{coffee.get_cost()}")
    # Simple Coffee + Milk + Sugar + Vanilla + Milk = ₹90.0

    # Different combination — no new class needed ✅
    print("\n--- Different Order ---")
    coffee2 = WhipDecorator(VanillaDecorator(SimpleCoffee()))
    print(f"{coffee2.get_description()} = ₹{coffee2.get_cost()}")
    # Simple Coffee + Vanilla + Whip = ₹73.0
