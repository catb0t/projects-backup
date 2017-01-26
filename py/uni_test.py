from unicodedata import normalize

isascii = (lambda struni:
            (len(normalize('NFD', struni).encode('ascii', 'replace'))
                == len(struni)))

print(isascii("abcde"))
print(isascii("abcdÃª"))
