balance=5000
print("Welcome to the ATM")
operation= input("Choose operation: 'Withdraw' or 'Check Balance': ").lower()
if operation == "withdraw":
    amount= float(input("Enter amount to withdraw: "))
    if amount <= balance:
        balance-=amount
        print(f"Withdrawal successful. Remaining balance: ${balance:.2f}")
    else:
        print("Insufficient Balance.")
elif operation == "check balance" :
    print(f"Your current balance: ${balance:.2f}")
else:
    print("Invalid operation selected.")
