# let's make a class

class Atm:
    def __init__(self):
        self.__pin = ''
        self.__balance = 0

        self.__menu()

    def __menu(self):
        while True:
            user_input = input("""Enter your choice: 
                     1. Enter 1 to create a pin
                     2. Enter 2 to a make a deposit
                     3. Enter 3 to make a withdrawal
                     4. Enter 4 to check balance
                     5. Exit   
        """)
            if user_input == "1":
                self.set_pin()
            elif user_input == "2":
                self.deposit()
            elif user_input == "3":
                self.withdrawal()
            elif user_input == "4":
                self.check_balance()
            elif user_input == "5":
                print('Bye')
                break

    def set_pin(self):
        self.__pin = input('Enter your pin: ')
        print("Pin is updated")
    def deposit(self):
        temp = input('Enter your pin: ')
        if temp == self.__pin:
            amount = int(input('Enter the deposit amount: '))
            self.__balance += amount
        else:
            print('Pin is invalid')
    def withdrawal(self):
        temp = input('Enter your pin: ')
        if temp == self.__pin:
            amount = int(input('Enter the withdrawal amount: '))
            if amount <= self.__balance:
                self.__balance -= amount
            else:
                print("Insufficient funds")
        else:
            print('Pin is invalid')
    def check_balance(self):
        temp = input('Enter your pin: ')
        if temp == self.__pin:
            print(f"Your balance is: {self.__balance}")
        else:
            print('Pin is invalid')



