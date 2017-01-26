# /*
# * This program is free software; you can redistribute it and/or modify
# * it under the terms of the GNU General Public License as published by
# * the Free Software Foundation; either version 2 of the License, or
# * (at your option) any later version.
# *
# * This program is distributed in the hope that it will be useful,
# * but WITHOUT ANY WARRANTY; without even the implied warranty of
# * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# * GNU General Public License for more details.
# *
# * You should have received a copy of the GNU General Public License
# * along with this program; if not, write to the Free Software
# * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
# * MA 02110-1301, USA.
# *
# */

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

global crr

# this script requires unicode, as specifed by the applicant RFC.
# if your mainframe, personal workstation or dial-up modem uses EBCDIC, ANSI or middle-endian encoding instead, please refrain from crashing your system and potentially also your neighbours' by not running this script.
# overflowerrors propogate, you know.

# by running this script, you are held liable for any damages to xe.com or global-rates.com, and may be a defendant in subsequent cases.
# the author of this script is not held liable for any damages herein, as per the GPL.

# this program is built like an old pre-millenium operating system: lots of seeming protection on the high, interface levels, and very little nearer the direct network, disk and raw_bytes i/o
# the only [status:planned] feature that didn't make it in? automated call-home and error reporting. I figured I'd set up a POST method to send data in RAW image format to IMGUR and decode it on my own pc
# but that would be twice the current length. then, I thought I'd write an automated email client, but that would be a waste of time if, for instance, the user did not have installed or running an SMTP server.
# that also ended up being more work than I care to do. (also, not very secure: it could in theory, for all you know, grab and email to me whatever it wants from your computer, but I'm not going to do that because while it would be cool,
# I'm not that bad of a person.)

# explanations of Not Invented Here: https://en.wikipedia.org/wiki/Not_Invented_Here ; http://www.lmgtfy.com/?q=brian+lunduke+linux+sucks+2014+youtube

# how to use you're types good:
# https://www.destroyallsoftware.com/talks/useing-youre-types-good

# i wish I could store variables in the immediate REPL
def immediate(dev=''): # immediate repl - unfortunately no access to internal variables
    try:
        while 1:
            try:
                exec(q('\n>>> '),vars())
            except KbInt:
                raise SyntaxError
            except:
                fp = io.StringIO()
                traceback.print_stack(file=fp) # file descriptor: 2 ** 128 -1
                w(fp.getvalue())
    except:
        ib();bc()

def zx():
    while 1: print(chr(randint(0, ax)), end='')

# invented here
def rnd(var):  # round to two places, rounding down in the process, then round up. needed for tip calculation.
    vsplit = sr(var).split(dt, 2)  # split the string on the .
    rav = flt(vsplit[0] + dt + vsplit[1][:2]) + .01  # glue it back, round it up and turn it to a float
    rsplit = sr(rav).split(dt, 2)  # split it again
    return flt(rsplit[0] + dt + rsplit[1][:2])  # trim all but two decimal places and glue it back

# invented here
def unrnd(var):  # fix a bug caused by rnd(x) which results in +1c of change,interest from nowhere and 32 F = 0.01 C
    return sr(float(var) - .01)  # undo the +0.01 by rnd which is really annoying but needed, sometimes

# Not Invented Here
def toCoin(totl): # totl.
    totl = unrnd(rnd(sr(totl)))
    total = totl
    tsplit = sr(totl).split(dt, 2)  # split the string on the . -> array
    # dolladolla
    totl = flt(tsplit[0])
    tw = totl // 20
    totl %= 20
    tn = totl // 10
    totl %= 10
    fv = totl // 5
    totl %= 5
    on = totl
    # pocket change tbh
    totl = flt(tsplit[1])
    hd = totl // 50
    totl %= 50
    qw = totl // 25
    totl %= 25
    dm = totl // 10
    totl %= 10
    ni = totl // 5
    totl %= 5
    pn = totl
    # Invented here
    totl = [(tw,' twent'),
            (tn,' ten'),
            (fv,' five'),
            (on,' one'),
            (hd,' half-dollar'),
            (qw,' quarter'),
            (dm,' dime'),
            (ni,' nickel'),
            (pn,' penn')]  # info + values
    prnt = ''  # empty string

    for i in xr(l(totl)):  # iterate over them
        strng = sr(int(totl[i][0])) + totl[i][1]  # starter: remove float
        if totl[i] == 1:  # if singular...
            if i == 0 or i == 8:  # if 'odd'
                prnt += strng + 'y' + nl  # add a y
            else:
                prnt += strng + nl  # the other ones are singular already
        else:
            if i == 0 or i == 8:  # if plural and 'odd'...
                prnt += strng + 'ies' + nl  # add an ies
            else:
                prnt += strng + 's' + nl  # or an s

    w(nl + 'your change is:', total)  # print the change as a float
    w(prnt)  # then print the string we constructed.

