import time
import getpass

filename="accounts.txt"
accounts={}
logged_in=False
session_active=True
atm_running=True

def load(file):
    for i in file:
        i=i.strip()
        if i!="":
            i=i.split(',')
            accounts[i[0]]={"pin":i[1],"balance":float(i[2])}
def save():
    with open (filename,"w") as f:
        for i in accounts:
            p=accounts[i]["pin"]
            b=accounts[i]["balance"]
            f.write(f"{i},{p},{b}\n")
def init():
    with open(filename,"w") as f:
        f.write(f"1001,2121,10000\n1002,1234,100000")
        with open(filename, "r") as f:
            load(f)

if __name__=="__main__":
    try:
        with open(filename, "r") as f:
            load(f)

    except FileNotFoundError:
        init()
        
                
    print("WELCOME TO THE ATM!")

    while atm_running==True:
        hch=input("WHAT WOULD YOU LIKE TO DO?\nCREATE ACCOUNT (1)\nLOGIN (2)\nDELETE ACCOUNT (3)\nEXIT (4)\nENTER YOUR CHOICE:")
        if hch=="1":
            naccp=input("ENTER ACCOUNT PIN:")
            id=0
            for i in accounts.keys():
                if int(i)>id:
                    id=int(i)
            if id==0:
                id=1000
            accounts[str(id+1)]={"pin":naccp,"balance":0}
            print("YOUR ACCOUNT NUMBER IS:",id+1)
            save()
            

        elif hch=="2":
            logged_in=False
            accn=input("ENTER ACCOUNT NUMBER:")
            pin=getpass.getpass("ENTER PIN:")
            

            if accn in accounts and accounts[accn]["pin"]==pin:
                print("LOGIN SUCCESSFUL")
                logged_in=True
                session_active=True
            else:
                print("INVALID CREDENTIALS")
            if logged_in==True:
                while session_active==True:
                    print("\n\n\n\nWHAT WOULD YOU LIKE TO DO?\nCHECK BALANCE (1)\nDEPOSIT CASH (2)\nWITHDRAW CASH (3)\nCHANGE PIN(4)\nTRANSFER MONEY(5)\nEXIT(6)")
                    time.sleep(1)
                    ch=input("ENTER CHOICE:")
                    if ch=="1":
                        print(accounts[accn]["balance"])
                        time.sleep(1)
                    elif ch=="2":
                        try:
                            dp=float(input("AMOUNT TO DEPOSIT:"))
                            if dp<0:
                                print("INVALID INPUT!")
                            else:
                                accounts[accn]["balance"]=(accounts[accn]["balance"]+dp)
                                time.sleep(1)
                                save()
                        except ValueError:
                            print("Invalid Input!")
                    elif ch=="3":
                        try:
                            wi=float(input("AMOUNT TO WITHDRAW:"))
                            if wi<0:
                                print("INVALID INPUT!")
                            else:
                                if wi>accounts[accn]["balance"]:
                                    print("INSUFFICIENT FUNDS")
                                else:
                                    accounts[accn]["balance"]=(accounts[accn]["balance"]-wi)
                                    time.sleep(1)
                                    save()
                            
                        except ValueError:
                            print("Invalid Input!")
                    elif ch=="4":
                        np=input("ENTER NEW PIN:")
                        accounts[accn]["pin"]=np
                        time.sleep(1)
                        save()
                    elif ch=="5":
                        try:
                            tacc=input("ENTER ACCOUNT TO TRANSFER:")
                            if tacc in accounts:
                                tam=float(input("ENTER AMOUNT TO TRANSFER:"))
                                if tam>accounts[accn]["balance"]:
                                    print("INSUFFICIENT FUNDS!")
                                else:
                                    accounts[tacc]["balance"]+=tam
                                    accounts[accn]["balance"]-=tam
                                    save()
                            else:
                                print("ACCOUNT NOT FOUND")
                        except ValueError:
                            print("Invalid Input!")
                        
                    elif ch=="6":
                        print("Exiting...")
                        logged_in=False
                        session_active=False
                        

                    else:
                        print("INVALID INPUT!")
        elif hch=="3":
            dacc=input("ENTER ACCOUNT NO TO DELETE:")
            dpin=getpass.getpass("ENTER ACCOUNT PIN TO DELETE:")
            if dacc in accounts and accounts[dacc]["pin"]==dpin:
                accounts.pop(dacc)
                print(f"ACCOUNT NO {dacc} DELETED SUCCESSFULLY")
                save()
            else:
                print("INVALID ACCOUNT/PIN")
        elif hch=="4":
            atm_running=False
            print("Exiting..")            






                
