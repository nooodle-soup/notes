# Access Modifiers

Access modifiers are used for controlling exposure (visibility) of variables,
 constants and methods to the user.

## Where to define variables in python classes

Let us create a class ```Account```.

```python
class Account:
    balance = 0

    def deposit(amount: float):
        self.balance += amount 
```

For now, our class has a ```balance``` variable. I can both
 be modified in the following way:
```python
account_1 = Account()
print(f"Account 1 balance = {account_1.balance}")
[Out]: Account 1 balance = 0

account_1.balance = 1
print(f"Account 1 balance = {account_1.balance}")
[Out]: Account 1 balance = 1
```

Seems that there is no harm done here. But it only seems that way. What if we
 directly modify the value of ```Account```'s balance?

```python
Account.balance = 1

account_2 = Account()
print(f"Account 2 balance = {account_2.balance}")
[Out]: Account 2 balance = 1
```

The value of ```balance``` after our modification has become 1 for all new
 accounts that would be opened in the future. This is a problem because the
 ```deposit``` function now needs to account for the increased default value
 from 0 to 1.

For our interface to be more secure, we need to define our variables in such a
 way that the user cannot modify these values. 

```python 
class Account:
    def __init__(self):
        self.balance = 0

    def deposit(amount: float):
        self.balance += amount
```

Now there is no way for a user to change the value of ```balance``` in a way
 that breaks the program. We can see below that even after directly changing
 ```Account.balance```, the balance of the account created after it retains 
 the orginal intended value of 0.

```python
Account.balance = 1

account = Account()
print(f"Account balance = {account.balance}")
[Out]: Account balance = 0 
```

## How to give the ability to modify and retrieve values

To allow users to modify values and access them safely, we can define accessors
 and modifiers. They are also known as getters and setters. We can create them
 in a couple of ways. For our example, let us create a new variable
 ```holder_name``` to store the name of the person to which the account
 belongs. Accounts can be transferred to another family member and would
 require the ```holder_name``` to change.

```python 
class Account:
    def __init__(self, holder_name: str):
        self.balance = 0
        self.holder_name = holder_name

    def deposit(amount: float):
        self.balance += amount
```

Now let us look at the ways in which we can create an interface to allow
 changing the name of the account owner. 

### 1. Explicitly creating accessors (getters) and modifiers (setters)

```python 
class Account:
    def __init__(self, holder_name: str):
        self.balance = 0
        self.holder_name = holder_name

    def deposit(amount: float):
        self.balance += amount
```

### 2. Using the ```property()``` function 

