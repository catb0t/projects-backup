# BrainStorm for JSLisp

### Abstract stuff

* a full-featured, non-restrictive LISP for the browser

* compile to readable, idiomatic and safe JS; output file will be annotated with comments from the original source *and* comments containing original forms of literals, expressions, etc

* *full* browser and node interop

* **hygenic macros**

* later: possible type checking / static analysis at compile-time

* all that's needed for a super simple web server is:

  ```lisp
  ├── site/      ;; the rest of the site's content (pages, CSS, images...)
  ├── index.lsml ;; a front page written in JSL HTML template system
  └── serve.ls   ;; a server written in JSL using Node's http
  ```
  * The command `./serve.ls` will:
    * start serving files and folders (i.e, run as a normal JS script)
    * render `lsml` files through a JSON+data-structure template system using JSL's implicit support for complex datatypes & inline code

  * html files with script tags like:

    ```html
    <script type="text/jsl" id="name"> (code...) </script>
    ```
    * the script content will be transpiled to annotated JavaScript
    * ids should contain only valid JSL ident name
    * script tags with `id="main"` will be executed on page load in order of appearance if more than one is present
    * script tags with other ids can be imported as modules like `(var ident (use "ident"))`

## Literals

### Identifiers and misc. literals

* JSL identifiers match [this](https://regex101.com/r/yP6nQ8/1):

```js
/^([^\d][^"`';\s(){}\[\]]*)$/
```

* identifiers can't start with a number, and if something looks like both a number and an identifier, it will be used as a number (because the identifier regex is meant to be very lenient). Hopefully, we can mitigate these occurences.

In keeping with LISP of old, the only reserved characters are:

  * `'` only appear at the beginning of symbol names and `'(quoted '(lists))`
  * `;` line-comment char, goes from `;` to next `\n`
  * `;()` `;{}` `;[]` multiline &amp; inline comment, **can nest**, **must be terminated** (that is, EOF before closing paren/brace is a syntax error)
  * `()` `{}` `[]` obviously, this is LISP; we also have some conveniences for hashes (objects) and vectors besides normal lists
  * `` `" `` string delimiters. Both can be broken over any number of lines without `\`-escaping the ends, but <code>&#96;</code> preserves newlines and leading whitespace. Both perform `${string_interpolation}` with arbitrary JSL code
  * whitespace. no, you may not have any in identifiers.

* JSL **strings** match [this](https://regex101.com/r/qN7sA5/1):
```js
/(["`])([^\1\\]*(?:\\.[^\1\\]*)*)\1/
```
  * **multiline by default**
  * interpolation inside `` `backticks` ``

### Numbers

* JSL **whole numbers** match [this](https://regex101.com/r/wT0cV1/3):

  ```js
  /^([+-]?(?:[\d][\d_]*[\d]|[\d])(?:e[+-]?[+-]?[\d_]+)?[YZEPTGMKHDdcmμnpfazy]*)$/
  ```
  and look like:
  ```
  -1
  +1
  1_0
  1_000_000
  10
  0
  -0_0
  +1_0
  2e15
  +2e-15
  -2e+15
  2e+15
  2_0e1_0
  -2_0e+-115_0
  4T
  6_0Z
  +5f
  -5f
  ```

  And more.

  * underscores are discarded at parse time `100_000_000 -> 100000000`
  * scientific notation is kept where possible.
  * SI postfixes are resolved to JS number literals, or `new Fraction()` where possible.
  * integral, represented as `new Fraction(x, 1);` by default, converted to JavaScript double when needed
  * with `(#pragma force-inexact-math)`: converted to JavaScript double immediately

  * All the SI prefixes in JSL:

  ```
  yotta Y 1_000_000_000_000_000_000_000_000
  zetta Z 1_000_000_000_000_000_000_000
  exa   E 1_000_000_000_000_000_000
  peta  P 1_000_000_000_000_000
  tera  T 1_000_000_000_000
  giga  G 1_000_000_000
  mega  M 1_000_000
  kilo  K 1_000
  hecto H 100
  deca  D 10
  deci  d .1
  centi c .01
  milli m .001
  micro μ .000001
  nano  n .000000001
  pico  p .000000000001
  femto f .000000000000001
  atto  a .000000000000000001
  zepto z .000000000000000000001
  yocto y .00000000000000000000001
  ```

* JSL **decimal-format numbers** match [this](https://regex101.com/r/eU3pF5/1):

  ```js
  /^([+-]?(?:\d[\d_]*\d[,.]\d*|\d+[,.]|[.,]\d+|\d+[,.]\d+)(?:e[+-]?[+-]?(?:\d[\d_]*\d|\d))?[YZEPTGMKHDdcmμnpfazy]*)$/
  ```
  and look like:
  ```
  +9.
  ,9
  -.9
  +100_000,001e34
  -10_000.1231f
  ```


* JSL **rational numbers** match [this](https://regex101.com/r/gR3uO2/4):

  ```js
  /^((?:[+-]?(?:[\d][\d_]*[\d]|[\d])(?:e[+-]?[+-]?[\d_]+)?[YZEPTGMKHDdcmμnpfazy]*)?[+-]?(?:[+-]?(?:\d[\d_]*\d[,.]\d*|\d+[,.]|[.,]\d+|\d+[,.]\d+)(?:e[+-]?[+-]?(?:\d[\d_]*\d|\d))?[YZEPTGMKHDdcmμnpfazy]*|[+-]?(?:[\d][\d_]*[\d]|[\d])(?:e[+-]?[+-]?[\d_]+)?[YZEPTGMKHDdcmμnpfazy]*)\/(?:[+-]?(?:\d[\d_]*\d[,.]\d*|\d+[,.]|[.,]\d+|\d+[,.]\d+)(?:e[+-]?[+-]?(?:\d[\d_]*\d|\d))?[YZEPTGMKHDdcmμnpfazy]*|[+-]?(?:[\d][\d_]*[\d]|[\d])(?:e[+-]?[+-]?[\d_]+)?[YZEPTGMKHDdcmμnpfazy]*))$/
  ```
  and look like:
  ```js
  2/2     // reduced to 1/1
  -1/2
  -3+-1.5/45.32 // if you want this, you can have it
  1/0     // runtime error, compile-time warning
  1/0.    // Infinity
  1/.0    // Infinity
  -1/0.   // -Infinity
  -1/.0   // -Infinity
  ```
  etc.
  * implemented with the excellent [Fraction.js][fraction]
  * if the reader finds a rational number literal in the source then
    * an `import`, `use` or `require` of `fraction.min.js` will occur at compile-time , in which case all rational numbers will be calculated as normal inexact JavaScript floats.
    * `(#pragma force-inexact-math)` causes all rational literals to be calculated inexactly and represented as JavaScript doubles.

* JSL **arbitrary base numbers** match [this](https://regex101.com/r/wK4lR0/2):
  ```js
  /(0[a-z0-9]+:[a-zA-Z0-9]+)/
  ```
  and look like:
  ```
  0hx:a
  0x:a
  0b:0
  0vv:99
  ```
  * always transpiled to base-10 at compile-time because JS is confused about octal and hex literals
  bases other than oct, hex, bin and dec can be interned with the `(#pragma new-base base literals...)` pragma:
  ```clojure
  (#pragma new-base 36 "v" "yy")
  ```
  Now `0v:74` and `0yy:74` are both compiled to `256` because `74` in base-36 is `256`. Before such a pragm

 [fraction]: https://github.com/infusion/Fraction.js
