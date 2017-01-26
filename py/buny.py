def countEars(b):
    if b == 0: return 0
    if b == 1: return 2
    else:      return 2 + countEars(b - 1)

if __name__ == '__main__':
    print(countEars(3))