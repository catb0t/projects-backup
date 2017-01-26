from sys import argv
from input_constrain import _read_keypress, _writer
fname = argv[1]

_writer("compilation successful; out-file: {}\nrunning ./{} after keypress or CTRL-C to abort run:".format(fname, fname))
try:
    _read_keypress()
    _writer("\n\n")
except (KeyboardInterrupt, EOFError):
    _writer("\nnot running due to interrupt or EOF\n")
    exit(1)
