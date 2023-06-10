import sys

class User:
  def __init__(self,username,password):
    self.username = username
    self.password = password



class Client(User):
  def __init__(self, username, password):
    super().__init__(username, password)
    self.deposit_balance = 0
    self.withdrow_balance = 0
    self.transaction_history = []
  
  def deposit(self,amount):
    self.deposit_balance += amount
    self.transaction_history.append(f'Deposit {amount}')
    print('Deposit Successfully')

  def withdrow(self,amount):
    if self.available_balance>amount:
      self.withdrow_balance += amount
      self.transaction_history.append(f'Withdrow {amount}')
      print('withdrow Successfully')
    else:
      print("you don't have balance")
  
  

  


  @property
  def available_balance(self):
    if self.deposit_balance<=self.withdrow_balance:
      return 0
    return self.deposit_balance-self.withdrow_balance
  
  def show_history(self):
    for i, history in enumerate(self.transaction_history, start=1):
      print(f"{i}. {history}")



class Admin(User):
  def __init__(self, username, password):
    super().__init__(username, password)








class Bank:
  def __init__(self, name, balance):
    self.__name = name
    self.__available_balance = balance
    self.__total_loan = 0
    self.__is_load_available = True
    self.user_list = []
    self.admin_list = []

  @property
  def available_balance(self):
    return self.__available_balance
  @property
  def total_loan(self):
    return self.__total_loan
  @property
  def is_load_available(self):
    return self.__is_load_available

  @is_load_available.setter
  def is_load_available(self, value):
    self.__is_load_available = value
  
  def take_loan(self,amount, user):
    if self.available_balance==0:
      if amount < 2*user.available_balace:
        self.__available_balance -=amount
        self.__total_loan +=amount
        user.deposit += amount
        user.transaction_history.append(f'take loan {amount}')
      else:
        print('your goiven amount cross the limit')
    else:
        print('The Bank is BankRupt')  



  def transfar(self, from_user, to_username, amount):
    for user in self.user_list:
      if to_username == user['username']:
        print('user found')
        if from_user.available_balance>amount:
          user["deposit_balance"] += amount
          user["transaction_history"].append(f'Transfer {amount} from {from_user.username} to {user["username"]}')
          print('Transfar Successfully')
          return
        else:
          print("you don't have balance")
          return
      else:
        print('To User Not Fount')
        return


  def account_create(self,username,password,is_admin=False):
    user = None
    if is_admin:
      user = Admin(username,password)
    else:
      user = Client(username,password)
    self.user_list.append(vars(user))
    print(f'{user.username} create successfully')
    return user
  
  def login(self,username, password):
    for user in self.user_list:
      if user["username"]==username and user["password"]==password:
        return True,'user'
    
    for admin in self.admin_list:
      if admin["username"]==username and admin["password"]==password:
        return True, 'admin'
    return False, None

bank = Bank('AFI Bank', 1000000)






def main():
  def client_action(username,password):
    
    user = bank.account_create(username,password)
    while True:
        action = input("""
        1. for deposit. 
        2. for withdrow. 
        3. for check available balance.
        4. for transfer amount.
        5. for check transaction history.
        6. for take a loan .
        7. for logout 
        """)
        if action == '1':
          amount = int(input("Enter Deposit Amount: "))
          user.deposit(amount)
          
        elif action == '2':
          amount = int(input("Enter Withdrow Amount: "))
          user.withdrow(amount)
          
        elif action == '3':
          print(f'your available balance {user.available_balance}')
          
        elif action=='4':
          to_username = input('Enter other User username: ')
          amount = int(input("Enter Amount: "))

          bank.transfar(user,to_username,amount)
          
        elif action == '5':
          user.show_history()
          
        elif action == '6':
          amount = int(input("Enter Withdrow Amount: "))
          if bank.is_load_available:
            user.take_loan
          else:
            print('During this time our loan service off ')
          
        elif action=='7':
          main()

  def admin_action():
    username = input('Enter your username: ')
    password = input('Enter your password: ')
    bank.account_create(username,password,True)
    while True:
      action = input("""
        1. for check the total available balance of the bank.
        2. for check the total loan amount.
        3. for on or off the loan feature of the bank.
        4. for logout
        """)
      if action == '1':
        print(f'Total available Balance of Bank is {bank.available_balance}')
        
      elif action == '2':
        print(f'Total given loan {bank.total_loan}')
        
      elif action == '3':
        bank.is_load_available = False
        print('Loan Feature change')
        
      elif action=='4':
        print('logout successfully')
        main()



  while True:
    comand = input("Press 1 for Create Admin account\nPress 2 for Create Admin account\nPress 3 for Login\nPress 4 for Logout\n")
    

    if comand=='1':
      admin_action()
      
    elif comand=='2':
      username = input('Enter your username: ')
      password = input('Enter your password: ')
      client_action(username,password)
    elif comand=='3':
      username = input("Enter Username : ")
      password = input("Enter Password : ")
      is_valid, type = bank.login(username,password)
      
      if is_valid and type=='admin':
        admin_action()
      elif is_valid and type=='user':
        client_action(username, password)
      else:
        print('User not exist first create account')
        main()
    elif comand == '4':
      sys.exit()



if __name__=='__main__':
  main()