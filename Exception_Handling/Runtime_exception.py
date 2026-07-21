try :
   a = 9
   s = '5'
   print(a+s)
except Exception as e :
   print(type(e))
   print(e.with_traceback)

try :
   s = '9e'
   a = int(s)
except Exception as e :
   print(type(e))
   print(e.with_traceback)

try :
   s = '9e'
   print(u)
except NameError as e :
   print(type(e))
   print(e.with_traceback)


try :
   li = [8,9,8,5,7]
   #print(li[9])
   #print(li[1]/0)
   print(78/"ji")
except IndexError as e :
   print(e.with_traceback)
except ZeroDivisionError as e :
   print(e.with_traceback)
except Exception as e :
   print (e.with_traceback)



#raise exception through Exception class and custom message . and also through user defined exception class
#custom exception class should be inherited from Exception class, and it is used for extra flexibility and to provide more specific error messages.

class SavingsAccount :
   def __init__(self,Joining_deposit,Account_no) :
      self.__total_balance = Joining_deposit
      self.__Account_no = Account_no
   
   def deposit(self,amount) :
      self.__total_balance += amount
      print(f"{amount} successfully credited to {self.__Account_no}")
   
   def withdraw(self,amount) :
      if self.__total_balance < amount :
         raise Exception("You don't have enough money in you bank")
      self.__total_balance -= amount
      print(f"{amount} successfully debited from {self.__Account_no}")
   
   def show_account_balance(self) :
      print(f"Your current balance is {self.__total_balance}")

account1 = SavingsAccount(50000,'39966783289')

account1.deposit(7000)
 
try :
   account1.withdraw(40000)
except Exception as e :
   print(e.args[0])
else :
   account1.show_account_balance()

try :
   account1.withdraw(40000)
except Exception as e :
   print(e.args[0])
else :
   account1.show_account_balance()


class Security_Error(Exception) :
    def __init__(self,exception_text) :
       super().__init__(exception_text)
    
    def logout(self) :
       print("logout from all devices")
             
class Google_employee :
   def __init__(self,employee_id,password,login_device):
      self.__employee_id = employee_id
      self.__password = password
      self.__login_device = login_device

   def login (self,id,password,device) :
      if device != self.__login_device :
         raise Security_Error("Multiple device login detected")
      if id == self.__employee_id and password == self.__password :
         print("login successful")
      else :
         print("login failed")



emp1 = Google_employee('2725331',"gy@345","IPHONE")

try :
   emp1.login('2725331',"gy@345","NOKIA")
except Exception as e :
   print(e.args[0])
   e.logout()