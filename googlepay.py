class gpay: 
    def __init__(self):
        print("GPAY")
        
        
    def check_name(self):
        self.__uname = input("Enter name : ")
        if type(self.__uname) == str:
            print(self.__uname,)
            print("Name verified  \n")
        else:
            raise TypeError("Invalid name")
        
    def check_mnumber(self):
        self.__unumber = input("Mobile Number : ")
        if type(self.__unumber)==str:
            if len(self.__unumber)==10:
                print(self.__unumber,)
                print("Mobile number verified \n")
            else:
                raise TypeError("Check your mobile number : ")
        else:
            raise ValueError("Invalid Type")
        
    def check_mail(self):
        self.__umailid = input("Mail ID :")
        if type(self.__umailid) == str:
            if len(self.__umailid) <35:
                print(self.__umailid)
                print("Email id verified \n")
            else:
                raise TypeError("check your Emailid")
        else:
            raise ValueError("Invalid Email Address")
        
    def check_upi(self):
        self.__upi = input("Enter upi id :")
        if type(self.__upi) == str:
            if len(self.__upi) <16:
                print(self.__upi)
                print("Upi id verified \n")
                print("verified your account \n")
            else:
                raise TypeError("check your Upi")
        else:
            raise ValueError("Invalid upi")
        
class bank(gpay):
    def __init__(self):
        print("bank account details")
        
    def check_bank(self):
        self.ubank = input("Bank")
        self.uaccno = input("Account number")
        if len (self.uaccno) <=17:
            print("Verified account number")
        else:
            raise TypeError("Check bank account number")
        
    def pin_creation(self):
        self.pin = input("Set up a 4 digit upi pin ")
        if len(self.pin) == 4:
            self.repin = input("re enter pin")
            if self.pin==self.repin:
                print("Pin Setup...")
            else:
                raise TypeError("Incorrect pin ")
        else:
            print("Re-enter 4 digit pin")
            
class userdata(bank):
    def __init__(self):
            self.alldata=[self.__uname,self.__unumber,self.__umailid,self.__upi,self.ubank,self.uaccnos,elf.pin]
            print(self.alldata)
            
class payment(bank):
    def __init__(self):
        print("Payment....")
        
    def reciver_data(self,ifsc):
        self.__rname = input("Reciver's Name")
        if type(self.__rname) == str:
                self.__ifsccode = ifsc
                print (ifsc)
                if len(self.__ifsccode) == 11:

                    print("IFSC CODE verified")
                else:
                    raise ValueError("Inalid IFSC code")
        else:
            raise TypeError("Invalid Type Name")

    def transcaction(self):
            self.__raccno = input(" Reciver's Account number")
            if len (self.__raccno) <=17:
                    self.__reaccno1=input(" Re-Enter Reciver's Account number")
                    if self.__reaccno1 == self.__raccno:
                           print("Account verified")
                    else:
                         raise ValueError("Account mismatched Try again")
            else:
                raise ValueError("maximum limit crossed ")
            
    def e(self):
            self.amount = input("Enter amount: ")
            self.pin = input("4 digit pin: ")
            if self.pin == "8015":
                print("Transcaction sucess \n you earned a new scratch card")
            else:
                print("Incorect pin try again")
                
user = gpay()
user.check_name()
user.check_mnumber()
user.check_mail()
user.check_upi()
user1=bank()
user1.check_bank()
user1.pin_creation()
user3 = payment()
user3.reciver_data("SBIN0000921")
user3.transcaction()
user3.e()

