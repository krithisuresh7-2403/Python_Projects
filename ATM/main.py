from operations import deposit, withdraw, balance_check

def operation(user_action, bank_balance):
    if user_action=="deposit" or user_action=="d":
        total_balance = deposit(bank_balance)
        return total_balance
    
    elif user_action=="withdraw" or user_action=="w":
        total_balance= withdraw(bank_balance)
        return total_balance
        
    elif user_action=="balance" or user_action=="b":
        balance_check(bank_balance)
        return bank_balance
    
def pin_check(user_pin, pin_input):
    if user_pin == pin_input:
        return True
    else:
        return False
    
    
if __name__ == "__main__":
    
    user_pin = "12345"
    bank_balance = 10000
    proceed = True
    
    while proceed:
        
        pin_inp = input("Enter your pin: ")
        if pin_check(user_pin, pin_inp):
            user_action = input("Do you want to Deposit/Withdraw/Check Balance? ").lower()
            bank_balance =operation(user_action,bank_balance)
            next_action= input("Do you want to continue? y/n ").lower()
            if next_action=="y":
                proceed = True
            else:
                proceed = False    
        else:
            print("Wrong PIN! Please Enter the right pin")
            proceed = False