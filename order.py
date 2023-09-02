from product import Product,Discount
from customer import Customer

class Productprice(Product,Discount,Customer):
    def __init__(self,product_name,price):
        super().__init__(product_name,price)
    def total_price(self):    
        product_price = self.price - super().calculate_discount()
        print(f"total_product_price : {product_price}")
        
        
obj1 = Productprice("product-1",2000)
obj1.cus_info("john","rajkot",36578,"tyr@gmail.com")
discount_price = obj1.calculate_discount()
print("product discount_price :",discount_price)
obj1.total_price()

