def deposit(current_balance):
    dep_amount=int(input("Enter the Deposit amount: "))
    total_balance = current_balance+dep_amount
    return total_balance

def withdraw(current_balance):
    with_amount = int(input("Enter the withdraw amount: "))
    if current_balance-with_amount<0:
        print("Insufficient Balance!")
        total_balance=current_balance
    else:
        total_balance = current_balance-with_amount
    
    return total_balance

def balance_check(current_balance):
    print(f"Your current balance is {current_balance}")
    
    
    