# Not Invented Here.
def cvrt(tmp, uni, to):
    erstr = 'invalid conversion'  # duh.
    if uni == to:
        raise Val('conversion must not be of same unit!')  # that would be recursive.
    if type(tmp) != float:
        raise TypeError('temp must be float not',
                                           str(type(tmp)).split("'")[1] + ' !')  # str != float
    if uni == 'c':  # if centigrade
        if to == 'f':  # and farenheit
            # f = c * (9/5) + 32
            return tmp * (9 / 5) + 32
        elif to == 'k':
            # k = c - 273.15 = ((f - 32) * (5/9)) - 273.15
            return tmp - 273.15
        else:
            raise IO(erstr)  # why an Input/Output error for bad input? I don't know...
    elif uni == 'f':  # if f
        if to == 'c':  # and c
            # c = (f - 32) * (5/9)
            return (tmp - 32) * (5 / 9)
        elif to == 'k':
            # k = c - 273.15 = ((f - 32) * (5/9)) - 273.15
            return cvrt(tmp, 'f', 'c') - 273.15
        else:
            raise IO(erstr)
    elif uni == 'k':  # kelvins! that other, actually meaningful unit.
        if to == 'f':
            # k = c - 273.15 = ((f - 32) * (5/9)) - 273.15
            return cvrt(cvrt(tmp, 'k', 'c'), 'c', 'f')
        elif to == 'c':
            # k = c - 273.15 = ((f - 32) * (5/9)) - 273.15
            return tmp + 273.15
        else:
            raise IO(erstr)  # errors
    else:
        raise IO(erstr)  #

# not invented here.
# CONvert CURrencies, funny haha
def concur(crr, amt, uni, to):
    b = ['usd','eur','gbp','inr','aud','cad','sgd','chf','myr','jpy','cny']
    # returned by crr:
    '''locales = {0:['United States Dollar',    B[0],b[0]],
                  1:['European Union Euro',     B[1],b[1]],
                  2:['British Pound Sterling',  B[2],b[2]],
                  3:['Indian Rupee',            B[3],b[3]],
                  4:['Australian Dollar',       B[4],b[4]],
                  5:['Canadian Dollar',         B[5],b[5]],
                  6:['Singapore Dollar',        B[6],b[6]],
                  7:['Swiss Franc',             B[7],b[7]],
                  8:['Malaysian Ringgit',       B[8],b[8]],
                  9:['Japanese Yen',            B[9],b[9]],
                  10:['Chinese Yuan Renminbi',  B[10],b[10]]}'''

    # between USD and X: return X% of USD
    # between X and Y, via USD: return X% of USD, Y% of USD, and then max(x,y) percent of min(x,y)

    amt = float(amt)

    for i in xr(l(crr)):
         crr[i][2] = flt(crr[i][2])

    rt = {b[0]:flt(crr[0][2]),
          b[1]:flt(crr[1][2]),
          b[2]:flt(crr[2][2]),
          b[3]:flt(crr[3][2]),
          b[4]:flt(crr[4][2]),
          b[5]:flt(crr[5][2]),
          b[6]:flt(crr[6][2]),
          b[7]:flt(crr[7][2]),
          b[8]:flt(crr[8][2]),
          b[9]:flt(crr[9][2]),
          b[10]:flt(crr[10][2])}

    if uni == to:
        ib('must convert between two different currencies!')
    elif uni == 'usd':
        if to in rt:
            return float(rt[to] * amt)
        else:
            ib('unsupported currency')
    elif uni in rt:
        if to in rt:
            return float((rt[uni] * rt[to]) * amt)
        else:
            ib('unsupported currency')
    else:
        ib('unsupported currency')

# Invented here. Obviously.
def toKM(miles):
    miles = float(trim(float(miles)))
    # Don't. Question. Complex. Things. That. Work. E-v-e-r. E. v. e. r.
    return [trim(miles * 1.6), trim(miles)]

