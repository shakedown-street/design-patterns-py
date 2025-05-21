"""
This is an example of the builder creational pattern implemented in Python.

This is usually not a common or recommended pattern in Python
because you can create flexible constructors with *args and **kwargs
to handle optional or named parameters without long, confusing construtors.
Additionally, Python's @dataclass decorator further reduces the need for
implementing the builder pattern.

Situationally however, the builder pattern can still be useful in Python
for complex object creation or enforcing step-by-step building.
"""


class Product:
    def __init__(
        self,
        name: str,
        description: str,
        is_featured: bool,
        price: float,
        is_active: bool,
    ):
        self.name = name
        self.description = description
        self.is_featured = is_featured
        self.price = price
        self.is_active = is_active

    def display(self):
        print("Product ------------")
        print("Name", self.name)
        print("Price", self.price)
        print("Featured", self.is_featured)
        print("Description", self.description)
        print("Active", self.is_active)


class ProductBuilder:
    def __init__(self):
        self.name = ""
        self.description = ""
        self.is_featured = False
        self.price = 0
        self.is_active = True

    def set_name(self, name: str):
        self.name = name
        return self

    def set_description(self, description: str):
        self.description = description
        return self

    def set_is_featured(self, is_featured: bool):
        self.is_featured = is_featured
        return self

    def set_price(self, price: float):
        self.price = price
        return self

    def set_is_active(self, is_active: bool):
        self.is_active = is_active
        return self

    def validate(self):
        if not self.name:
            raise ValueError("`name` is required and has not been set")

        if not self.price:
            raise ValueError("`price` is required and has not been set")

    def build(self) -> Product:
        self.validate()

        return Product(
            self.name,
            self.description,
            self.is_featured,
            self.price,
            self.is_active,
        )


product_1 = (
    ProductBuilder()
    .set_name("Product 1")
    .set_description("Here is my description of product 1")
    .set_price(19.99)
    .build()
)
product_2 = (
    ProductBuilder()
    .set_name("Product 2")
    .set_description("Here is my description of product 2")
    .set_price(24.99)
    .set_is_featured(True)
    .build()
)

product_1.display()
product_2.display()
