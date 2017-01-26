# Prettyprinted Titleboxes

<sup>please read the whole post before answering!</sup>

This is a prettyprinted titlebox, using unicode box-drawing characters (code points `U+2550`, `U+2551`, `U+2554`, `U+2557`, `U+255A` and `U+255D`) for the box's borders, generated with a <s>small</s> fair amount of Python. Everything is built from scratch and nothing is hardcoded: the filename is the actual filename, the time is the file's modification time, and the `about a minute ago` is derived from that.

The box's width is either determined from your system's settings (terminal width) or if that value is unavailable, uses a hardcoded `80`. For the width of the box itself, that value is multiplied by `.75`.

Whitespace is added to the left side to try to center the box horizontally and the height is determined by the number of rows of text.

The inner text is centered by whitespace on both sides, which is calculated and appended accordingly. Then, extensive error-checking takes place to ensure that under no circumstances does the right side of the box ever not line up for a given string length.

<pre><code>╔══════════════════════════════════════════════════════════════════╗
║                                                                  ║
║                         filename: header.py                      ║
║                                                                  ║
║         authored by Png Fgriraf &lt;notmyrealemail@gmail.com&gt;       ║
║                                                                  ║
║         on 30-11-2015 @ 00:43:35 UTC (about a minute ago)        ║
║                                                                  ║
║      redistributable under the GNU GPLv3 || &lt;http://fsf.org&gt;     ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝
</code></pre>

<!-- Here's a pastebin, because SE thinks it's funny to remove `<`, `>`, and superfluous whitespace and make them unrecoverable. http://pastebin.com/wfnid60U -->

Making my program output other kinds of alignments and borders as an example would be a lot of work, so I won't right now but I think you get the idea.

## The task

Write a full program taking input **or not** to make such a titlebox.
Running/building/interpreting it must produce an output; functions alone are allowed if you include in the byte-count their separate invocation.

### What makes a titlebox?

For this challenge, the *minimum requirements* are as follows: <sup>Fear not, clarification ahead!</sup>

1. four lines of text,

2. 40 ASCII-fixed-width columns wide,

3. 3 independently variable fields (i.e, filename, modified time and relative time of modification),

4. a top and bottom border, consistent of any normal-width **printable** unicode code point including spaces,

5. a left and right border, consistent of any normal-height **printable** unicode code point including spaces,

6. a form of alignment, consistent of any normal-width **printable** unicode code point including spaces,

7. no printed errors or junk output before, after or within the titlebox's display<sup> how do you expect to impress the boss??</sup>

### Clarifications on the previous (one per item)

1. you may pad text-filled lines with lines consistent entirely of whitespace above and below for style/readability, ***bonus*** if you choose to.<br>the fourth line is any fixed-length string of your choice the length of which is equal to 60%+ of the inner width of the box.

2. this minimum is for hardcoded widths. if you opt to grab from system configuration the terminal width to use then it's not your fault if someone uses their terminal at 10x24.

3. you may use any source, but you may only use each format once per source. for example, if you choose `random.randint()` as the source and no formatting for your first field, then your second field may be the floating-point time since the Unix Epoch, but if you choose that alone you may only use it again if it's formatted differently. in the provided case above, I use the filename, and then the Epoch twice: once formatted using `time.strftime(mtime)`, and once by calculating the difference between `mtime` and `now` and making it human-readable (plurals and grammar and more, oh my!). <br><br>**if (and only if) your language is incapable of reading the time, a file's \*nix `mtime` (modified-time) (or your platform's equivalent) or its own filename for whatever reason *and there are no suitable substitutes or equivalents*, you may substitute instead any string for which no two invocations will be identical (with the notable exception of filenames and the like).**

4. if the character prints on your machine, but you have a weird system-wide encoding from 1979, then it's not really printable, is it? acceptable characters are those printable in ASCII, and any normal-width unicode code point for which any of the fonts `Monospace`, `Ubuntu Mono` or `Liberation Mono` contain glyphs. <sup>I have access to these, as does anyone with internet, because they are free and open fonts.</sup>

5. same as \#4.

6. you may left-, right- or center-align the text, however if you choose either of the <s>lazy</s> former options, you will be penalised. the encoding rule from \#4 also applies.

7. whether or not there are internal errors raised is entirely inconsequential; all that matters is whether they print or not. if, and only if, printing is implicit in your language, then whatever junk is needed to make the titlebox Perfect is okay (as long as it's not superfluous or suppressable).

### Rules, boring Rules

Time for some hard-and-fast rules:

1. You may not hardcode the whole of the output. Not encoded, not in a separate file, not compressed, you may not. similarly, you may not *require* the user to paste in the finished title box just so it can copy <a href="https://en.wikipedia.org/wiki/Cat_(Unix)">standard input to standard output</a>, but you may take input and utilise it diligently.

2. Your program, when executable, must complete in linear time on modern hardware and be testable by any Linux, Windows or Mac user willing to download a compiler / interpreter. Using platform-specific syscalls is allowed, provided *someone somewhere* can indeed verify your code.

3. <sup>i have run out of rules, please suggest more!</sup>

4. Standard loopholes are, of course, disallowed.

## Scoring / bonuses

Though there is no leaderboard (yet?) please format your answer header as such:<sup>of course the link is optional</sup>

<pre><code># [Language](http://link.xyz), <s>old.bytes</s> current.bytes
</code></pre>

such that Humans May Read It.

### Bonuses

* For each line of text over 4, take 20% off your score in bytes.

* For each inner-whitespace padding line accompanying a line of text or the border, take off 10%.

* For each text field (distinguished by source and formatting) over the three required, take off 10%.

* If you choose to center-align your text, take off 10%.

* If you choose right-align, add 10% to your score.

* If you choose left-align, add 5% to your score.

* For each alignment miscalculation (due to even/odd length strings or otherwise) in a given invocation in a set of total 100 test invocations, add 5%.

* <sup>??? more??</sup>

* This is [tag:code-golf] so shortest code in bytes wins!

My score, with no applicable bonuses for my ungolfed code is approximately 5000 bytes. (I haven't counted because it's in a library file with other miscellaneous functions, some of which it uses, but thats my estimate. (The file is 22636 bytes.))

Happy golfing!

----
suggested tags: [tag:code-golf] [tag:ascii-art] [tag:kolmogorov-complexity]
