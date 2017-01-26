# mouse15 v0.0.0.1
a concise concatenative stack-based programming language
---

## types

mouse15 has five basic types:

 * `123` = number (integer)
 * `123.0` = number (floating point)
 * `"Hello, World!"` = string
 * `{"value" "value2"}` = type-agnostic array
 * `{"key"|"value" "key2"|"val2"}` = type-agnostic dictionary

mouse15 is dynamically typed; more on that later.

## operators

mouse15 has plenty of default builtin operators:

 * ` ` &nbsp;is whitespace; it is never needed (ever!) but is sometimes used for readability
 * `¤` begins a single line comment which continues either to the next occurrence or the end of the line
 * `§` begins a multiline comment, which continues to the next occurrence
 * `123` pushes 123.0
 * `"Hello, World!"` pushes a string
 * `'c` pushes the ascii codepoint for `c` (99)
  * `'¤` pushes the unicode codepoint for `¤` (164)
  * `' ¤` pushes the unicode codepoint for ` ` (32) and then begins a comment

 * <code>&#96;</code> ... <code>&#96;</code> puts the inner string on the stack; `pop`ing it off will exec it
  * an unclosed <code>&#96;</code> anywhere puts the whole program on the stack
 * `6 @x` pushes the 7th 0-indexed item in the array `x`
  * `"key" @x` pushes the first value of `x` with that key
  * `@x{l:h}` allows for python-style array indexes
 * `#` pops top of stack and `exec`s in the current environment
 * `%MYFUNC%` ... `;` is a macro definition; call it like `$MYFUNC;`
 * `%{` ... `}%` defines an anonymous block
 * `^` breaks execution
  * if in a loop, break from the loop
  * if in a macro, break
  * else, exit with second-to-top as error code/message
 * `*` pops two from stack, multiplies and pushes result
  * `"Hello " 5 *` pushes `"Hello Hello Hello Hello Hello "`
 * `(` ... `)` is an infinite loop
  * `^` breaks
  * `(i 10 > ^ 1 !i +` ... `)` loops 9 times, incrementing i each time
 * `-` pops top two from stack, subtracts last from first and pushes result
  * `"Hello" 5 "ll" -` pops from the stack, removes max 5 occurrences of the substring `"ll"` from the string, and pushes result
 * `_` pops the top of the stack, negates it and pushes it
  * `"Hello" _` pushes `"olleH"`
 * `+` pops top two from stack, adds and pushes result
  * `"Hello,"+" World!"` pushes `"Hello, World!"`
 * `=` pops the top two from stack and pushes `1.0` if type-and-value-equal and `0.0` otherwise
  * `"5"5=` pushes `0.0`
 * `~` pops the top two from stack and pushes `1.0` if type-agnostic value-equal and `0.0` otherwise
  * `"5"5~` pushes `1.0`
 * `1 0 > [` if true `|` elseif `v 0 = |` if true `|` else `]`
 <br>or:
 ```
1 0 > [
//if true//
| v 0 = |
//elif true//
| //else//
]
 ```
 * `\` is general-purpose OR/else
 * `~` is bitwise NOT
 * `&` is bitwise AND
 * `|` is bitwise XOR
 * `^~&|` is bitwise OR
 * `/` is Forth's `/MOD`: pushes modulus and division
 * `:x5;` sets `x` to 5
  * `:x5=;` sets `x` to whether 5 and the top of the stack are `=`-equal
  * `:x5~;` sets `x` to whether 5 and the top of the stack are `~`-equal
  * `:x{` ... `};` sets `x` to an array indexable like `@x5`
 * `;` is general-purpose terminator
 * `,` pops the top of the stack & prints that UTF-8 or ASCII codepoint
 * `.` pops the top of the stack & prints to STDOUT
 * `<`, `>` pops two from stack and return `1.0` if less than or greater than, respectively & `0.0` otherwise
 * string or number on a string: compares length
 * `?` pushes input as a string

🐭 λ ¶

## predefined variables (builtins)

### uppercase

the uppercase alphabet is initialised to 26 functions, which can of course be shadowed.
their addresses are equivalent to the first 26 binary numbers.

 * `A` - pops and converts TOS to a string and pushes it
 * `B` - array where:
  * index 0 is a function that pushes `1.0` if TOS is valid Base64 and `0.0` otherwise
  * index 1 is a function that pops and attempts to decode TOS, and pushes the result
  * index 2 is a function that pops and encodes TOS as base64, then pushes the result
 * `C` -
 * `D` - copies TOS and pushes it (aka dup)
 * `E` - array where: errors are defined; calling any element of this array will raise it at runtime and cause the program to unrecoverably crash, exiting with the error code of that error's index
 * `F` - forget (aka drop)
 * `G` - undefined
 * `H` - array where: http-things are defined
 * `I` - pops and converts TOS to a float and pushes
 * `J` - undefined
 * `K` - undefined
 * `L` - length of top of stack
 * `M` - undefined
 * `N` - undefined
 * `O` - undefined
 * `P` - undefined
 * `Q` - undefined
 * `R` - array where: regex is implemented
 * `S` - swap the top of the stack with the second-to top item
 * `T` - array where: string tools are defined
 * `U` - undefined
 * `V` - undefined
 * `W` - undefined
 * `X` - undefined
 * `Y` - undefined
 * `Z` - undefined

### lowercase

the lowercase alphabet is initialised to 26 arrays of numbers. each array's first item is a number representing its position in the alphabet (i.e. `0 @a` = 0, `0 @z` = 25) and its other indicies hold various magic numbers, many of which are carried from mouse-2002.

 * `a`

## syntax

* whitespace is always optional, except around separate numbers:
```
a
```

## input/output

## runtime

When the program starts, the 52 variables are loaded into memory and macros are evalutated. The program runs, and if nothing was printed to STDOUT during the runtime then the top item of the stack will be popped and printed.

## example programs

* "Hello, World!"
```
"Hello, World!" § output of top stack element is implicit if no prior output
```
* Cat
```
?
```
 * or, for a looping version that can also read a file given as arg:
 ```
 :a &ARG; ;
 a L 1 = [
      1 @a &FOPEN; .
  |
      (
        ? "" ! ^ .
      )
  ]
 ```
* "For" loop: prints 0-10
```
!l :x;
(
    x 0 > ^
    | 1 !x +
    i .
)
```
* Print character representation of square of input: 4 bytes
```
? D * ,
```

* Bzzt! (Count to 500, printing bzzt instead of *n* if *n* mod 3 is 0): 28 bytes
```
(
    x 501 < ^
    x d \
    [
      x.
    |
      "bzzt".
    ]
    !x 1 +
)
```
