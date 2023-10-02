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

Here, `add2` is the function name and `x` is the parameter. The function type
 is `int -> int` which essentially means that the function takes in an int and 
 returns an int. For the `add` function, the type signature is `int -> int ->
 int` which can be read as "takes in two int arguments and returns an int 
 value".
