

class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

    def display_info(self):
        print(f"product ID: {self.product_id}")
        print(f"name: {self.name}")
        print(f"price: {self.price:}")


class Book(Product):
    def __init__(self, product_id, name, price, author):
        super().__init__(product_id, name, price)
        self.author = author

    def display_info(self):
        super().display_info()
        print(f"author: {self.author}")


book = Book(101, "The Great Gatsby", 10.99, "F. Scott Fitzgerald")
book.display_info()
