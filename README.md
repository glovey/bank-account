# bank-account

project to design a bank account with simple features - check account details, withdraw and deposit

introduced a PIN number check so you cant acces methods with entering the account objects pin
introduced a main menu so the user chooses the action they want

Issues / improvements:

I wanted to include an 'open account' function to generate new account objects. Rough code below:

 def OpenAccount(name, balance):

  acc_number =1
  name = input("To open an account give your first name")
  balance = ("Now state your opening balance")

  f"acc{acc_number}" = Account(name, balance)
  

  print (f"CONGRATS, you have a new bank account\naccount number is acc{acc_number}#\naccount name = {name}\n balance is {balance}")
  acc_number +=1
  
  ISSUE with the above - can't use f-strings as variable names so need to find a way to generate unique acc number id's to which i would then apply OOP (Account class)
  
  If this was impelemeted you could then check pin against each Account object so the user could check details and for particular accounts.
  
  to be continued...
  
  
