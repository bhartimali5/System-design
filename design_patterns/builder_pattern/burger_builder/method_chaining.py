class Burger:
    def __init__(self):
        self.bun = None
        self.patty = None
        self.cheese = False
        self.toppings = []
        self.sauce = None

    
    def __str__(self):
        self.toppings.append("Lettuce")
        return f"Burger with {self.bun}, {self.patty}, cheese: {self.cheese}, toppings: {', '.join(self.toppings)}, sauce: {self.sauce}"
    

class BurgerBuider():
    def __init__(self):
        self._burger = Burger()

    def set_bun(self, bun):
        self._burger.bun = bun
        return self

    def set_patty(self, patty):
        self._burger.patty = patty
        return self

    def set_cheese(self, cheese):
        self._burger.cheese = cheese
        return self

    def set_toppings(self, toppings):
        self._burger.toppings = toppings
        return self

    def set_sauce(self, sauce):
        self._burger.sauce = sauce
        return self

    def get_burger(self):
        return self._burger
    

    ## Example usage
if __name__ == "__main__":
    burger = (BurgerBuider()
              .set_bun("Sesame")
              .set_patty("Beef")
              .set_cheese(True)
              .set_toppings(["Lettuce", "Tomato"])
              .set_sauce("Ketchup")
              .get_burger())
    
    print(burger)