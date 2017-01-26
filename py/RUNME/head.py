### DEFAULT HEADER INCLUDE ###
import time
starttime = time.time()
yourGodTheCreatorOwner = 'Png Fgriraf <gurovanelzvare@tznvy.pbz>'
try:
    if ETALS:
        pass
    else:
        ETALS = ''
except NameError:
    ETALS = ''

# not invented here
import codecs, base64, os, sys, random, datetime, string, shutil, requests, traceback, io, turtle;
import __main__ as main;
from lxml import html

xr = range;
l = len;
w = print;
q = input;
mTime = os.stat(main.__file__).st_mtime  # for a programmer, I'm a very lazy person
ax = 0x656;
zb = '';
d = '';
nl = '\n';
b64 = base64;
r13 = 'rot_13';
# invented here
x = [nl, '', r13, 'rGWzqJbmp', 'b64'];
t = ((l(x) - 1) / 2) * .1;
dt = '.';
# Not Invented Here.
aDcd = codecs.decode;
aNcd = codecs.encode


def unrot(s): return aNcd(s, r13);


def rotten(s): return aNcd(s, r13);


def base64dcd(b): w(aDcd(b64.b64decode(b), 'utf-8'))


def base64ncd(s): w(base64.b64encode(bytearray(s, 'utf-8')).decode('utf-8'));


def st(f): return str(f)


def s(t=None):
    if t == None:
        time.sleep(1)
    else:
        time.sleep(t)


r2e = unrot;
e2r = rotten;
b64dc = base64dcd;
b64ec = base64ncd;
ncode64 = b64ec;
dcode64 = b64dc;
e = r2e
# macros
KbInt = KeyboardInterrupt
Attrib = AttributeError
mTime = os.stat(main.__file__).st_mtime;
r2e = unrot;
e2r = rotten;
b64dc = base64dcd;
b64ec = base64ncd;
ncode64 = b64ec;
dcode64 = b64dc


def ib(custom_message=''):
    tib = Timer('ib')
    custom_message = nl * 2 + custom_message
    
    message_a = nl + '☹ ' * 8 + ' E R R O R ' + ' ☹' * 8 + nl

    fp = io.StringIO()

    traceback.print_stack(file=fp)
    message_b = fp.getvalue()
        
    if 'AttributeError' in message_b:
        message_b = ''

    message = message_a + nl + message_b + 'stacktrace in ' + str(tib.show(stop=True, units='msec')) + ' msec' + custom_message + nl 
    return message
    for i in xr(l(message)):
        w(message[i],end='')
    else:
        w()

def bo():
    w('{')


def bc():
    w('}')


def srt(st=None):
    if st == None:
        w('\n')
    else:
        w(r2e(st))


r = srt

class Round(object):
    
    def __init__(self, in_obj):
        self.in_obj = str(in_obj)
        try:
            float(self.in_obj)
        except:
            raise TypeError('cannot Round() non-numbers')
    
    def trim(self, precision=2):
        vsplit = self.in_obj.split('.')
        try:
            vsplit[1] = vsplit[1][:precision]
        except:
            pass
        if vsplit[1] == None or vsplit[1] == '':
            result = int(vsplit[0])
        else:
            result = float(vsplit[0] + dt + vsplit[1])
        return result
    
    def up(self):
        x = float(self.in_obj)
        if x == int(x):
            return x + 0.1
        y = 1 * (10 ** (0 - l(str(x).split(dt)[1])))
        if int(str(x)[-1]) % 2 == 0:
            z = x + y * 2
        else:
            z = x + y
        a = str(z).split(dt)
        return float(a[0] + dt + a[1][:l(str(x).split(dt)[1])])    

    def down(self):
        x = float(self.in_obj)
        if x == int(x):
            return x - 0.1
        y = 1 * (10 ** (0 - l(str(x).split(dt)[1])))
        if int(str(x)[-1]) % 2 == 0:
            z = x - y * 2
        else:
            z = x - y
        a = str(z).split(dt)
        return float(a[0] + dt + a[1][:l(str(x).split(dt)[1])])

    def infer(self):
        return int(self.in_obj)
    

