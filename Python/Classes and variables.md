# Classes and variables

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
 and mutators. They are also known as getters and setters. We can create them
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

A convention that is accepted by all pythonistas is using an underscore at the
 start of the variable or function name to indicate that it is a private 
 entity. I will be following that convention from now on.

Now let us look at the ways in which we can create an interface to allow
 changing the name of the account owner. 

### 1. Explicitly creating accessors (getters) and mutators (setters)

```python 
class Account:
    def __init__(self, holder_name: str):
        self._balance = 0.0
        self._holder_name = holder_name

    def deposit(amount: float):
        self._balance += amount

    def get_holder_name(self):
        return self._holder_name

    def set_holder_name(self, name: str):
        self._holder_name = name
```

Here we see that we explicitly define the get and set methods for our variable
 ```_holder_name```. The user can now view and change the value of the variable
 without having to directly change the value.

### 2. Using the ```property()``` function 

The above method works perfectly well, but there is a more pythonic way to
 do this.

```python 
class Account:
    def __init__(self, holder_name: str):
        self._balance = 0.0
        self._holder_name = holder_name

    def deposit(amount: float):
        self._balance += amount

    def _get_holder_name(self):
        return self._holder_name

    def _set_holder_name(self, name: str):
        self._holder_name = name

    holder_name = property(
        fget = _get_holder_name,
        fset = _set_holder_name,
        doc  = "The name of the account holder."
    )
```

The ```property()``` function allows us to expose a variable as a placeholder
 for our private variables and makes the user experience better at the same
 time without having to compromise on whether our private variable is safe or
 not. The ```property()``` function also takes in an argument ```fdel```
 which deletes the instance attribute. All of these are optional arguments
 but if using the ```property()``` function, you would at least pass the
 ```fget``` parameter generally.

### 3. Using the ```@property``` decorator

```python 
class Account:
    def __init__(self, holder_name: str):
        self._balance = 0.0
        self._holder_name = holder_name

    def deposit(amount: float):
        self._balance += amount

    @property
    def holder_name(self):
        """The name of the account holder."""
        return self._holder_name

    @holder_name.setter
    def holder_name(self, name):
        self._holder_name = name
```

Under the hood, this method uses the ```property()``` method, but instead of
 having to use the function itself, we use the decorator to pass functions as
 arguments. We use ```@property``` to define the getter for our private
 variable. The name of the function is the name of the exposed variable. Each
 function for the property (getter, setter, deleter) has the same name. A
 setter is the only one that has a parameter in its blueprint. The doc for the
 property is written in the getter function.
