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
# let x7 = 10-3;;
val x7 : int = 7 

# let x_plus_3 = x + 3;;
val x : int = 10
```


