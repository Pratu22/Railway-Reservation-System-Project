from pickle import dump, load
import time
import random
import os
class Ticket:
    def __init__(self):
        self.no_ofac1stclass = 0
        self.totaf = 0
        self.no_ofac2ndclass = 0
        self.no_ofac3rdclass = 0
        self.no_ofsleeper = 0
        self.no_oftickets = 0
        self.name = ""
        self.age = 0
        self.resno = 0
        self.status = ""

    def ret(self):
        return self.resno

    def retname(self):
        return self.name

    def display(self):
        f = 0
        fin1 = open("tickets.dat", "rb")
        if not fin1:
            print("ERROR")
        else:
            print()
            n = int(input("ENTER PNR NUMBER:"))
            print("\n\n")
            print("FETCHING DATA...".center(80))
            time.sleep(1)
            print("PLEASE WAIT...!!".center(80))
            time.sleep(1)
            os.system('cls')
        try:
            while True:
                tick = load(fin1)
                if n == tick.ret():
                    f = 1
                    print("=" * 80)
                    print("PASSENGER'S NAME:", tick.name)
                    print("PASSENGER'S AGE:", tick.age)
                    print("PNR NO:", tick.resno)
                    print("STATUS:", tick.status)
                    print("NO OF SEATS BOOKED:", tick.no_oftickets)
                    print("=" * 80)
        except:
            pass
            fin1.close()
            if f == 0:
                print("WRONG PNR NUMBER..!!")

    def pending(self):
        self.status = "WAITING LIST"
        print("PNR NUMBER:", self.resno)
        print("STATUS=", self.status)

    def cancellation(self):
        z = 0
        f = 0
        fin = open("tickets.dat", "rb")
        fout = open("temp.dat", "ab")
        print()
        r = int(input("ENTER PNR NUMBER:"))
        try:
            while True:
                tick = load(fin)
                z = tick.ret()
                if z != r:
                    dump(tick, fout)
                elif z == r:
                    f = 1
        except:
            pass
            fin.close()
            fout.close()
            os.remove("tickets.dat")
            os.rename("temp.dat", "tickets.dat")
            if f == 0:
                print("NO SUCH RESERVATION NUMBER FOUND")
            else:
                print("TICKET CANCELLED")

    def reservation(self):
        trainno = int(input("ENTER THE TRAIN NO:"))
        z = 0
        f = 0
        fin2 = open("trdetails.dat", "rb")
        fin2.seek(0)
        if not fin2:
            print("ERROR")
        else:
            try:
                while True:
                    tr = load(fin2)
                    z = tr.gettrainno()
                    n = tr.gettrainname()
                    if trainno == z:
                        print("TRAIN NAME IS:", n)
                        f = 1
                        print("-" * 80)
                        no_ofac1st = tr.getno_ofac1stclass()
                        no_ofac2nd = tr.getno_ofac2ndclass()
                        no_ofac3rd = tr.getno_ofac3rdclass()
                        no_ofsleeper = tr.getno_ofsleeper()
                        if f == 1:
                            fout1 = open("tickets.dat", "ab")
                            self.name = input("ENTER THE PASSENGER'S NAME:")
                            self.age = int(input("PASSENGER'S AGE:"))
                            print("\t\t SELECT A CLASS YOU WOULD LIKE TO TRAVEL IN:-")
                            print("1. AC FIRST CLASS")
                            print("2. AC SECOND CLASS")
                            print("3. AC THIRD CLASS")
                            print("4. SLEEPER CLASS")
                            c = int(input("\t\t\tENTER YOUR CHOICE:"))
                            os.system('cls')
                            amt1 = 0
                            if c == 1:
                                self.no_oftickets = int(input("ENTER NO_OF FIRST CLASS AC SEATS TO BE BOOKED:"))
                                i = 1
                                print("PROCESSING..", time.sleep(0.5))
                                print(".", time.sleep(0.3))
                                print(".")
                                time.sleep(2)
                                os.system('cls')
                                print("TOTAL AMOUNT TO BE PAID=", amt1)
                                self.resno = random.randint(1000, 2546)
                                x = no_ofac1st - self.totaf
                                if x > 0:
                                    self.confirmation()
                                    dump(self, fout1)
                                    break
                                else:
                                    self.pending()
                                    dump(tick, fout1)
                                    break
                            elif c == 2:
                                self.no_oftickets = int(input("ENTER NO_OF SECOND CLASS AC SEATS TO BE BOOKED:"))
                                i = 1
                                while i <= self.no_oftickets:
                                    self.totaf += 1
                                    amt1 = 900 * self.no_oftickets
                                    i += 1
                                    print("PROCESSING..", time.sleep(0.5))
                                    print(".", time.sleep(0.3))
                                    print(".")
                                    time.sleep(2)
                                    os.system('cls')
                                    print("TOTAL AMOUNT TO BE PAID=", amt1)
                                    self.resno = random.randint(1000, 2546)
                                x = no_ofac2nd - self.totaf
                                if x > 0:
                                    self.confirmation()
                                    dump(self, fout1)
                                    break
                                else:
                                    self.pending()
                                    dump(tick, fout1)
                                    break
                            elif c == 3:
                                self.no_oftickets = int(input("ENTER NO_OF THIRD CLASS AC SEATS TO BE BOOKED:"))
                                i = 1
                                while i <= self.no_oftickets:
                                    self.totaf += 1
                                    amt1 = 800 * self.no_oftickets
                                    i += 1
                                    print("PROCESSING..", time.sleep(0.5))
                                    print(".", time.sleep(0.3))
                                    print(".")
                                    time.sleep(2)
                                    os.system('cls')
                                    print("TOTAL AMOUNT TO BE PAID=", amt1)
                                    self.resno = random.randint(1000, 2546)
                                x = no_ofac3rd - self.totaf
                                if x > 0:
                                    self.confirmation()
                                    dump(self, fout1)
                                    break
                                else:
                                    self.pending()
                                    dump(tick, fout1)
                                    break
                            elif c == 4:
                                self.no_oftickets = int(input("ENTER NO_OF SLEEPER CLASS SEATS TO BE BOOKED:"))
                                i = 1
                                while i <= self.no_oftickets:
                                    self.totaf += 1
                                    amt1 = 550 * self.no_oftickets
                                    i += 1
                                    print("PROCESSING..", time.sleep(0.5))
                                    print(".", time.sleep(0.3))
                                    print(".")
                                    time.sleep(2)
                                    os.system('cls')
                                    print("TOTAL AMOUNT TO BE PAID=", amt1)
                                    self.resno = random.randint(1000, 2546)
                                x = no_ofsleeper - self.totaf
                                if x > 0:
                                    self.confirmation()
                                    dump(self, fout1)
                                    break
                                else:
                                    self.pending()
                                    dump(tick, fout1)
                                    break
            except:
                pass
                if f == 0:
                    time.sleep(2)
                    print("\n\n\n\n\n\n\t\t\t\t NO SUCH TRAINS FOUND!!")
                    time.sleep(2)

    def confirmation(self):
        self.status = "CONFIRMED"
        print("PNR NUMBER:", self.resno)
        print("STATUS=", self.status)
        
tick = Ticket()
