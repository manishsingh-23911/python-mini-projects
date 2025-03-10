print("Welcome to the simple ATM Simulator")

balance = 1000

user_pin = '1234' # using numbers in a string in this case helps to avoid converting int. to string later on

entered_pin = input("PLease enter your PIN: ")

if entered_pin != user_pin:
     print("Invalid PIN. Exiting.")
     atm_on = False
else:
    atm_on = True

while atm_on:
    print("Main Menu:")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Enter your Choice: ")


    if choice == '1':
        print("Your current balance is $" + str(balance))

    elif choice == '2':
        amount = float(input("Enter the amount to deposit: $"))
        balance += amount
        print("$" + str(amount) + "deposited successfully.")
    elif choice == '3':
        amount = float(input("Enter the amount to withdraw: $"))
        if amount > balance:
            print("Insufficient Balance!")
        else:
            balance -= amount
            print("$" + str(balance) + "withdrawn successfully.")

    elif choice =='4':
        print("Thank you for using the ATM. Goodbye!")
        atm_on = False

    else:
        print("Invalid choice. PLease try again.")