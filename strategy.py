"""
This is an example of the strategy behavioral pattern implemented in Python.

Scenario:
We have an e-commerce application that calculates shipping costs based on
different shipping strategies.
"""


class ShippingStrategy:
    def calculate_shipping(self):
        raise NotImplementedError("Shipping strategy not implemented.")


class StandardShipping(ShippingStrategy):
    def calculate_shipping(self):
        return 5.00


class ExpressShipping(ShippingStrategy):
    def calculate_shipping(self):
        return 15.00


class OvernightShipping(ShippingStrategy):
    def calculate_shipping(self):
        return 25.00


class Order:
    def __init__(self, subtotal: float, shipping_strategy: ShippingStrategy):
        self._shipping_strategy = shipping_strategy
        self.subtotal = subtotal

    def set_shipping_strategy(self, shipping_strategy: ShippingStrategy):
        self._shipping_strategy = shipping_strategy

    def calculate_total(self):
        shipping_cost = self._shipping_strategy.calculate_shipping()
        return self.subtotal + shipping_cost


standard_shipping = StandardShipping()
express_shipping = ExpressShipping()
overnight_shipping = OvernightShipping()

order = Order(250.00, standard_shipping)
print("Total with Standard Shipping:", order.calculate_total())

order.set_shipping_strategy(express_shipping)
print("Total with Express Shipping:", order.calculate_total())

order.set_shipping_strategy(overnight_shipping)
print("Total with Overnight Shipping:", order.calculate_total())
