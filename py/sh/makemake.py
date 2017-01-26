import sys

argv = sys.argv[1:]

fn = argv[0].split(".")[0]             # filename
rest = "".join(argv[1:]) # rest of opts

if rest == "":
    rest = '-Wall -Wextra -Wfloat-equal -Wundef -Werror -fverbose-asm -Wshadow -Wpointer-arith -Wcast-align -Wstrict-prototypes -Wstrict-overflow=5 -Wwrite-strings -Wconversion --pedantic -std=c11'

makefil = """CFLAGS={}

clean:
\trm -f {}
""".format(rest, fn)

fio = open("Makefile", "x")
fio.write(makefil)
fio.close()