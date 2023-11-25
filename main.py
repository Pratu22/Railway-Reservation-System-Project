from pickle import load
from pickle import dump
import time
import os
from tickets import *
from trains import *
def menu():
    tr = Train()
    tick = Ticket()
    print
    print("WELCOME TO INDIAN RAILWAYS".center(80)) 
    while True:
        print
        print("=" * 80)
        print("\t\t\t\t RAILWAY")
        print
        print("=" * 80)
        print
        print("\t\t\t1. ADD TRAINS *Only For Admins*") #admin password is password
        print
        print("\t\t\t2. TRAIN DETAILS.")
        print
        print("\t\t\t3. RESERVATION OF TICKETS.")
        print
        print("\t\t\t4. CANCELLATION OF TICKETS.")
        print
        print("\t\t\t5. DISPLAY PNR STATUS.")
        print
        print("\t\t\t6. QUIT.")
        print("-" * 80)
        ch = int(input("\t\t\t ENTER YOUR CHOICE :"))
        os.system("cls")
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\nLoading please wait", time.sleep(1))
        print(".", time.sleep(0.5))
        print(".", time.sleep(2))
        os.system("cls")

        if ch == 1: #if 1 selected
            j = "password" #default admin password change according to yourself
            r = input("\n\n\n\n\n\n\n\n\n\n\n\t\t\t\tENTER THE PASSWORD: ")
            os.system("cls")
            if j == r:
                x = "y"
                while x.lower() == "y":
                    fout = open("trdetails.dat", "ab")
                    tr.getinput()
                    dump(tr, fout)
                    fout.close()
                    print(
                        "\n\n\n\n\n\n\n\n\n\n\n\t\t\t UPDATING TRAIN LIST PLEASE Wait",
                        time.sleep(1),
                    )
                    print(("."), time.sleep(0.5))
                    print(("."), time.sleep(2))
                    os.system("cls")
                    print("\n\n\n\n\n\n")
                    x = input("\t\t DO YOU WANT TO ADD ANY MORE TRAINS DETAILS ?")
                    os.system("cls")
                    continue
            elif j != r:
                print("\n\n\n\n\n")
                print("Wrong Password".center(80))
        elif ch == 2: #if 2 Selected
            fin = open("trdetails.dat", "rb")
            if not fin:
                print("ERROR")
            else:
                try:
                    while True:
                        print("*" * 80)
                        print("\t\t\t\tTRAIN DETAILS")
                        print("*" * 80)
                        print
                        tr = load(fin)
                        tr.output()
                        input("PRESS ENTER TO VIEW NEXT TRAIN DETAILS")
                        os.system("cls")
                except:
                    pass
        elif ch == 3: 
            print("=" * 80)
            print("\t\t\t\tRESERVATION OF TICKETS")
            print("=" * 80)
            print
            tick.reservation()
        elif ch == 4:
            print("=" * 80)
            print("\t\t\t\tCANCELLATION OF TICKETS")
            print("=" * 80)
            print
            tick.cancellation()
        elif ch == 5:
            print("=" * 80)
            print("PNR STATUS".center(80))
            print("=" * 80)
            print
            tick.display()
        elif ch == 6:
            os.system("cls")
            print("\t\t\t\t\n\n\n\n\n\t THANK YOU FOR USING RAILWAY RESERVATION SYSTEM ..... ")
            print("\n\t\t\tCREATED BY : ")
            print("\t\t\t\t PRATHAMESH RAHATE")
            print("\t\t\t\t TECHOTAKU ;)")
            print("\t\t\t\t PEACE ")
            print("\n\n\n\n\n\n\n\n\n\n\t\t\t\t\tEXITING")
            time.sleep(3)
            print(".")
            time.sleep(0.5)
            os.system("cls")
            quit()


menu()
