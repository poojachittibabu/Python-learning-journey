class grandpa():
    def phone(self):
        print("grandpa phone")
class dad(grandpa):
     def money(self):
         print("dad's money")
class son(dad):
    def laptop(self):
        print("son's laptop")
ram=son()
ram .laptop()
ram.money()
ram.phone()
d1=dad()
d1.phone()
d1.money()

