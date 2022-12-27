This program allows the user to create a bank account. 

Within the class "BankAccount" there is a contrusctor takes a 2 arguments, self and name. The name argument will
be the name of who owns the bank account. There is a __repr__() function to return a string showing who owns the account. Following those are 3 methods
that are used to show the balance, deposit more money, or withdraw a certain amount of money. 

Both the deposit() and withdraw() methods perform checks before it can perform the intended tasks. Both methods check to make sure the inputted amount
is greater than 0, the withdraw() method has an extra step to check wether the current balance is also greater than 0.  