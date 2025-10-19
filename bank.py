import random

class Bank:
    Holder_Details = []

    def create_new_Account(self):
        print('*** Welcome to Union Bank ***')
        new_Holder = {}

        # Holder basic details
        new_Holder['Holder_Name'] = input('Enter Holder name: ').strip()
        while True:
            aadhar = input('Enter Aadhar number (12 digits): ').strip()
            if aadhar.isdigit() and len(aadhar) == 12:
                new_Holder['Aadhar_Number'] = aadhar
                break
            else:
                print("Invalid Aadhar number! Enter 12 digits.")

        while True:
            mobile = input('Enter Mobile number (10 digits): ').strip()
            if mobile.isdigit() and len(mobile) == 10:
                new_Holder['Mobile'] = mobile
                break
            else:
                print("Invalid Mobile number! Enter 10 digits.")

        new_Holder['IFSCCODE'] = 'IFSC05235'
        new_Holder['Account_Number'] = random.randint(1111111111, 9999999999)

        # Account type and initial deposit
        Type_of_Acc = input('Select Account Type Saving/Zero: ').strip().lower()
        while True:
            if Type_of_Acc in ['saving', 'savings']:
                print('Your Account is Saving. You have to deposit at least 500 rupees.')
                try:
                    s_acc = int(input('Deposit amount: '))
                    if s_acc >= 500:
                        new_Holder['Sufficient_Balance'] = s_acc
                        break
                    else:
                        print('Deposit at least 500 rupees.')
                except:
                    print("Enter a valid number!")
            elif Type_of_Acc in ['zero']:
                print('Your Account is Zero. You have to deposit at least 100 rupees.')
                try:
                    s_acc = int(input('Deposit amount: '))
                    if s_acc >= 100:
                        new_Holder['Sufficient_Balance'] = s_acc
                        break
                    else:
                        print('Deposit at least 100 rupees.')
                except:
                    print("Enter a valid number!")
            else:
                Type_of_Acc = input('Invalid input! Select Account Type Saving/Zero: ').strip().lower()

        new_Holder['Account_Type'] = 'Saving' if Type_of_Acc in ['saving','savings'] else 'Zero'

        Bank.Holder_Details.append(new_Holder)
        print("\nAccount created successfully!")
        print(f"Account Number: {new_Holder['Account_Number']}")
        print(f"Holder Name   : {new_Holder['Holder_Name']}")
        print(f"Account Type  : {new_Holder['Account_Type']}")
        print(f"Balance       : {new_Holder['Sufficient_Balance']}")
        print("-"*40)

    def Deposit(self):
        print('*** Welcome to Deposit option ***')
        name = input('Enter Holder name: ').strip()
        try:
            acc = int(input('Enter Account Number: '))
            amount = int(input('Enter Deposit amount: '))
        except:
            print("Invalid input! Enter numbers only.")
            return

        for x in Bank.Holder_Details:
            if x['Holder_Name'] == name and x['Account_Number'] == acc:
                x['Sufficient_Balance'] += amount
                print(f"Deposit successful! New Balance: {x['Sufficient_Balance']}")
                break
        else:
            print("Account not found.")

    def Withdraw(self):
        print('*** Welcome to Withdraw option ***')
        name = input('Enter Holder name: ').strip()
        try:
            acc = int(input('Enter Account Number: '))
            amount = int(input('Enter amount to withdraw: '))
        except:
            print("Invalid input! Enter numbers only.")
            return

        for x in Bank.Holder_Details:
            if x['Holder_Name'] == name and x['Account_Number'] == acc:
                if x['Sufficient_Balance'] >= amount:
                    x['Sufficient_Balance'] -= amount
                    print(f"Withdrawal successful! Remaining Balance: {x['Sufficient_Balance']}")
                else:
                    print("Insufficient balance.")
                break
        else:
            print("Account not found.")

    def Details(self):
        name = input('Enter Holder name: ').strip()
        try:
            acc = int(input('Enter Account Number: '))
        except:
            print("Invalid input!")
            return

        for x in Bank.Holder_Details:
            if x['Holder_Name'] == name and x['Account_Number'] == acc:
                print("\n--- Account Details ---")
                for k,v in x.items():
                    print(f"{k} ==> {v}")
                print("-"*40)
                break
        else:
            print("Account not found.")

    def Check_Balance(self):
        name = input('Enter Holder name: ').strip()
        try:
            acc = int(input('Enter Account Number: '))
        except:
            print("Invalid input!")
            return

        for x in Bank.Holder_Details:
            if x['Holder_Name'] == name and x['Account_Number'] == acc:
                print(f"Balance ==> {x['Sufficient_Balance']}")
                break
        else:
            print("Account not found.")


# ----- Main Menu -----
obj = Bank()

while True:
    print('''\n----- Bank Menu -----
1) Create New Account
2) Deposit
3) Withdraw
4) Account Details
5) Check Balance
6) Exit''')

    choice = input("Choose an option (1-6): ").strip()
    if choice == '1':
        obj.create_new_Account()
    elif choice == '2':
        obj.Deposit()
    elif choice == '3':
        obj.Withdraw()
    elif choice == '4':
        obj.Details()
    elif choice == '5':
        obj.Check_Balance()
    elif choice == '6':
        print("Thank you for using the banking system.")
        break
    else:
        print("Invalid option. Please choose between 1 to 6.")