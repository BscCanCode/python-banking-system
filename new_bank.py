database = {}
def main():
    result = cr_acc()
    if result is not None:
        account, password = result
        balance = 0 #at openeing balance is 0
        database[account] = [password, balance]
        print(f"The account {account} with password: {password} is created successfully!")
        transaction(account)
    else:
        print("Credentials are incorrent, try again!")

def cr_acc():
    account = int(input("Create your 8 digit account number: "))
    password = int(input("Enter your password: "))
    if len(str(account)) < 8 or len(str(password)) < 4:
        return None
    else:
        return account, password  

def transaction(account):
    while True:
        choice = int(input("Enter the choice \n1.withdraw\n2.deposit\n3.check_balance\n4.exit:"))
        if choice == 1:
            acc_num = int(input("Enter your account number: "))
            password = int(input("Enter your password: "))
            if acc_num == account and password == database[account][0]:
                amount = int(input("Enter the amount to withdraw: "))
                if amount < database[account][1]:
                    database[account][1]-=amount
                    print(f"Amount {amount} withdrawn successfully from the account {account} successfully")
                else:
                    print("not enough balance in your account!")
            else:
                print("checl account number or password and try again!")
        elif choice == 2:
            accc_num = int(input("Enter the account number: "))
            passs = int(input("Enter the password: "))
            if accc_num == account and passs == database[account][0]:
                deposit = int(input("Enter the amount to deposit: "))
                print(f"Amount {deposit} is deposited in the account {account} successfully!")
                database[account][1]+=deposit
            else:
                print("Account number and passowrd check and try again!")
        elif choice == 3:
            accc_nums = int(input("Enter the account number: "))
            passss = int(input("Enter the password: "))
            if accc_nums == account and passss == database[account][0]:
                print(f"your balance for account_num {account} is {database[account][1]}")
            else:
                print("Check account_number and password and try again!")
        elif choice == 4:
            print("Exit is done")
            exit()

if __name__ == "__main__":
    main()     