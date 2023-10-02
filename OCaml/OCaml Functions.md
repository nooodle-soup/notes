# OCaml Functions

Functions in OCaml are both similar and different at the same time compared
 to other languages. Let us discuss the features of OCaml functions.

### Function Definition 

In OCaml, functions are values. This means that we define a function in the
 same manner as we would a variable, using the `let` keyword. The first 
 identifier following the `let` keyword is the function name, and each
 identifier following the function name is a parameter of that function. 
 This is what a function looks like in OCaml.

```ocaml
# | let add2 x = x + 2;;
  | val add2 : int -> int = <fun>
# | let add x y = x + y;;
  | val add : int -> int -> int = <fun>
```

Here, `add2` is the function name and `x` is the parameter. The type signature
 is `int -> int` which essentially means that the function takes in an int and 
 returns an int. For the `add` function, the type signature is `int -> int ->
 int` which can be read as "takes in two int arguments and returns an int 
 value". What it actually means is something we will discuss a bit later.

### Function as Arguments 

Given that functions are values, it would make sense to be able to pass a 
 function as an argument. This is similar to languages like Python where a
 function can be passed as an argument.

```ocaml
# | let apply_and_add f x y = f x + f y;;
  | val apply_and_add : (a' -> int) -> a' -> a' -> int = <fun>
```

We can observe a few new things in the type signature. The first is the 
 introduction of the generic `a'`. These generics are used to show that 
 depending on the function passed, the value of `x` and `y` will have to be
 of the type `a'`, as the function can only operate on values of those types.
 The second thing to observe is that the type signature uses parenthese here,
 something that we have not seen before. The parentheses in a type signature
 are used to show the type signature of a function. Here, `(a' -> int)` is 
 the type signature of the function `f`. The generic `a'` is used as we can not
 know what type of argument the function takes in. It could take a string, a
 float, another function as well. 

### Function as Return Values 

OCaml allows functions to be returned from another function. This keeps in line
 with the idea that functions are values. 

```ocaml
# | let create_adder x = fun y -> x + y;;
  | val create_adder : int -> int -> int = <fun>
```

Here, `create_adder` takes in an argument `x` and returns a function that 
 takes in another argument `y` and returns the sum of `y` with that value of `x`.
 The `fun` keyword is a way to write the equivalent of lamba functions in 
 Python. So say you want an adder that adds 2 to any value and returns it. To 
 achieve this, you can pass 2 to `create_adder` and you're all set.

```ocaml
# | let add2 = create_adder 2;;
  | val add2 : int -> int = <fun>
# | add2 3;;
  | - : int = 5
```

### Currying

We can also provide a function with partial arguments and it will return a
 function waiting for the rest of the arguments. To understand how this works, 
 we need to look at what is known within the OCaml world as Partial Application 
 of Functions. Let us bring back the `apply_and_add` function here and pass a 
 function to it.

```ocaml
# | let apply_and_add f x y = f x + f y;;
  | val apply_and_add : (a' -> int) -> int -> int -> int = <fun>
# | let to_int_and_add = apply_and_add Int.of_float;;
  | val to_int_and_add : float -> float -> int = <fun> 
```

We see that passing partial arguments to the function `apply_and_add` works.
 `to_int_and_add`'s type signature shows that it is a function that accepts 
 two floats and returns an int. Note that the type signature changed from 
 two generics to two floats. This is because of the function that was passed to 
 `apply_and_add`. This demonstrates that partial application of functions 
 creates functions that are waiting for the next argument. This is 
 possible because of a feature called **Currying**. This is a feature that 
 brings a lot of power to the language and provides flexibility to the style 
 of writing OCaml.

