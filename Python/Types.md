# Notes On Python

## Types

You can use python types to ensure the type of data you are passing
 around in your program.

Take the following for example ->

```python
def add_ints(x, y):
    sum = x + y
    print(f"The sum of {x} and {y} is {sum}.")
    return sum
```

This function works perfectly for ints. However, it also works perfectly for
 floats.

To make it so that the function takes in ints and works only on ints, we can
 explicitly state the types of variables x and y. In the above case, we need to
 set them both to ```int```. To make sure our returned value is also an
 integer, we can set the return type of the function to ```int```.

Our function now looks like this ->

```python
def add_ints(x: int, y: int) -> int:
    sum = x + y
    print(f"The sum of {x} and {y} is {sum}.")
    return sum
```

While I am a strong believer of designing functions such that a ```None```
 value is never passed as an argument, sometimes it is needed (because of
 language limitations).

Let us look at the code below ->

```python
class Node:
    def __init__(self, value, next):
        self.value = value
        self.next  = next
```

This is a class for a node to be used in a singly linked list. What we see is
 that both the ```value``` and ```next``` arguments can take in a ```None```.
 Thinking about it, our ```value``` should never be ```None``` as a node with
 nothing in it should not exist. So we need to make sure that the ```value```
 always has something. The ```next``` however, can be a ```None``` value as the
 list has to end somewhere. (This is language specific. There may not be a
 concept of ```None``` in a language at all, as in OCaml.)

So our function now becomes ->

```python
import Optional from typing

class Node:
    def __init__(self, value, next: Optional[Node]):
        self.value = value
        self.next  = next
```