def trim(var):
    var = str(var)
    vsplit = var.split('.')
    vsplit[1] = vsplit[1][:2]
    result = vsplit[0] + dt + vsplit[1]
    return result

# invented here
def distance():
    try:
        astring = e('''
pbbeqvangrf-gb-qvfgnapr ERCY {
         k1,l1            k2,l2        -> xvybzrgerf :  zvyrf
    42.3601,71.0589  37.7833,122.4167  ->  4384.33   : 2740.22
''') # one may note the proper spelling of kilometres
        for i in xr(l(astring)):
            w(astring[i],end='')
        while 1:
            disterr = 'distcalc: bad input' # fail
            inp = sp.join(q(e('\n: ')).split()).lower().split(sp) # a parser!
            if l(inp) == 2:
                try:
                    #using x and y for these values was a *really* bad idea, kay?
                    inp1 = inp[0].split(',')
                    inp2 = inp[1].split(',')

                    inp1_1 = flt(inp1[0])
                    inp1_2 = flt(inp1[1])

                    inp2_1 = flt(inp2[0])
                    inp2_2 = flt(inp2[1])

                    dinp1 = abs(inp1_2 - inp2_2) * 53
                    dinp2 = abs(inp1_1 - inp2_1) * 69

                    data = [inp1_1,inp1_2,inp2_1,inp2_2,'m']
                    for i in xr(l(data)):
                        data[i] = str(data[i])

                    x = '\n Klicks: {}\n Miles : {}'

                    try:
                        result = constructUrl(data,'coord_matrix') # ask the internet
                    except:
                        result = ''

                    if result:
                        w(x.format(result[0],result[1]))
                    else:
                        a = toKM(unrnd(sr(rnd((dinp1 ** 2) + (dinp2 ** 2)) ** .5)))
                        w(x.format(a[0],a[1]))
                        del a
                except:
                    ib(disterr)
            else:
                ib(disterr)
    except KbInt:
        bc()

'''
{0: ['United States Dollar', 'USD', '1.0000'], 1: ['European Union Euro', 'EUR', '0.9036'], 2: ['British Pound Sterling', 'GBP', '0.6533'], 3: ['Indian Rupee', 'INR', '64.886'], 4: ['Australian Dollar', 'AUD', '1.4020'], 5: ['Canadian Dollar', 'CAD', '1.3191'], 6: ['Singapore Dollar', 'SGD', '1.3937'], 7: ['Swiss Franc', 'CHF', '0.9842'], 8: ['Malaysian Ringgit', 'MYR', '4.2547'], 9: ['Japanese Yen', 'JPY', '120.36'], 10: ['Chinese Yuan Renminbi', 'CNY', '6.3569']}
'''

