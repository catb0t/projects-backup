#!/usr/bin/env python3
def T_lookup(obj, name):
    "looking up the attribute"
    return True if name in (*dir(obj), *(obj.__dict__.keys())) else False


def T_catch_getattr(obj, name):
    "using getattr and catching exceptions"
    try:
        return bool(getattr(obj, name))
    except AttributeError:
        return False


def T_hasattr_native(obj, name):
    "using hasattr alone"
    return hasattr(obj, name)


def T_abuse_exec(obj, name):
    "abusing exec"
    try:
        exec("{}.{}".format(obj.__name__, name), globals(), locals())
        return True
    except AttributeError:
        return False


def T_abuse_eval(obj, name):
    "abusing eval"
    try:
        eval("{}.{}".format(obj.__name__, name), globals(), locals())
        return True
    except AttributeError:
        return False

if __name__ == '__main__':

    from timeit import timeit
    from re import match, compile
    prf = compile("^T_")

    scope = globals().copy()

    funcs = sorted(
        [ scope[obj] for obj in scope if match(prf, obj) ],
        key=lambda f: __import__("inspect").findsource(f)[1]
    )

    times_fail = []
    times_pass = []

    for func in funcs:
        print("timing", func.__name__)
        ftime = timeit(stmt='func(func, "asd")', setup="from __main__ import func", globals=locals())
        times_fail.append(ftime)
        ptime = timeit(stmt='func(func, "__name__")', setup="from __main__ import func", globals=locals())
        times_pass.append(ptime)

    times = list(zip(times_pass, times_fail))

    i = 0
    while i < len(times):
        fname = funcs[i]
        a_time, b_time = list(map(lambda i: round(i, 4), times[i]))
        out = "{} \n\tpass: {}\n\tfail: {}".format(fname.__name__, a_time, b_time)
        print(out)
        i += 1

    i = 0
    while i < len(times):
        func, tobj = funcs[i].__doc__, times[i]
        at, bt = round(tobj[0], 3), round(tobj[1], 3)
        print(func, "\n\tattr exist:", str(at), "\n\tnot exist: ", str(bt))
        i += 1

    #comb = list(dict(zip([func.__doc__ for func in funcs], [round(time, 3) for time in times])).items())

    #sc = list(sorted(comb, key=lambda f:f[1]))

    #from itertools import chain
    #print(str("{} ({}) is faster than " + ("{} ({}) which is faster than " * (len(sc) - 1))).format(*list(chain(*sc))) + "junk")

