x=__import__('string').ascii_letters;y,z=x[26:],x[:26];a,b=y[::-1],z[::-1];print(''.join([b[z.index(i)]if i in b else a[y.index(i)] if i in a else i for i in input()]))
