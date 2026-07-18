class student:
    def __init__(self):
        self.name="pooja"
        self.reg="123"
    def display(self):
        print("name:",self.name)
        print("reg no:",self.reg)
s1=student()
s2=student()
s1.name="hari"
s1.reg="2"
s2.name="kavi"
s2.reg="3"
s1.display()
s2.display()