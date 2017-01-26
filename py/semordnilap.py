#!/usr/bin/env python3
def main():
    with open("/usr/share/dict/words", "r") as f:
        wordset = set(f.read().strip().split())

    revlist = (''.join(word[::-1]) for word in wordset)

    pairs   = set(
        (wrd, rev)
        for wrd, rev in zip(wordset, revlist)
            if wrd < rev
            and rev in wordset
    )

    return pairs

if __name__ == '__main__':
    s = main()
    from pprint import pprint
    pprint(s)
    print(len(s))