# also invented here
def money():  # $$$
    try:
        # try to format the string
        f='║' # unicode > you
        interest = nl + sp*3 + f + nl + sp*3 + f + ' gur pheerag H.F. vagrerfg engr vf: ' + str(getInterest()) + '%'
    except:
        interest = '' # nope.
    try:
        crr = constructUrl(api='exchangec') # pronounced "exchange-c" or "exchange-eck"
        try:
            p1 = '   ╠: '
            o = ' ('
            m = ') : '
            n=t
            crr_fmt = e('''
{}
{}'''.format(p1 + crr[0][0] + o + crr[0][1] + m + sp*2 + crr[0][2] + nl +
             p1 + crr[1][0] + o + crr[1][1] + m + sp*3 + crr[1][2] + nl +
             p1 + crr[2][0] + o + crr[2][1] + m     +    crr[2][2] + nl +
             p1 + crr[3][0] + o + crr[3][1] + m + sp*10 + crr[3][2] + nl +
             p1 + crr[4][0] + o + crr[4][1] + m + sp*5 + crr[4][2] + nl +
             p1 + crr[5][0] + o + crr[5][1] + m + sp*7 + crr[5][2] + nl +
             p1 + crr[6][0] + o + crr[6][1] + m + sp*6 + crr[6][2] + nl +
             p1 + crr[7][0] + o + crr[7][1] + m + sp*11 + crr[7][2] + nl +
             p1 + crr[8][0] + o + crr[8][1] + m + sp*5 + crr[8][2] + nl +
             p1 + crr[9][0] + o + crr[9][1] + m + sp*10 + crr[9][2],
             '   ╚: ' + crr[10][0] + o + crr[10][1] + m + sp + crr[10][2]))
        except:
            crr_fmt = ''
            n=t
    except:
        crr_fmt = ''
        n=t
    try:
        if crr_fmt == '':
            crr_fmt = '\n   ╚:'
        astring = e('''
Svanapvny Pbairefvba ERCY {}

 1═╦═[G]vc:
   ║
   ╠═══: g  fho  gnk gvc ᚛᚛ gbgny
   ╚═══: 1 24.89  8  15  ᚛᚛ 31.85

 2═╦═[P]unatr:
   ║
   ╠═══: p  fho  pnfu ᚛᚛ punatr
   ╚═══: 2 65.45 100  ᚛᚛ 34.55, punatr

 3═╦═[Z]rny Gbgnyyre:
   ║
   ╠═══: z  fho  gnk gvc cnvq ᚛᚛ gbgny
   ╠═══: z 55.55  5  12  100  ᚛᚛ 69.44, pnfu
   ╚═══: 3 24.89  8  15  50   ᚛᚛ 18.15, pnfu

 4═╦═[V]agrerfg:{}
   ║
   ╠═══: v vavgvny engr ercrngf lrnef ᚛᚛ gbgny
   ╠═══: v   100   .25    12      1   ᚛᚛ 128.07
   ╚═══: 4  24.89  .28    1       1   ᚛᚛ 31.863

 5═╦═[R]kpunatr Pheerapvrf:
   ║
   ╠═══: r hfq:80 pal  ᚛᚛  508.48 PAL vf 80 HFQ
   ║{}
   '''.format('{',interest,crr_fmt))  # docstrings? no.
        '''

         3═╦═[S]bbq Gbgnyyre: nf lrg havzcyrzragrq
           ║
           ╠═══: s  fho  gnk gvc pnfu ᚛᚛ punatr
           ╚═══: 3 24.89  8   15  30  ᚛᚛ 31.85
        '''
        for i in xr(l(astring)):
            s(.001)
            w(astring[i],end='')
        while 1:  # loop until kbint
            ip = sp.join(q(e('\n: ')).split()).lower().split(sp)  # get some input, then strip its extra whitespace and split it

            if l(ip) < 3:
                pass  # do nothing if the input is out of range
            else:  # if it's the right length...
                try:
                    ip[0] = int(ip[0])
                except:
                    w(end='')

                if ip[0] == 1: # bindings = better ui direction
                        ip[0] = 't'
                elif ip[0] == 2:
                        ip[0] = 'c'
                elif ip[0] == 3:
                        ip[0] = 'm'
                elif ip[0] == 4:
                        ip[0] = 'i'
                elif ip[0] == 5:
                        ip[0] = 'e'

                if ip[0] == 't' or ip[0] == 'c':  # what are we dealing with?
                    try:
                        n = t;mo, sl, mf = ip;ip = [mo, sl, mf, n]  # try to assign it
                    except Val:
                        mo = ip[0];n = t;sl = ip[1];mf = ip[2]  # if that fails, assign more robustly
                elif ip[0] == 'i':
                    try:
                        mo, sl, mf, x1, x2 = ip  # try to assign it
                    except Val:
                        mo = ip[0];sl = ip[1];mf = ip[2];x1 = ip[3];x2 = ip[4]  # if that fails, assign more robustly
                elif ip[0] == 'm': # m sub tax tip paid
                    try:
                        mo = ip[0]
                        sl = ip[1]
                        mf = ip[2]
                        x1 = ip[3]
                        x2 = ip[4]
                    except:
                        pass
                elif ip[0] == 'e': # e curr_a:00.00 curr_b
                    try:
                        mo = ip[0]
                        sl = ip[1].split(':')
                        mf = ip[2]
                    except:
                        pass
                else:
                    ib()

                try:
                    sl = flt(sl)  # try to convert to float
                    if mo != 'e':
                        mf = flt(mf)  #
                    if mo == 'i' or mo == 'm':
                        x1 = flt(x1)  # interest-calc specific
                        x2 = flt(x2)

                except:
                    pass

                try:
                    if mo == 't':  # repls r kool
                        tax = flt(mf * .01 + n) # try pronouncing 'flt' sometime.
                        food = sl  # total up the food
                        if tax >= 2:  # why the hell are you paying triple on tax?!?!
                            ib('are you *seriously* paying like, triple on tax??')  # that's a fail!
                        w('-> ' + sr(rnd(sr((food * tax) + food))))  # math.to_str
                    elif mo == 'c':  # repls r kool
                        toCoin(mf - sl)
                    elif mo == 'i':
                        #P: principal amount (initial investment)
                        init = sl
                        #r: annual nominal interest rate (as a decimal)
                        if mf:
                            interest = mf  # set it to a variable
                        else:
                            interest = .25  # fail (not sure how we got here if it wasn't set but yknow)
                        #n: number of times the interest is compounded per year
                        repeat = x1
                        #t: number of years
                        years = x2
                        # "outsource nothing" haha o k a y
                        w('-> ' + unrnd(sr(rnd(init * ((interest / repeat) + 1) ** (repeat * years)))))
                    # extended options
                    elif mo =='m': # mo sl mf x1,2
                        sub = sl
                        tax = flt(mf * .01 + n)
                        tip = x1
                        paid = x2
                        toCoin(rnd(sr(rnd(sr(unrnd(abs(flt(sr(rnd((sub * tax) + sub) - paid)))))))))
                    elif mo == 'e': # mo sl mf
                        #crr = constructUrl(api='exchangec')
                        if crr != '':
                            w(str(sl[1]),sl[0].upper(), 'is', str(trim(concur(crr, sl[1], sl[0], mf))), mf.upper())
                        else:
                            pass
                            # test if a file containing stored rates exists and if so, read it ?
                    else:
                        ib('money: operation unsupported')  # fail
                except SyntaxError:
                    ib('money: bad input')
    except KbInt:
        bc()  # handle CTRL-C nicely
    # though my testing, the next two can't be triggered by any input.
    #except Ind:ib() # if you somehow majorly mucked up your input, fail.
    #except: ib() # who knows what kind of junk the repl gets subjected to; just blame errors on the user.

