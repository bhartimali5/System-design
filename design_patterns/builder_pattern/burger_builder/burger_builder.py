"""
classic+director for fixed menu burgers
method chaining for custom burgers
"""

from design_patterns.builder_pattern.burger_builder.burger import Burger
from abc import ABC, abstractmethod

class BurgerBuilder(ABC):

    @abstractmethod
    def set_bun(self):
        pass

    @abstractmethod
    def set_patty(self):
        pass

    @abstractmethod
    def set_cheese(self):
        pass

    @abstractmethod
    def set_toppings(self):
        pass

    @abstractmethod
    def set_sauce(self):
        pass

    @abstractmethod
    def set_size(self):
        pass

    def get_burger(self) -> Burger: 
        pass
       
    