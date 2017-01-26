from input_constrain import until_not
import string

ALLOWED_CHARS = string.printable

def textwriter():
    print("")
    print("Start typing to begin.")
    try:
        textwriterCommand = until_not(ALLOWED_CHARS)
    except (EOFError, KeyboardInterrupt):
        pass
    saveAs = input("Save file as: ")
    with open(saveAs, 'w') as f:
        f.write(textwriterCommand)