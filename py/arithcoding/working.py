#!/usr/bin/env python3.5
#!/usr/bin/env python3
def train(text):
    """text -> 0-order probability statistics as a dictionary

    Text must not contain the NUL (0x00) character because that's
    used to indicate the end of data.
    """
    assert "\x00" not in text
    counts = {}
    for c in text:
        counts[c]=counts.get(c,0)+1
    counts["\x00"] = 1
    tot_letters = sum(list(counts.values()))

    tot = 0
    d = {}
    prev = 0
    for c, count in counts.items():
        nxt = tot + count, tot_letters
        d[c] = (prev, nxt)
        prev = nxt
        tot = tot + count
    assert tot == tot_letters

    return d

def encode(string, prob):
    start = 0
    width = 1
    for ch in string:
        d_start, d_width = prob[ch]
        start += d_start*width
        width *= d_width

    return random.uniform(start, start+width)

def decode(num, prob):
    string = []
    while True:
        for symbol, (start, width) in prob.iteritems():
            if 0 <= num - start < width:
                num = (num - start) / width
                string.append(symbol)
                break
        if symbol == '@':
            break

    return ''.join(string)

string = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
print(string)
prob = train(string)
print("\n" + "\n".join((i + " = " + str(prob[i]) for i in prob if i != chr(0))))
e = encode(string, prob)
print(e)
s = decode(e, prob)
print(s)