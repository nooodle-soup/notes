# OCaml Basics

Learning a language, any language has 5 essential components. They are:
1. Syntax
2. Semantics
3. Idioms
4. Libraries
5. Tools

Let's discuss them briefly in reference to the following python code.

```python
import math

def printx(x):
    if math.sqrt(x) > 10:
        print(x)

x = 10

printx(x)
```

### 1. Syntax

Syntax of a language is the set of rules that define what makes up a program
 in the language. In our code above, syntax refers to what and how we can
 write to make a well-formed program. The keywords (```def```, ```if```,
 ```import```), the presence of whitespace (as compared to languages that don't
 require indentation for defining blocks of code), punctuation (```:``` instead
 of a typical ```{}```), operators (```=```), formatting, etc. all together
 make up the syntax for a language.

### 2. Semantics

According to Wikipedia, semantics is the rigorous mathematical study of the
 meaning of programming languages. Semantics assigns assigns computational
 meaning to valid strings in a programming language syntax.

In a simpler manner, semantics are the rules which define how a program will
 behave. There are two parts to semantics, static semantics which is the
 compile time checking of the legality of the program other than the obvious
 syntactic checks, and dynamic semantics which define the run time behaviour
 of a program during execution or evaluation.

### 3. Idioms

Idioms of a programming language are essentially the most common takes to
 expressing computations using the features of the language.

### 4. Libraries

As a language gets older and programmers write more code with it, slowly
 there is a rise of convenience functions and interfaces pertaining to a
 problem which are usually bundled together in what we call a library. Every
 programming language has them and learning how to use them is an essential
 part of the journey to learn a programming language.

### 5. Tools

Tools are very useful to make a programming language easy to use. Debuggers,
 Integrated Development Environments and even performance analysis tools
 help one master a language and build better programs.

Let's start with understanding the OCaml syntax.

## Naming Variables

Variable names (identifiers) can only start with a lowercase letter or an
 underscore. Punctuations expept for _ and ' are excluded. The following are
 some examples I wrote in utop (OCaml's toplevel that is a REPL (Read-Eval-
 Print Loop). Assume I have used utop unless I state otherwise.

```ocaml
# | let x7 = 10-3;;
  | val x7 : int = 7 
  |
# | let x_plus_3 = x + 3;;
  | val x : int = 10
```

These are the valid ways in which one can define identifiers for variables. Let
 us look at some invalid examples.

 ```ocaml
# | let X = 10;;
  | Error: Unbound constructor X
  |
# | let 7x = 7;;
  | Error: Unknown modifier 'x' for literal 7x
```

We can see that the capital letters at the start of a variable cause an error.
 This is because they are reserved for something that is called a constructor.
 Constructors will be talked about in more detail when we come to user defined
 types.

One thing to note is that every statement in OCaml is an expression.
 In ```let x7 = 10 - 3;;```, ```10 = 3``` is an expression that evaluates to
 ```7```, which is a value of type ```int```. This allows the type of ```x7```
 to be inferred to ```int```. The OCaml interpreter is simple and smart and
 uses the expressions in a statement to infer the type of the indentifiers.

A value can be of the following types:
1. Base Values
    1. Integer numbers
    2. Floating-point numbers
    3. Characters
    4. Character Strings
2. Tuples
3. Records
4. Arrays
5. Variant values
6. Polymorphic variants
7. Functions
8. Objects

Keep in mind that all values are expressions but not all expressions are 
 values. An expression can fail to evaluate to a value in the following cases:
1. Evaluating the expression raises an error.
2. The expression can never be evaluated (infinite loops).

Now that we know how to name variables, let's look at functions.

## Functions

Functions in OCaml might seem almost alien if you have never experienced any 
 other Meta-Language (ML). They are defined using the same keyword used for
 assigning values to variables. The parameters are not written in parentheses.
 There is no clear syntactical way to show the start or end of a code block.
 And there is no return statement. Here's an example.

```ocaml
# | let add x y = x + y;;
  | val add : int -> int -> int = <fun>
```

Once you start writing code in OCaml though, you will wonder why you even used
 parentheses in the first place and why you needed the return keyword.
