# class Category:

Complete the Category class in budget.py. 

It should be able to instantiate objects based on different budget categories like food, clothing, and entertainment. 

When objects are created, they are passed in the name of the category. 

The class should have an instance variable called ledger that is a list. 
  
    
The class should also contain the following methods:
- the **"\_\_init\_\_"** function runs when the class is created and will be provided with the name of the category

    - agruments: 
        - class:self
        - string:name
    - operations:
        - declare:
            - string:name
            - array:ledger
            - integer:funds

- the "\_\_str\_\_" function will print the class info in a custom graph bar

    - requirements:
        - A title line of 30 characters where the name of the category is centered in a line of * characters.

        - A list of the items in the ledger. Each line should show the description and amount. The first 23 characters of the description should be displayed, then the amount. The amount should be right aligned, contain two decimal places, and display a maximum of 7 characters.

        - A line displaying the category total.

                                EXAMPLE
                    *************Food*************
                    initial deposit        1000.00
                    groceries               -10.15
                    restaurant and more foo -15.89
                    Transfer to Clothing    -50.00
                    Total:                  923.96
    
    - arguments
    - operations
        - 
- A **deposit** method that accepts an amount and description.

    - requirements: 
        - If no description is given, it should default to an empty string. 
        - The method should append an object to the ledger list in the form of
                {"amount": amount, "description": description}.

    - arguments:
        - class : self
        - integer : ammount
        - string : description
            - default = ""

    - operations
        - append to array:ledger->object:{"amount": amount, "description": description}
        - add integer:ammount to integer:funds
    
- A **withdraw** method that is similar to the deposit method, but the amount passed in should be stored in the ledger as a negative number.

    - requirements:
        - If there are not enough funds, nothing should be added to the ledger. 
        - This method should return True if the withdrawal took place, and False otherwise.
        - note: **withdraw** method will is never called before deposit method

    - arguments:
        - class : self
        - integer : ammount
        - string : description
            - default = ""

    - operations:
        - make "ammount" negitative
        - if class:method:(**check_funds**):arguments(ammount)
        - if integer:funds minus ammount is less than zero:
            - **return false**
        - if array:ledger is empty:
            - **return false**
        - append to array:ledger->object:{"amount": -amount, "description": description}
        - declare funds (funds minus ammount)
        - **return true**

- A **get_balance** method that returns the current balance of the budget category based on the deposits and withdrawals that have occurred.

    - arguments:
        - class:self

    - operations:
        - **return funds**

- A "transfer" method that accepts an amount and another budget category as arguments. 

    - requirements:
        - The method should add a withdrawal with the amount and the description "Transfer to [Destination Budget Category]". 
        
        - The method should then add a deposit to the other budget category with the amount and the description "Transfer from [Source Budget Category]". If there are not enough funds, nothing should be added to either ledgers. 
        
        - This method should return True if the transfer took place, and False otherwise.

    - agruments:
        - class:self
        - integer:ammount
        - class:Category
    
    - operations:
        - boolean:is_valid: if class:self:method("check_funds")arguments(integer:ammount) **and** class:Category:method("check_funds"): arguments: (integer:ammount)
        
        - if not is_valid:
            - **return false**

        - class:self: 
            - method(**withdraw**): arguments:
                - (integer: ammount, fstring : "Transfer to {class:Category:name}")

        - class:Category:
            - method(**deposit**): arguments:
                - (integer: ammount, fstring : "Transfer to {class : self : name})

- A **check_funds** method that accepts an amount as an argument. 

    - requirements:
        - It returns False if the amount is greater than the balance of the budget category and returns True otherwise. 
        - This method should be used by both the withdraw method and transfer method.
    - arguements:
        - class:self
        - integer : ammount

    - operations:
        - **return** boolean: if class:self:
            - integer:funds
            - is less than integer: ammount