class phone():
    chargertype="C type"
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
    def display(self):
        print("Brand:",self.brand)
        print("Price:",self.price)
        print("chargertype:",self.chargertype)
samsung=phone("Samsung","15000")
samsung.display()
vivo=phone("vivo","20000")
vivo.display()
