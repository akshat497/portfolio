import datetime
import json
accounts={}
def createAccount():
    Name=input("enter your name")
    Age=input("enter your age")
    aadhar=input("enter your aadhar card number")
    PAN=input("enter your PAN card number")
    Phone=input("enter your Phone number")
    account_number=str(datetime.date.today())+str(datetime.datetime.now().second)
    details={
        "account_number":account_number,
        "name":Name,
        "age":Age,
        "aadhar_card_number":aadhar,
        "pan_card_number":PAN,
        "phone_number":Phone,
        "balance":0
    }
    accounts[Phone]=details
    print(accounts)
    file=open("accounts.json","w")
    json.dump(accounts,file,indent=4)
    print("Account created successfully")
  
  
def DepositMoney():
    Phone=input("enter your phone number")
    file=open("accounts.json","r")
    print(file)
    accounts = json.load(file)
    if Phone not in accounts:
        print("your account does not exist")
        return
    money=float(input("enter how much money u want to deposit"))
    accounts[Phone]["balance"]+=money

    print(accounts[Phone]['balance'],accounts)
    
    Newfile=open("accounts.json","w")
    json.dump(accounts,Newfile,indent=4)
    print("Money deposited successfully")  

def WidrawMoney():
    Phone=input("enter your phone number")
    file=open("accounts.json","r")
    print(file)
    accounts = json.load(file)
    if Phone not in accounts:
        print("your account does not exist")
        return
    money=float(input("enter how much money u want to widraw"))
    if money>accounts[Phone]["balance"]:
        print("insufficiant balance")
        return
    
    accounts[Phone]["balance"]-=money

    print(accounts[Phone]['balance'],accounts)
    
    Newfile=open("accounts.json","w")
    json.dump(accounts,Newfile,indent=4)
    print("Money deposited successfully") 
    print("Widrwal successfull")  


def CheckBalance():
    Phone=input("enter your phone number")
    file=open("accounts.json","r")

    accounts=json.load(file)

    print("your account balance is" ,accounts[Phone]['balance'])
    

while(True):
    print("1 to create bank account")
    print("2 Deposit money")
    print("3 Widraw money")
    print("4 Account balance")
    print("5 Exit")

    choice=int(input("enter your choice"))

    if(choice==1):
        createAccount()
    elif(choice==2):
        DepositMoney()
    elif(choice==3):
        WidrawMoney()
    elif(choice==4):
        CheckBalance()
    elif(choice==5):
        break 