# invented here
def converTemp():
    try:
        astring = e('''
GrzcPbaireg ERCY {

  [sebz] [gb] [inyhr] -> inyhr
     S    P     32    -> 0P
     p    x     67    -> -206.13 X

  [sebz] [inyhr0] -> h:inyhr1 h:inyhr2
     S      32    -> P:0 X:-273.15
     x      0     -> S:523.68 P:273.15''')  # NOT a docstring!!
        for i in xr(l(astring)):
            w(astring[i], end='')
        while 1:
            ip = sp.join(q(e('\n: ')).split()).lower().split(sp)  # split the input on spaces
            lip = l(ip)  # get the number of tokens
            ulist = ['c', 'f', 'k']  # make a list of units
            c = 'Pragvtenqr / Prypvhf'  # this *is* a docstring... kinda.
            f = 'Sneraurvg'
            k = 'Xryivaf'
            cvVal = 'cvrt: TypeError: expected a certain type but got garbage instead'
            cvDom = 'cvrt: Input/OutputError: domain not authoritative for range'
            if lip == 2:  # if just two tokens,
                try:
                    su, tmp = ip  # try to makeuseof
                except Val:
                    ib(cvVal)  # fail
                try:
                    tmp = flt(tmp)  # if the one that should be a number, isn't a number...
                except Val:
                    ib(cvVal)  # fail!
                if su in ulist:  # if it's in the list...
                    try:
                        ulist.remove(su)  # remove it!
                        # for some reason a generator / list comprehension didn't work here.
                        reslist = [cvrt(tmp, su, ulist[0]),
                                   cvrt(tmp, su, ulist[1])]  # list of results NOT including the input! clever, eh?
                        restr = '-> {}:{} {}:{}'.format(ulist[0], \
                                                        unrnd(rnd(reslist[0])), \
                                                        ulist[1], \
                                                        unrnd(rnd(reslist[1])))  # make it look nice
                        w(restr.upper())  # uppercase it, and print
                    except:
                        ib(cvDom)  # fail!
                else:
                    ib(cvVal)  # f a i l !
            elif lip == 3:  # if three tokens...
                try:
                    su, eu, tmp = ip  # try to iterate over them
                except Val:
                    ib(cvVal)
                try:
                    tmp = flt(tmp)  # try to cast flt
                except Val:
                    pass # let error pass, knowing either it will be or was handled
                try:
                    w('-> ' + unrnd(sr(rnd(cvrt(tmp, su, eu)))), eu.upper())  # evaluate it & print
                except:
                    ib(cvDom)  # fail!
            elif lip == 1:
                if ip[0] == 'c':
                    r(c)  # docstrings...
                elif ip[0] == 'f':
                    r(f)  #
                elif ip[0] == 'k':
                    r(k)  #
                else:
                    pass  # some input should pass silently.
            else:
                pass  # *vomits*
    except KbInt:
        bc()  # handling CTRL-C is important.

