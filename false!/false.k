// false!
// wouter van oortmerssen
// http://wouter.fov120.com/false/false.txt
// also http://math.boisestate.edu/%7Eholmes/holmes/sfdocs.pdf

\d .f

H:"'"                                                                                   / character
L:"[]"                                                                                  / lambda
C:"{}"                                                                                  / comment
Q:"\"\\"                                                                                / quote
B:" \n\t\r",_ci 255                                                                     / blanks
N:"0123456789"                                                                          / numeric
V:"abcdefghijklmnopqrstuvwxyz"                                                          / variable
Z:"ABCDEFGHIJKLMNOPQRSTUVWXYZ"                                                          / value of variable

x:{[n;f]{(((-n)_ x),,f .(-n)#x;y)}}                                                     / n-ary application -> 1
y:{[n;f]{(((-n)_ x),f .(-n)#x;y)}}                                                      / n-ary application -> m
w:{:[(*x)_in B;x;B[0],x]}                                                               / prefix w/ blank

O:+(("`"     ;{T~:;(x;y)})                                                              / trace
    (C 1     ;{`0;(x;y)})                                                               / stop
    (":"     ;{.[;();:;].|-2#x;(-2_ x;y)})                                              / set
    (";"     ;{((-1_ x),,.*-1#x;y)})                                                    / get
    ("!"     ;{(-1_ x;(1_-1_*-1#x),w y)})                                               / apply
    ("+"     ;x[2;+])                                                                   / add
    ("-"     ;x[2;-])                                                                   / sub
    ("*"     ;x[2;*])                                                                   / mul
    ("/"     ;x[2;_%])                                                                  / div
    ("<"     ;x[2;!])                                                                   / mod (added)
    ("_"     ;x[1;-:])                                                                  / neg
    ("="     ;x[2;~])                                                                   / equal
    (">"     ;x[2;>])                                                                   / more
    ("&"     ;x[2;&])                                                                   / and
    ("|"     ;x[2;|])                                                                   / or
    ("~"     ;x[1;~:])                                                                  / not
    ("$"     ;y[1;{(x;x)}])                                                             / dup
    ("%"     ;y[1;{()}])                                                                / pop
    ("\\"    ;y[2;{(y;x)}])                                                             / swap
    ("@"     ;y[3;{(y;z;x)}])                                                           / rot
    (")"     ;{({x,,x(#x)-y+1}.(-1_ x;*-1#x);y)})                                       / pick (ø)
    ("("     ;{(-2_ x;(,/1!($-2#x),"!"),w y)})                                          / dip
    ("?"     ;{(-2_ x;({:[x;1_-1_ y;()]}.-2#x),y)})                                     / if
    ("#"     ;{(-2_ x;({(1_-1_ x),u[(1_-1_ y),w x,y,"#"],"?"}.-2#x),w y)})              / while
    ("."     ;y[1;{`0:$x;()}])                                                          / output <- num
    (","     ;y[1;{`0::[1=4:x;_ci x;x];()}])                                            / output <- char {<- num}
    ("^"     ;{(x;(0:`),y)}))                                                           / chars <- input

A:_n                                                                                    / state
a:{:[~#y;k;~_n~A;`.f@*A;y[0]_in*O;o;y[0]_in V;v;m][x;*y;1_ y]}                          / apply 1

k:{(x;z)}                                                                               / end

h:{A::_n;(x,,*$y;z)}                                                                    / in character

c:{if[y=C 1;A::_n];(x;z)}                                                               / in comment

q:{if[y=Q 1;:(@[x;-1+#x;,;y,*z];2_ z)]                                                  / in escape
   if[y=*Q;A::_n;`0:*-1#x;:(-1_ x;z)]                                                   / exit quote
   (@[x;-1+#x;,;y];z)}                                                                  / in quote

n:{if[y _in N;:(@[x;-1+#x;,;y];z)]                                                      / in numeric
   A::_n;(@[x;-1+#x;0$];y,z)}                                                           / exit numeric

l:{if[y=L 1;A:::[1<#A;1_ A];:(@[x;-1+#x;,;L 1];z)]                                      / exit lambda
   if[y=*L;A,:`l;:(@[x;-1+#x;,;*L];z)]                                                  / enter lambda
   (@[x;-1+#x;,;y];z)}                                                                  / in lambda

o:{O[1;O[0]?y][x;z]}                                                                    / in operator

v:{(x,`$y;z)}                                                                           / in variable

m:{if[y _in Z;:(x;(V[Z?y],";"),z)]                                                      / value of
   if[y _in N;A::`n;:(x,,,y;z)]                                                         / enter numeric
   if[y=*C;A::`c;:(x;z)]                                                                / enter comment
   if[y=*Q;A::`q;:(x,,"";z)]                                                            / enter quote 
   if[y=H;A::`h;:(x;z)]                                                                 / enter character
   if[y=*L;A::,`l;:(x,,,*L;z)]                                                          / enter lambda
   A::_n;(x;z)}                                                                         / normal

D:30                                                                                    / trace width
T:0                                                                                     / trace flag
t:{k:0;if[g y;p b[x;y];k:(0:`)~,*B];(x;:[k;"";y])}                                      / trace (step)
g:{(~(*x)_in`,C)&(#x)&T&A~_n}                                                           / trace?
p:{`0:@[x;&x _lin 1_ B;:;*B]}                                                           / print
b:{(D$d x)," \004 ",(-D)$y}                                                             / format trace
s:{if[~g x;`0:,d x]}                                                                    / show stack
d:{:[#x;1_,/B[0],'f'[x;4::'x];""]}                                                      / display
u:1!(|L),                                                                               / format enlist
f:{:[7=y;O[0;O[1]?x];3=y;H,x;~1=y;$x;0>x;($-x),"_";$x]}                                 / format stack
e:{:[#y;*(a . t .)/(x;y,*-1#B);()]}                                                     / evaluate y on x
r:{:[x~,*B;.m[`p`r]:_n;s S::e[S;x]];}                                                   / respond
i:{S::x;A::_n;.m.p:2#*B;.m.r:r}                                                         / interpreter
j:{if[x _in,:'"01";T::0$x;:_n];A::_n;`0:,d e[();6::["."_in x;x;x,".f"]]}                / interpret file

\d .k

`0:,"false! 2006-06-17\n[space] to exit to K, [return] to clear, .f.i() for false!\n";.f.j'_i;.f.i()
