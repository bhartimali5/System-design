from design_patterns.builder_pattern.burger_builder.burger import Burger
from design_patterns.builder_pattern.burger_builder.burger_builder import BurgerBuilder

class NonVegBurgerBuilder(BurgerBuilder):

    def __init__(self):
        self._burger = Burger()

    def set_bun(self):
        self._burger.bun = "Sesame Seed Bun"

    def set_patty(self):
        self._burger.patty = "Chicken Patty"

    def set_cheese(self):
        self._burger.cheese = True

    def set_toppings(self):
        self._burger.toppings = ["Lettuce", "Tomato", "Onion"]

    def set_sauce(self):
        self._burger.sauce = "BBQ Sauce"

    def set_size(self):
        self._burger.size = "Large"

    def get_burger(self) -> Burger:
        return self._burger