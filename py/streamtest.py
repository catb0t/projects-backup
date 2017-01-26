def runner(string):

    exec("s = 7 + " + string, globals(), locals())

    return s

def caller():
    s = runner("5")
    print(s)

caller()