# Definitely Not Invented Anywhere Ever.
def madlib():  # I wanted it to display on one line, which means change your shell's width, close it, reopen it, and rerun the program.
    try:
        u = '_'
        sh = '\n "{}!" ur fnvq {} nf ur whzcrq vagb uvf pbairegvoyr {} naq qebir bss jvgu uvf {} jvsr.{}'  # russian.

        inp = q(e(sh.format(u * 13, \
                            u * 8, \
                            u * 6, \
                            u * 11, \
                            nl + sp * 2 + 'rkpynzngvba' + sp * 13 + 'nqireo' + sp * 37 + 'abha' + sp * 26 + 'nqwrpgvir' + nl * 2) \
                  + '\n glcr jbeqf sbe gur fcnprf va gur beqre va juvpu gurl nccrne {\n : ')).split(' ')
        for i in xr(l(inp)):  # iterate over the input to ROT13 it
            inp[i] = e(inp[i])  #
        if l(inp) < 4:
            ib('libmadglibmadglib: input not within range')  # fail on not enough input
        else:
            r(sh.format(inp[0], \
                        inp[1], \
                        inp[2], \
                        inp[3], \
                        nl))  # format strings are literal hell and I hate everything about them.
    except KbInt:
        bc()

# invented not here, but elsewhere, here.
def cvrtRepl():  # simple read-eval-print-loop conversion suite with plenty of functions
    def pqstr():
        if netget('http://isup.me') != None: # simple test for network i/o
            a = '''║     ╠═⇒ Vagrerfg Engr Npphzhyngbe
║     ╚═⇒ Rkpunatr Pheerapvrf'''
        else:
            a = '║     ╚═⇒ Vagrerfg Engr Npphzhyngbe'
        qstring = '''                                 ␣       ␣
Glcr gur Pbeerfcbaqvat Yrggre // Pebjarq Ahzore // PGEY-P gb rkvg {}
   ␣     ⠉            ⠉
╔═ 1 ═╦╣ Genafnpgvbaf Pnyphyngbe
║     ║  ⠉
║     ╠═⇒ Gvc Pnyphyngbe
║     ╠═⇒ Punatr Rahzrengbe
║     ╠═⇒ Zrny Gbgnyyre
{}
║  ␣
╠═ 2 ═╦╣ Pbaireg Grzcrengherf
║     ║  ⠉
║     ╠═⇒ Pragvtenqr
║     ╠═⇒ Sneraurvg
║     ╚═⇒ Xryivaf
║  ␣
╠═ 3 ═╦╣ Qvfgnapr Orgjrra Gjb Cbvagf
║     ║  ⠉
║     ╠═⇒ Xvybzrgerf
║     ╚═⇒ Zvyrf
║  ␣
╠═ 4 ═╦╣ Znqyvo Trarengbe
║     ║  ⠉
║     ╚═⇒ Znqyvo Pbafgehpgbe
║
╚═ ? ══╣ '''.format('{', a) # also NOT a docstring. how do you make those again...? """ docstring """ ?
        for i in xr(l(qstring)):
            s(0.002)
            w(e(qstring[i]),end='')
        return ''

    while 1:
        try:
            f = q(pqstr()).lower().split(' ')[0]
            try:
                f = int(f)
                fcomp = {0:'NULL',1:'t',2:'c',3:'d',4:'m',5:'i'}
                if f in fcomp:
                    f = fcomp[f]
                else:
                    bc()
                    r()
                    bo()
                    r('\nzarzbavp abg qrsvarq!\n')
                    s(.75)
                    bc()
            except:
                pass
            if f == 'r':
                bc();r4e()  # i need my toolkit of REPLS handy.
            elif f == 'b':
                bc();rB64()  #
            elif f == 'h':
                bc();r();bo();printAttribLn();r();bc()  # r() without a string argument just prints a newline
            elif f == 'f':
                bc();rFib()  #
            elif f == 'zb':
                bc();printAttribLn(1);r();bc()  #
            elif f == 'gz':
                bc();garbage(2000)  # tricked ya!
            elif f == 'g':
                bc();garbage()  # spits out garbage forever in small blocks.
            elif f == 'i':
                bc();immediate()
            #
            elif f == 't':
                bc();money()  # choices, choices
            elif f == 'c':
                bc();converTemp()
            elif f == 'd':
                bc();distance()
            elif f == 'm':
                bc();madlib()
            elif f == 'zx':
                bc();zx()
            elif f == '':
                bc()  # read junk
            else:
                ib()
                bc()  # read more junk
        except KbInt:
            bc()
            break  # make CTRL-C prettier
        #except:r('\nshapgvba haqre pbafgehpgvba');bc();r()

