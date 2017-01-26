
while input("myprompt\n ") in (""):
    try:
        print(int(input("myprompt\n ")), "yes")
        break
    except ValueError:
        print('nope')
        break
    if not ValueError:
        print('helo')
