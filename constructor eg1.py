class laptop:
    def __init__(self):
        self.price=0
        self.ram=""
        self.proc=""
        print("demo")
    def display(self):
        print("price:",self.price)
hp=laptop()       
hp.price=50000
hp.ram="15gb"
hp.proc="i5"
hp.display()
print(hp.ram)