import pickle 
import os 
import pathlib 

class Account: 
    def __init__(self, accNo=0, name='', accType='', deposit=0): 
        self.accNo = accNo 
        self.name = name 
        self.type = accType 
        self.deposit = deposit 

    def createAccount(self): 
        self.accNo = int(input("Enter the account number: ")) 
        self.name = input("Enter the account holder name: ") 
        self.type = input("Enter the type of account (C/S): ") 
        self.deposit = int(input("Enter the initial deposit (>=500 for Savings and >=1000 for Current): ")) 

    def modifyAccount(self): 
        print("Account Number: ", self.accNo) 
        self.name = input("Modify Account Holder Name: ") 
        self.type = input("Modify type of Account: ") 
        self.deposit = int(input("Modify Balance: ")) 

    def depositAmount(self, amount): 
        self.deposit += amount 

    def withdrawAmount(self, amount): 
        self.deposit -= amount 

    def report(self): 
        print(self.accNo, " ", self.name, " ", self.type, " ", self.deposit) 

    def getAccountNo(self): 
        return self.accNo 

    def getAccountHolderName(self): 
        return self.name 

    def getAccountType(self): 
        return self.type 

    def getDeposit(self): 
        return self.deposit 

def intro(): 
    print("\t\t\t\t**********************") 
    print("\t\t\t\tBANK MANAGEMENT SYSTEM") 
    print("\t\t\t\t**********************") 
    input("Press Enter to continue...") 

def writeAccount(): 
    account = Account() 
    account.createAccount() 
    writeAccountsFile(account) 

def displayAll(): 
    file = pathlib.Path("accounts.data") 
    if file.exists(): 
        infile = open('accounts.data', 'rb') 
        mylist = pickle.load(infile) 
        for item in mylist: 
            print(item.accNo, " ", item.name, " ", item.type, " ", item.deposit) 
        infile.close() 
    else: 
        print("No records to display") 

def displaySp(num): 
    file = pathlib.Path("accounts.data") 
    if file.exists(): 
        infile = open('accounts.data', 'rb') 
        mylist = pickle.load(infile) 
        infile.close() 
        found = False 
        for item in mylist: 
            if item.accNo == num: 
                print("Your account Balance is =", item.deposit) 
                found = True 
                break 
        if not found: 
            print("No existing record with this number") 
    else: 
        print("No records to Search") 

def depositAndWithdraw(num1, num2): 
    file = pathlib.Path("accounts.data") 
    if file.exists(): 
        infile = open('accounts.data', 'rb') 
        mylist = pickle.load(infile) 
        infile.close() 
        os.remove('accounts.data') 
        for item in mylist: 
            if item.accNo == num1: 
                if num2 == 1: 
                    amount = int(input("Enter the amount to deposit: ")) 
                    item.depositAmount(amount) 
                    print("Your account has been updated") 
                elif num2 == 2: 
                    amount = int(input("Enter the amount to withdraw: ")) 
                    if amount <= item.deposit: 
                        item.withdrawAmount(amount) 
                        print("Your account has been updated") 
                    else: 
                        print("You cannot withdraw a larger amount") 
        outfile = open('newaccounts.data', 'wb') 
        pickle.dump(mylist, outfile) 
        outfile.close() 
        os.rename('newaccounts.data', 'accounts.data') 
    else: 
        print("No records to Search") 

def deleteAccount(num): 
    file = pathlib.Path("accounts.data") 
    if file.exists(): 
        infile = open('accounts.data', 'rb') 
        oldlist = pickle.load(infile) 
        infile.close() 
        newlist = [item for item in oldlist if item.accNo != num] 
        os.remove('accounts.data') 
        outfile = open('newaccounts.data', 'wb') 
        pickle.dump(newlist, outfile) 
        outfile.close() 
        os.rename('newaccounts.data', 'accounts.data') 
        print("Account deleted") 
    else: 
        print("No records to Search") 

def modifyAccount(num): 
    file = pathlib.Path("accounts.data") 
    if file.exists(): 
        infile = open('accounts.data', 'rb') 
        oldlist = pickle.load(infile) 
        infile.close() 
        os.remove('accounts.data') 
        for item in oldlist: 
            if item.accNo == num: 
                item.modifyAccount() 
        outfile = open('newaccounts.data', 'wb') 
        pickle.dump(oldlist, outfile) 
        outfile.close() 
        os.rename('newaccounts.data', 'accounts.data') 
    else: 
        print("No records to Search") 

def writeAccountsFile(account): 
    file = pathlib.Path("accounts.data") 
    if file.exists(): 
        infile = open('accounts.data', 'rb') 
        oldlist = pickle.load(infile) 
        oldlist.append(account) 
        infile.close() 
        os.remove('accounts.data') 
    else: 
        oldlist = [account] 
    outfile = open('newaccounts.data', 'wb') 
    pickle.dump(oldlist, outfile) 
    outfile.close() 
    os.rename('newaccounts.data', 'accounts.data') 

# Start of the program 
intro() 

ch = '' 
while ch != '8': 
    print("\tMAIN MENU") 
    print("\t1. NEW ACCOUNT") 
    print("\t2. DEPOSIT AMOUNT") 
    print("\t3. WITHDRAW AMOUNT") 
    print("\t4. BALANCE ENQUIRY") 
    print("\t5. ALL ACCOUNT HOLDER LIST") 
    print("\t6. CLOSE AN ACCOUNT") 
    print("\t7. MODIFY AN ACCOUNT") 
    print("\t8. EXIT") 
    print("\tSelect Your Option (1-8): ", end='') 
    ch = input().strip() 
    if ch == '1': 
        writeAccount() 
    elif ch == '2': 
        num = int(input("\tEnter The account No.: ")) 
        depositAndWithdraw(num, 1) 
    elif ch == '3': 
        num = int(input("\tEnter The account No.: ")) 
        depositAndWithdraw(num, 2) 
    elif ch == '4': 
        num = int(input("\tEnter The account No.: ")) 
        displaySp(num) 
    elif ch == '5': 
        displayAll() 
    elif ch == '6': 
        num = int(input("\tEnter The account No.: ")) 
        deleteAccount(num) 
    elif ch == '7': 
        num = int(input("\tEnter The account No.: ")) 
        modifyAccount(num) 
    elif ch == '8': 
        print("\tThanks for using the bank management system") 
        break 
    else: 
        print("Invalid choice") 
