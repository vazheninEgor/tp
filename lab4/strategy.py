from abc import ABC, abstractmethod

# Интерфейс стратегии расчета скидки
class DiscountStrategy(ABC):
    @abstractmethod
    def calculate_discount(self, amount):
        pass

# Стратегия для обычного клиента
class RegularCustomerDiscount(DiscountStrategy):
    def calculate_discount(self, amount):
        print("Applying regular customer discount.")
        return amount * 0.05  # 5% скидка

# Стратегия для VIP клиента
class VIPCustomerDiscount(DiscountStrategy):
    def calculate_discount(self, amount):
        print("Applying VIP customer discount.")
        return amount * 0.20  # 20% скидка

# Стратегия для клиента с акциями
class PromotionalDiscount(DiscountStrategy):
    def calculate_discount(self, amount):
        print("Applying promotional discount.")
        return amount * 0.10  # 10% скидка

class ShoppingCart:
    def __init__(self, discount_strategy: DiscountStrategy):
        self.discount_strategy = discount_strategy

    def set_discount_strategy(self, strategy: DiscountStrategy):
        self.discount_strategy = strategy

    def calculate_final_price(self, amount):
        discount = self.discount_strategy.calculate_discount(amount)
        return amount - discount

if __name__ == "__main__":
    cart = ShoppingCart(RegularCustomerDiscount())
    total_amount = 1000
    print(f"Final price: {cart.calculate_final_price(total_amount)}")

    cart.set_discount_strategy(VIPCustomerDiscount())
    print(f"Final price: {cart.calculate_final_price(total_amount)}")

    cart.set_discount_strategy(PromotionalDiscount())
    print(f"Final price: {cart.calculate_final_price(total_amount)}")