class Timer(object):

    def __init__(self, uniq_id):
        self.queries = 0
        self.uniq_id = uniq_id
        self.started = time.time()
        
    def show(self, stop=False, units='sec',cut=2):

        self.queries += 1

        timediff = time.time() - self.started
        if stop == True:
            del self.started
        if units == 'sec':
            pass
        elif units == 'msec':
            timediff *= 1000
        elif units == 'micsc':
            timediff *= 1000000
        elif units == 'min':
            timediff /= 60

        if cut != None:
            timediff = Round(timediff).trim(cut)
            return timediff
        else:
            return timediff
      
    def stop(self, suppress=False):
        timenow = time.time()
        timediff = self.started - timenow
        timedict = {'diff':timediff, 'started':self.started, 'ended':timenow, 'queries':self.queries}
        del self.started
        return timedict

class NumTools(object):
    '''
    Useful information about a list of numbers.
    '''
    def __init__(self, numlist):
        intype = type(numlist)
        arraytypes = [list, tuple, dict]
        if intype not in arraytypes:
            raise TypeError('must average a list of numbers')
        numlist = list(numlist)
        for i in range(len(numlist)):
            numlist[i] = float(numlist[i])
        self.numlist = numlist

    def mean(self):
        a = 0
        for i in range(len(self.numlist)-1):
            a += (self.numlist[i] + self.numlist[i+1])
        return a / len(self.numlist)

    def median(self, multi=False):
        sortlist = sorted(self.numlist)
        even = sortlist[(int(len(sortlist) / 2) + 1)]
        odd = sortlist[(len(sortlist) // 2)]
        if multi == False:
            if len(sortlist) % 2 == 0:
                result = even
            else:
                result = odd
            return result
        elif multi == True:
            return {'even':even, 'odd':odd}
            
    def mode(self):
        std = sorted(self.numlist)
        n, b = [[], []]
        for i in range(len(std)):
            if std.count(std[i]) > 1 and std.count(std[i]) not in n:
                n.append({'value':std[i], 'occurrences':std.count(std[i])})
        for i in range(len(n)):
            if n[i] not in b:
                b.append(n[i])
        v = b[-1]
        return v
    
    def range(self, multi=False):
        listmax = max(self.numlist)
        listmin = min(self.numlist)
        difference = listmax - listmin
        if multi == False:
            return difference
        elif multi == True:
            return {'min':listmin, 'max':listmax, 'difference':difference}
        
    def all(self):
        origin = NumTools(self.numlist)
        result = {'mean':origin.mean(), 'median':origin.median(multi=True), 'mode':origin.mode(), 'range':origin.range()}
        return result
    
'''
# get all instances of a class, really slowly, because garbage collector.
for obj in gc.get_objects():
	if isinstance(myinstance, myclass):
		pass
'''
            
# i wish I could store variables in the immediate REPL
def immediate(dev=''): # immediate repl - unfortunately no access to internal variables
    try:
        while 1:
            try:
                exec('print(' + input('\n>>> ') + ')')
            except KbInt:
                break
            except:
                fp = io.StringIO()
                traceback.print_stack(file=fp) # file descriptor: 2 ** 128 -1
                w(fp.getvalue())
    except IOError:
        ib()
        bc()


def repl():  # simple read-eval-print loop suite with plenty of functions
    qstring = '''
Pubbfr n ERCY: {
   [E]bg13
   [O]nfr64
   [U]rnqre Ercevag
   [S]vobanppv Gbbyf
   [Z]vav Clguba Oenva Grnfre
   ['''
    while 1:
        try:
            f = q(e(qstring)).lower().split(' ', 1)[0]
            if f == 'r':
                bc();r4e()
            elif f == 'b':
                bc();rB64()
            elif f == 'h':
                bc();r();bo();header();r();bc()  # r() without a string argument just prints a newline
            elif f == 'f':
                bc();rFib()
            elif f == 'm':
                bc();miniPyQuiz()
            elif f == 'zb':
                bc();printAttribLn(1);r();bc()
            elif f == 'g':
                bc();garbage(2000)
            elif f == 'gz':
                bc();garbage()
            elif f == '':
                bc()  # read junk
            else:
                ib();bc()  # read more junk
        except KbInt:
            bc();break  # make CTRL-C prettier
        # except:r('\nshapgvba haqre pbafgehpgvba');bc();r()

'''
def miniPyQuiz():  # 128 bytes to generate the competition's max output of 2047
    try:
        r()
        n = 4 ** 9;
        f = [0, 1];
        o = str;  # original source uses 'r' but that's the rot13 function in this script so it's bound to o
        for i in xr(1, n): f.append(f[i - 1] + f[i - 2])
        print(o(o(o(f[n])[:1564][::-1].split(' '))[::-1]).split('8'))  # using 'print' because w or p are not defined
        s(1)
        if q(r2e(
            '\nOenva Grnfre: jevgr yrff guna 128 olgrf bs pbqr va nal ynathntr (cersrenoyl clguba) gb tvir guvf rknpg 2047-olgr bhgchg. {\n            Uvag: 4**9gu svobanppv...')) == "":
            bc()
        else:
            bc()
    except KbInt:
        bc()
'''

def r4e():
    try:
        r('\nRatyvfu <-> Ebg13 Ernq-Riny-Cevag-Ybbc {')
        while 1:
            r(q())
    except KbInt:
        bc()


def fib(n=0, nth=None):  # fib backend
    fibnum = [0, 1]
    for i in xr(2, n):
        fibnum.append(fibnum[i - 1] + fibnum[i - 2])
    if n == 0:
        return None
    elif nth != None:
        try:
            w(fibnum[nth - 1])
        except Ind:
            b64dc(b'Y2FuJ3QgcmV0dXJuIHZhbHVlIG91dHNpZGUgbGlzdCBpbmRleCBidWZmZXI=')
    else:
        w(fibnum)


def rFib():  # repl fibonacci implementation
    r('\nSvobanppv ERCY: ergheaf svefg "a" svo ahzoref be "agu" svo {')
    try:
        while 1:
            inp = q('\n: ')
            try:
                if sr(inp[l(inp) - 2] + inp[l(inp) - 1]) == 'th':
                    try:
                        ip = int(sr(inp).split('th')[0])
                    except Val:
                        ib()
                    try:
                        if ip > 999999:
                            ib()
                        else:
                            fib(ip, ip)
                    except Val:
                        ib()
                    except Ind:
                        ib()
                    except:
                        pass
                else:
                    try:
                        inp = abs(int(inp))
                        if inp > 10000:
                            ib()
                        else:
                            fib(inp)
                    except Val:
                        ib()
            except Ind:
                ib()
    except KbInt:
        bc()


def rB64():  # repl base64 converter
    try:
        while 1:
            inp = q(e('r[a]pbqr be [q]rpbqr sbyybjrq ol fcnpr gura fgevat be olgrneenl {\n')).lower().split(' ', 1)
            try:
                if inp == '':
                    pass
                elif not inp[1]:
                    ip = abs(int(inp.split('th')[0]))
                elif inp[1]:
                    try:
                        if inp[0] == 'n' or inp[0] == 'e':
                            b64ec(inp[1])
                        elif inp[0] == 'd' or inp[0] == 'u':
                            try:
                                b64dc(bytearray(inp[1], 'utf-8'))
                            except:
                                ib()
                    except Ind:
                        ib()
                else:
                    ib()
            except Ind:
                ib()
    except KbInt:
        bc()


def garbagequit():  # a function to stop the spew of garbage.
    y = 0;
    d = ''
    while y < 50:  # print 50 lines of one char per line to clear the screen
        d = d + nl + chr(random.randint(0, ax))
        print(d)
        y += 1


def garbage(count=2 ** 128 - 1):  # generate junk and spit it out of stdout for some time(forever?)
    try:
        w(
            '   >>>   C O N T R O L - C  T O  S T O P   <<<')  # actually worthless, considering it only shows for .1 sec...
        blk = 512;
        d = ''  # blocksize. making the blocksize smaller may make it run somewhat faster, i dunno. the main reason it lags is Tk trying to keep a bazillion characters in memory.
        i = 0
        while i < count:
            n = 0
            while n < blk:
                d += chr(random.randint(0, ax))
                n += 1
            i += 1
            print(d, end='')
        garbagequit()
    except KbInt:
        garbagequit()


def sQuery(query='', typ=None,
           ln=None):  # squery as in safe_query. Not in use, however, because its only intent right now is a useful input-processing backend for a header customiser repl.
    # short of that, currently it's quite generic and doesn't even parse the input; just checks if it meets parameters and returns it. needs work.
    inp = q(query)
    if l and l(inp) <= ln:
        if typ != None:
            if typ == 'int':
                try:
                    return int(inp)
                except Val:
                    return IO
            if typ == 'float':
                try:
                    return float(inp)
                except Val:
                    return IO
            if typ == 'str':
                try:
                    return sr(inp)
                except Val:
                    return IO
            if typ == 'bool':
                try:
                    return bool(inp)
                except Val:
                    return IO
            if typ == 'exec' or typ == 'eval' or typ == 'literal':
                pass
        else:
            return inp
    else:
        raise IO


sQ = sQuery

# ascii art. y a y.

###################################################################################################################
###########################################################
#############################
####################
#############
########
######
####
###      BEGIN HEADER GENERATOR
##
#
if ETALS:
    A = e(yourGodTheCreatorOwner) + ', ' + ETALS + ', ' + 'et al.'
else:
    A = e(yourGodTheCreatorOwner)


def isEv(n):
    n = int(n)
    if n % 2 == 0:
        return 1
    else:
        return 0


def toEv(n, r=1):
    n = int(n);
    m = n + 1
    if isEv(n) == False:
        if r == 1:
            if isEv(m) == 1: return m
        elif r == -1:
            if isEv(n - 1) == 1: return m
        else:
            if isEv(m) == 1: return m
    elif isEv(n) == 1:
        return n


def cmt():  # not country music television
    di = time.time() - mTime  # difference in seconds
    mn = int(di % 3600 / 60)  # to minutes
    hr = int(di // 3600)  # to hours
    dy = hr // 24  # to days
    wk = dy // 7  # to weeks
    mt = dy // 30  # to months
    yr = mt // 12  # to years
    ms = st(mn);
    hs = st(hr);
    ds = st(dy);
    ws = st(wk);
    ms = st(mt);
    ys = st(yr)  # make string copies
    vb = '(yrff guna n zvahgr ntb)'  # less than a minute ago
    if hr + mn == 0:
        return vb  # total hrmm to check if any time has passed
    # this could be a third shorter if not for plurals...
    elif yr >= 5:
        return '(unys n qrpnqr ntb: png, zneel nyrk!)'  # marry bf
    elif yr > 1:
        return '(' + ys + ' lrnef ntb)'
    elif yr > 0:
        return '(n lrne ntb)'
    elif mt > 1:
        return '(' + ms + ' zbaguf ntb)'
    elif mt > 0:
        return '(n zbagu ntb)'
    elif wk > 1:
        return '(' + ws + ' jrrxf ntb)'
    elif wk > 0:
        return '(n jrrx ntb)'
    elif dy > 1:
        return '(' + ds + ' qnlf ntb)'
    elif dy > 0:
        return '(n qnl ntb)'
    elif hr > 1:
        return '(' + hs + ' ubhef ntb)'
    elif hr > 0:
        return '(n ubhe ntb)'
    elif mn > 1:
        return '(' + ms + ' zvahgrf ntb)'
    elif mn > 0:
        return '(nobhg n zvahgr ntb)'  # a minute ago
    elif mn == 0:
        return vb  # as above


def fN():
    sN = os.path.basename(__file__);
    mN = os.path.basename(main.__file__)
    if main.__file__ == __file__:
        return sN
    else:
        return mN + ' <- ' + sN


try:
    wid, j = shutil.get_terminal_size();
    wid = toEven(wid);
except:
    wid = 80
wid = 90
bw = int(.85 * wid);
bwin = bw - 2;
bwinpad = bwin - 2;
adj = 1;
sp = ' ';
spin = sp * bwin;
idt = toEv((wid - bw) / 2, -1) * sp;
hz_t = '═';
hz_b = '═';
vl = '║';
vr = '║';
clt = '╔';
crt = '╗';
clb = '╚';
crb = '╝'
if clt == '[':
    bwintop = bwin + 2;hzt_bw = (hz_t * bwintop)
elif clt == '╔':
    bwintop = bwin;hzt_bw = (hz_t * bwintop)
else:
    bwintop = bwin;hzt_bw = sp + (hz_t * bwintop)


def printAttribLn(zb=''):
    hzb_bw = hz_b * bwin;
    Lop = [e('svyranzr:'), e('nhguberq ol'), e('ba'), e('erqvfgevohgnoyr haqre gur')];
    Lnd = [fN(), A, time.strftime(e('%q-%z-%L @ %U:%Z:%F HGP'), time.gmtime(mTime)) + sp + e(cmt()),
           e('TAH TCYi3 || <uggc://sfs.bet>')]

    def cMn(u):
        return toEv(bwin - (l(Lop[u]) + l(Lnd[u])), -1) // 2

    def cRMn(u):
        return 0 - (1 - (toEv(((bwin - (l(Lop[u]) + l(Lnd[u]))) // 2), -1)))

    def cL(u):
        return l(Lmn[u]) + l(Lop[u]) + l(Lnd[u]) + cRMn(u)

    def cRDf(u):
        return LmR[u] - (lof[u] - bwin)

    def cRMnSp(u):
        return (LmRAj[u]) - adj

    Lmn = [cMn(i) * sp for i in xr(4)]
    LmR = [cRMn(i) for i in xr(4)]
    lof = [cL(i) for i in xr(4)]
    LmRAj = [cRDf(i) for i in xr(4)]
    LmRsp = [cRMnSp(i) * sp for i in xr(4)]
    tLn = [Lmn[i] + Lop[i] + sp + Lnd[i] + LmRsp[i] for i in xr(4)]
    for i in xr(4):
        if l(tLn[i]) > bwin:
            LmnRsp[i] = int((toEv(LmRAj[i]) - adj) - (l(tLn[i]) - bwin)) * sr(sp)
    aln = [idt + vl + Lmn[i] + Lop[i] + sp + Lnd[i] + LmRsp[i] + vr + nl for i in xr(4)];
    crnTop = idt + clt + hzt_bw + crt + nl;
    preTxt = sp + idt + vl + spin + vr + nl;
    return str(nl + idt + nl + sp + crnTop + preTxt + sp + aln[0] + preTxt + sp + aln[1] + preTxt + sp + aln[2] + preTxt + sp + aln[3] + preTxt +
    idt + sp + clb + hzb_bw + crb + nl)

def header(prnt=None):
    if prnt:
        r('Cevagf n phfgbzvfnoyr urnqre jvgu pnyphyngrq naq nqwhfgnoyr znetvaf, qvzrafvbaf, naq nyvtazragf.')
    else:
        w(str(time.time() - starttime)[:10], 'msec', nl)
        for i in xr(l(printAttribLn())):
            w(printAttribLn()[i],end='')
        else:
            w()

if main.__file__ == __file__:
    header()
    # s()
    repl()

##
##   INCLUDE THIS
##
'''
# header
ax = 0x656
try:
    import head
    from head import *
    header()
except ImportError:
    from random import *
    while 1: print(chr(randint(0, ax)), end='')
# end
'''
