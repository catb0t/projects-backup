import warnings

class AmbiguousStatementWarning(Warning):
    pass

def x():
    warnings.warn("unable to parse statement syntax",
                   AmbiguousStatementWarning, stacklevel=3)
    print("after warning")

def x_caller():
    x()

x_caller()
raise AmbiguousStatementWarning("ambiguous statement syntax")
