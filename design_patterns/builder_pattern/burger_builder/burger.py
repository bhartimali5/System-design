class Burger:
    def __init__(self):
        self.bun = None
        self.patty = None
        self.cheese = False
        self.toppings = []
        self.sauce = None
        self.size = None


    def __str__(self):
        self.toppings = []
        self.toppings.append("Lettuce")
        self.toppings.append("Tomato")
        self.toppings.append("Cheese")
       
        return (f"Burger(size={self.size}, bun={self.bun}, patty={self.patty}, "
                f"cheese={self.cheese}, toppings={self.toppings}, sauce={self.sauce})")