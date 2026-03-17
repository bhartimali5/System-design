from burger_builder import BurgerBuilder
from design_patterns.builder_pattern.burger_builder.veg_burger import VegBurgerBuilder

##The Director ensures the order of construction never changes and it is independent of the concrete builder and product.
class BurgerConstructor:
    def __init__(self, builder: BurgerBuilder):
        self._builder = builder

    def construct_burger(self):
        self._builder.set_bun()
        self._builder.set_patty()
        self._builder.set_cheese()
        self._builder.set_toppings()
        self._builder.set_sauce()
        self._builder.set_size()
        return self._builder.get_burger()
    

## Example usage:
veg_burger_builder = VegBurgerBuilder()
burger_constructor = BurgerConstructor(veg_burger_builder)
veg_burger = burger_constructor.construct_burger()    