print("welcome to bank abc")
balance=10000
a=input("choose a language :a)eng b)kan c)hin :")
pin=int(input("enter pin :"))
if pin!=1234:
    print("incorrect pin")
else:
    o=int(input("select your option :1)balance enquire 2)withdrawl :"))
    if o==1:
        print(balance)
    else:
        w=int(input("enter withdraw amount :"))
        balance=balance-w
        x=input("do you want to display the balance (y or n):")
        if x=='y':
            print(balance)
            print("thankyou visit again")
        else:
            print("thankyou visit again")