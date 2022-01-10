#OOP challenge


#account class

class Account:

  def __init__(self, name, balance, pin):

    self.name = name
    self.balance = balance
    self.pin = pin
  
  def __str__(self):

    return f"Name: {self.name} \nBalance: {self.balance}"

  def deposit (self):
    ammount = input("how much do you want to deposit?")
    self.balance = self.balance + int(ammount)
    print (f"your new balance is {self.balance}")

  def withdraw (self):
    want_withdraw = "Y"
    while want_withdraw == "Y":
      ammount = input("how much do you want to withdraw?")

      if self.balance - int(ammount) < 0:
        print ("your balance can't go below zero!")
        want_withdraw = input("do you want to try again?")

      else:
        self.balance = self.balance - int(ammount)
        print (f"you witdrew {ammount}, your new balance is {self.balance}")
        want_withdraw = input("do you want to withdraw again?")
    print ("thanks for your custom")

  def pin_check(self):
    
    user_acc = input("what is your account number?")
    user_pin = input("to access account enter pin")

    if int(user_pin) == self.pin:
      
      return True
    else:
      
      return False

#General methods



def main_menu(choice):
  choice = ""
  choice =  input("Choose an option: \ndeposit (answer 1)\nwithdraw (answer 2)\nCheck account details (answer 3)\nlog off (answer 4)")
  return choice

def transact (trans):
  
  choice = input ("do you want to perform a transaction? Y/N")
  if choice == "Y":
    trans = True
    return trans
  else: 
    print("thank you goodbye")
    trans = False
    return trans



acc001 = Account("joe", 1000,1234)
trans = True
choice = ""
if acc001.pin_check() == True:
  trans =  transact(trans)
  while trans == True:
    choice = main_menu(choice) 
    if choice == "1":
      acc001.deposit()
      trans = transact(trans)
    elif choice == "2":
      acc001.withdraw()
      trans = transact(trans)
    elif choice == "3":
      print (acc001)
      trans = transact(trans)
    else:
      print("thanks, goodbye")
      trans = False


