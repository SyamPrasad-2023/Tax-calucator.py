'''code to illustrate a product with its price by normal instance and calculate
the product tax rate by 10% in a class method as print 
total amount to be paid'''

class Product:
    tax_rate=0.18
    def __init__(self, name, price):
        self.name = name
        
        self.price = price
    def finalprice(self):
        total= self.price * (1+Product.tax_rate)
        print(f" final price of {self.name} is {total:.2f}")
    @classmethod
    def setax(cls,rate):
        cls.tax_rate = rate/100
name= str(input("enter the product name:")) 
price = float(input("enter the product price:"))
rate= int (input("enter tax_rate in %:"))
Product.setax(rate)
item= Product(name,price)
item.finalprice()
