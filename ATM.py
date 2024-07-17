import time
print("Welcome!! Please insert your card")
time.sleep(4) 
password = 1032
pin = int(input("Enter your ATM Pin: ")) 
balance = 20000
if password == pin:
    while True:
        print("\t 1 == Account balance inquiry")
        print("\t 2 == Cash withdrawal")
        print("\t 3 == Cash deposit")
        print("\t 4 == PIN change")
        print("\t 5 == Transaction history")
        print("\t 6 == Exit")
        print("\n")
        try: 
            option = int(input("Please enter your choice: "))
        except:
            print("Please enter valid choice")
        if option == 1: 
            print(f"Your current balance {balance}")
            print("------------------------------------------------")
            print("------------------------------------------------")
        elif option == 2: 
            withdraw_amount = int(input("Enter amount to withdrawal: "))
            balance = balance-withdraw_amount
            if withdraw_amount<=balance:
                print(f"Your updated balance is {balance}")
                print("------------------------------------------------")
                print("------------------------------------------------")
                continue
            else:
                print("There is NO sufficient balance please try again..")
                print("------------------------------------------------")
                print("------------------------------------------------")
                break
        elif option == 3: 
            deposited_amount = int(input("Enter amount to deposit: "))
            balance = balance+deposited_amount
            print(f"Your updated balance is {balance}")
            print("------------------------------------------------")
            print("------------------------------------------------")
            continue
        elif option == 4: 
            print("Loading.......")
            print("Change pin")
            old_password=int(input("Enter your old password :"))
            if old_password==password:
                enter_new_pin = int(input("Enter your new pin: "))
                print("------------------------------------------------")
                print("------------------------------------------------")
                password = enter_new_pin
                continue
            else:
                print("wrong password please enter correct password!!!..")
                print("------------------------------------------------")
                print("------------------------------------------------")
                break
        elif option == 5:
            print("New Transaction History")
            print(f"Your account current balance is :{balance}")
            if option == 5:
                balance = 20000
                withdraw=int(input("Enter withdraw amount : "))
                withdraw_amount = balance - withdraw
                deposited = int(input("Enter deposited amount : "))
                deposited_amount = balance+deposited
                print(f"withdraw amount is {withdraw_amount}")
                print(f"credited amount is {deposited_amount}")
                print("------------------------------------------------")
                print("------------------------------------------------")
            else:
                print(f"Your account current balance is :{balance}")
        elif option == 6: 
            print("Exit")
            print("------------------------------------------------")
            print("------------------------------------------------")
            break
        else:
            break
            
else:
    print("Wrong pin entered!!! please try again")
