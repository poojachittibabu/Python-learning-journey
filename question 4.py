salary=int(input("salary"))
age=int(input("age"))
if(salary>=20000 or age<=25):
    loan=int(input("loan"))
    if(loan>50000):
        print("maximum amuont of loan is 50000")
    else:
        print("you are eligible")
else:
    print("you are not eligible")











