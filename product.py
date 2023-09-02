class Product:
    def __init__(self,product_name,price):
        self.product_name = product_name
        self.price = price
        print(f"product_Name : {self.product_name} , price : {self.price}")

class Discount:
    def calculate_discount(self):
        discount_price = self.price * 10 / 100
        return discount_price
