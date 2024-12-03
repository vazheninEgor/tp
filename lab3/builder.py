# Продукт
class Pizza:
    def __init__(self):
        self.dough = None
        self.sauce = None
        self.topping = None

    def __str__(self):
        return f"Pizza with {self.dough} dough, {self.sauce} sauce, and {self.topping} topping"

# Интерфейс строителя
class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()

    def set_dough(self, dough):
        self.pizza.dough = dough
        return self

    def set_sauce(self, sauce):
        self.pizza.sauce = sauce
        return self

    def set_topping(self, topping):
        self.pizza.topping = topping
        return self

    def build(self):
        return self.pizza

# Директор
class PizzaDirector:
    def __init__(self, builder: PizzaBuilder):
        self.builder = builder

    def construct_hawaiian_pizza(self):
        return self.builder.set_dough("cross").set_sauce("mild").set_topping("ham+pineapple").build()

# Пример использования
builder = PizzaBuilder()
director = PizzaDirector(builder)

hawaiian_pizza = director.construct_hawaiian_pizza()
print(hawaiian_pizza)