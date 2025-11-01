import time
password=1234
balance=25000
print("welcome to Rahul ATM")
print("insert your card")
card=int(input("press 1.yes 2.no :"))
if card==1:
    print("select the language")
    print("press 1.English 2.kannada 3.telugu :")
    lang=int(input())
    if lang==1:
        print("print enter your pin :")
        pin=int(input())
        if pin==password:
            print("select the option")
            print("1.Balance Enq 2.withdrawl")
            opt=int(input())
            if opt==1:
                print("your available balance is",balance)
            elif opt==2:
                print("enter the amount")
                amt=int(input())
                if amt%100!=0:
                    print("your transaction is proccessing")
                    time.sleep(3)
                    print("enter amount in the multiple of 100's , please try again")
                elif amt>balance:
                    print("your transaction is proccessing")
                    time.sleep(3)
                    print("withdrawl amount is greater than balance , please try again")
                else:
                    print("your transaction is proccessing")
                    time.sleep(3)
                    print("collect your cash ")
                    time.sleep(3)
                    print("do you want to check your balance")
                    print("1.yes 2.no")
                    choice=int(input())
                    if choice==1:
                        print("your available balance is",balance-amt)
                        print("thank you visit again")
                    else:
                        print("thank you visit again")
            else:
                print("wrong option")
        else:
            print("wrong pin")

    else:
        print("please select only english")
else:
    print("insert your card properly")