#
# import netthings; from netthings import* as th*s s*hit
#

# invented here
def constructUrl(data='',api=''): # format data into a URL, to send it to api_parse
    constructErr = 'apiurlconstructor: malformed or nonexistent api or query'
    try:
        data = str(data) # as str
        if api == 'gsearch': # kinda invented here but unused for now
            gsearch_data = 'https://www.google.com/search?q=' # yay, google!
            data = data.split(' ') # query split on spaces
            for i in xr(l(data)): # easier than enum() in my opinion: set the range to the length of the array.
                gsearch_data += '+' + data[i] # genius.
            try:
                return api_parse(gsearch_data, 'gsearch') # try to download and parse the thing pointed to by the url
            except:
                ib('gsearch: malformed query') # rejected!

        elif api == 'coord_matrix': # api names: invented here
            urlquery_data = 'http://boutler.com/gps/distance/?from='
            try:
                urlquery_data += data[0] + '+' + data[1] + '&to=' + data[2] + '+' + data[3] + '&unit=' + data[4]
            except TypeError:
                ib('coord_matrix: malformed data supplicant')
            except NameError:
                pass
            except Val:
                ib('coord_matrix: malformed data supplicant')


            try:
                return api_parse(urlquery_data, 'coord_matrix') # return result
            except requests.exceptions.ConnectionError:
                ib('coord_matrix: malformed query') # rejected!

        elif api == 'exchangec':
            urlquery_data = ''
            try:
                return api_parse(api='exchangec')
            except requests.exceptions.ConnectionError:
                ib('exchangec: malformed query or protocol failure')
            except:
                pass
        else:
            ib(constructErr)
    except:
        pass

# definitely invented here
def getInterest():# placeholder callable
    return api_parse(api='interest')

