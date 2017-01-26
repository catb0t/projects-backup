import re
c = re.compile(r"(.*[ea]?[ui]?rl$)")
n = open("/usr/share/dict/words")
z = n.read().split("\n")[:-1]
n.close()
del n
for i in range(len(z)):
    f = z[i]
    if re.match(c, f):
        print("{} probably rhymes with Perl".format(f))

    if f == f[::-1] and len(f) > 1:
        print("{} is a palindrome".format(f))

#    real    0m40.355s
#    user    0m39.412s
#    sys     0m0.656s

#    avg     .40355s per loop