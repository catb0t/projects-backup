import sys
while 1:
    char = sys.stdin.read(1)
    if char == '7':
        break
    print("char was", char)
    sys.stdin.flush()