# not invented here
def api_parse(page='',api=''):  # parse a webpage

    #get a page
    tree = netget(page)

    #returns federally set interest rate as float
    if api == 'interest':
        # take a webpage which has a predictable structure
        tree = netget('http://www.global-rates.com/interest-rates/central-banks/central-bank-america/fed-interest-rate.aspx')        
        try:
            #open a file for writing
            f = open('INT','w')
            # use XPath to identify the tag holding the value
            rate = tree.xpath('//*[@id="lbl_centralebankpercentage"]/text()')
            f.write(rate)
            # split it to get the number
            result = str(rate[0])[:6] # 0.250&nbsp;% -> 0.250
            # make it a number
            return float(result)
        except:
            f = open('INT','r')
            return float(f.read())
        
    # returns results as array
    elif api == 'gsearch':
        #put the first 7 results into an array
        '''
        header :
        //*[@id="rso"]/div[1]/div[1]/div/h3/a
        //*[@id="rso"]/div[1]/div[2]/div/h3/a
        //*[@id="rso"]/div[1]/div[3]/div/h3/a
        ...
        '''
        '''
        //*[@id="rso"]/div[1]/div[1]/div/div/div/div[1]
        //*[@id="rso"]/div[1]/div[2]/div/div/div/div[1]
        //*[@id="rso"]/div[1]/div[3]/div/div/div/div[1]
        ...
        '''
        gx_1 = '//*[@id="rso"]/div[1]/div[' # assuming this works.
        gx_2 = ']/div/h3/a/text()'
        gx_3 = ']/div/div/div/div[1]'
        trxp = tree.xpath
        results = [(trxp(gx_1 + '1' + gx_2), trxp(gx_1 + '1' + gx_3)),
                   (trxp(gx_1 + '2' + gx_2), trxp(gx_1 + '2' + gx_3)),
                   (trxp(gx_1 + '3' + gx_2), trxp(gx_1 + '3' + gx_3)),
                   (trxp(gx_1 + '4' + gx_2), trxp(gx_1 + '4' + gx_3)),
                   (trxp(gx_1 + '5' + gx_2), trxp(gx_1 + '5' + gx_3)),
                   (trxp(gx_1 + '6' + gx_2), trxp(gx_1 + '6' + gx_3)),
                   (trxp(gx_1 + '7' + gx_2), trxp(gx_1 + '7' + gx_3))]

        return results # and return...????? a bunch of junk unparsed text, probably

    elif api == 'coord_matrix':
        distance = tree.xpath('/html/body/form/font/form/p/table/tbody/tr[2]/td[2]/text()')
        result = distance.split(' ')[0]
        w('hello world')
        return result
        # method chaining makes me happy but I never get to do any in Python aka PEP8-thon :(
        # return netget(page).xpath('/html/body/form/font/form/p/table/tbody/tr[2]/td[2]/text()').split(' ')[0]

    elif api == 'exchangec':
        b = ['usd','eur','gbp','inr','aud','cad','sgd','chf','myr','jpy','cny']
        B = [ ]
        for i in xr(l(b)):
            B.append(b[i].upper())

        locales = {0:['United States Dollar',    B[0],b[0]],
                   1:['European Union Euro',     B[1],b[1]],
                   2:['British Pound Sterling',  B[2],b[2]],
                   3:['Indian Rupee',            B[3],b[3]],
                   4:['Australian Dollar',       B[4],b[4]],
                   5:['Canadian Dollar',         B[5],b[5]],
                   6:['Singapore Dollar',        B[6],b[6]],
                   7:['Swiss Franc',             B[7],b[7]],
                   8:['Malaysian Ringgit',       B[8],b[8]],
                   9:['Japanese Yen',            B[9],b[9]],
                   10:['Chinese Yuan Renminbi',  B[10],b[10]]}
        # Verbatim from this (>>!!non-obfuscated!!<<) website: "<!-- WARNING: Automated extraction of rates is prohibited under the Terms of Use. -->"
        # WHAT MAKES YOU THINK THAT WILL STOP ME.
        # HONESTLY.
        base_query = 'http://www.xe.com/currencyconverter/convert/?Amount=1'
        urlqueries, final_query, valist = [[],[],[]]

        for i in xr(l(locales)): # in theory these could be chained together but ???
            urlqueries.append('&From=' + B[0] + '&To=' + B[i])

        for i in xr(l(urlqueries)):
            final_query.append(base_query + urlqueries[i])

        for i in xr(l(final_query)):
            valist.append(netget(final_query[i]))
        # we now have a set of 11 html documents!
        tree = []
        try:
            for i in xr(l(valist)): # "don't use bots on our stuff!" - unobfuscated website who make it very easy to use bots on their stuff
                tree.append(valist[i].xpath('//*[@id="contentL"]/div[1]/div[1]/div/span/table/tbody/tr[1]/td[3]/text()'))
            for i in xr(l(locales)):
                locales[i][2] = tree[i][0][:6]
        except:
            pass

        if netget('http://isup.me') != None: # if there's a connection, write to the file
            f = open('CRR','w')
            for i in xr(l(locales)):
                f.write(locales[i][2] + nl)

        result = open('CRR','r').read().split('\n')
        
        for i in xr(l(result)):
            try:
                locales[i][2] = result[i]
            except:
                pass
            
        if result != None:
            return locales
        else:
            ib('exchangec: unable to open file for writing/reading')

    else:
        ib('api_parse: malformed query or no such api')

# not invented here
def netget(url='', method='get', header=None, postdata=None, silent=False):
    neterr = 'netget: requests: operation unsupported: malformed protocol'
    try:
        # try to get the page & put it in a var
        try:
            if method == 'get':
                page = requests.get(url)

            elif method == 'post':
                if header and postdata:
                    page = requests.post(url,header,postdata) # WIP: DO NOT USE
                else:
                    ib(neterr)
            else:
                ib(neterr)
        except:
            pass
        if page:
            # chromiumesque loading:
            loading = '\nTransferring data between <you> and ' + '<' + url + '>................'
            for i in xr(l(loading)):
                s(.001)
                w(loading[i], end='')
            else:
                w(nl)
            return html.fromstring(page.text) # return parseable HTML
    except:
        pass # fail silently.

# *so* not invented here.
if main.__file__ is __file__:
    cvrtRepl()
else:
    garbage()  # if calling this script from another file, spit out garbage forever.
