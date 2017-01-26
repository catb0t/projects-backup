#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
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
    from head import sp, dt, t, nl, w
    head.header()
    t1 = head.Timer(1)
except ImportError:
    from random import *
    while 1:
        print(chr(randint(0, ax)), end='')
# end

global crr, locales

def zx():
    while 1:
        print(chr(head.random.randint(0, ax)), end='')

# Not Invented Here
def toCoin(totl):
    global tsplit
    totl = str(totl)
    total = totl
    tsplit = str(totl).split(dt)
    if len(tsplit[1]) > 2:
        tsplit[1] = str(head.Round(dt + tsplit[1]).trim())[-2:]
    # dolladolla
    totl = float(tsplit[0])
    tw = totl // 20
    totl %= 20
    tn = totl // 10
    totl %= 10
    fv = totl // 5
    totl %= 5
    on = totl
    # pocket change
    totl = float(tsplit[1])
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
    totl = [(tw, 'twent'),
            (tn, 'ten'),
            (fv, 'five'),
            (on, 'one'),
            (hd, 'half-dollar'),
            (qw, 'quarter'),
            (dm, 'dime'),
            (ni, 'nickel'),
            (pn, 'penn')]  # info + values
    prnt = ''  # empty string

    for i in range(len(totl)):  # iterate over them
        strng = str(int(totl[i][0])) + sp + totl[i][1]  # starter: remove float
        if i == 0 or i == 8:
            if totl[i][0] == 1:
                prnt += strng + 'y' + nl
            elif totl[i][0] > 1 or totl[i][0] == 0:
                prnt += strng + 'ies' + nl
        else:
            if totl[i][0] == 1:
                prnt += strng + nl
            elif totl[i][0] > 1 or totl[i][0] == 0:
                prnt += strng + 's' + nl

    return [nl + 'your change is: ' + total, prnt]  # ret the change as a float and the string we constructed.

# Not Invented Here.
def cvrt(tmp, uni, to):
    erstr = 'invalid conversion'  # duh.
    if uni == to:
        raise ValueError('conversion must not be of same unit!')  # that would be recursive.
    if type(tmp) != float:
        raise TypeError('temp must be float not', str(type(tmp)).split("'")[1] + ' !')
    if uni == 'c':  # if centigrade
        if to == 'f':  # and farenheit
            # f = c * (9/5) + 32
            return tmp * (9 / 5) + 32
        elif to == 'k':
            # k = c - 273.15 = ((f - 32) * (5/9)) - 273.15
            return tmp - 273.15
        else:
            raise IOError(erstr)  # why an Input/Output error for bad input? I don't know...
    elif uni == 'f':  # if f
        if to == 'c':  # and c
            # c = (f - 32) * (5/9)
            return (tmp - 32) * (5 / 9)
        elif to == 'k':
            # k = c - 273.15 = ((f - 32) * (5/9)) - 273.15
            return cvrt(tmp, 'f', 'c') - 273.15
        else:
            raise IOError(erstr)
    elif uni == 'k':  # kelvins! that other, actually meaningful unit.
        if to == 'f':
            # k = c - 273.15 = ((f - 32) * (5/9)) - 273.15
            return cvrt(cvrt(tmp, 'k', 'c'), 'c', 'f')
        elif to == 'c':
            # k = c - 273.15 = ((f - 32) * (5/9)) - 273.15
            return tmp + 273.15
        else:
            raise IOError(erstr)
    else:
        raise IOError(erstr)
    
# not invented here.
# CONvert CURrencies, funny haha
def concur(crr, amt, uni, to):
    b = ['usd', 'eur', 'gbp', 'inr', 'aud', 'cad', 'sgd', 'chf', 'myr', 'jpy', 'cny']
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
    if type(amt) != float:
        try:
            amt = float(amt)
        except:
            pass

    for i in range(len(crr)):
        crr[i][2] = float(crr[i][2])

    rt = {b[0]: crr[0][2],
          b[1]: crr[1][2],
          b[2]: crr[2][2],
          b[3]: crr[3][2],
          b[4]: crr[4][2],
          b[5]: crr[5][2],
          b[6]: crr[6][2],
          b[7]: crr[7][2],
          b[8]: crr[8][2],
          b[9]: crr[9][2],
          b[10]: crr[10][2]}

    if uni == to:
        head.ib('must convert between two different currencies!')
    elif uni == 'usd':
        if to in rt:
            return float(rt[to] * amt)
        else:
            head.ib('unsupported currency')
    elif uni in rt:
        if to in rt:
            return amt * (rt[to] / rt[uni])
        else:
            head.ib('unsupported currency')
    else:
        head.ib('unsupported currency')

# Invented here. Obviously.
def toKM(miles):
    miles = head.Round(miles).trim()
    # Don't. Question. Complex. Things. That. Work. E-v-e-r. E. v. e. r.
    return [str(head.Round(head.Round(miles * 1.6).down()).trim()), str(head.Round(miles).trim())]

# invented here
def distance():
    try:
        astring = head.e('''
 pbbeqvangrf-gb-qvfgnapr ERCY {
      k1,l1            k2,l2        -> xvybzrgerf :  zvyrf
 42.3601,71.0589  37.7833,122.4167  ->  4384.33   : 2740.22
''')  # one may note the proper spelling of kilometres
        for i in range(len(astring)):
            w(astring[i], end='')
        while 1:
            disterr = 'distcalc: bad input'  # fail
            inp = sp.join(head.q(head.e('\n: ')).split()).lower().split(sp)  # a parser!
            if len(inp) == 2:
                try:
                    # using x and y for these values was a *really* bad idea, kay?
                    inp1 = inp[0].split(',')
                    inp2 = inp[1].split(',')

                    inp1_1 = float(inp1[0])
                    inp1_2 = float(inp1[1])

                    inp2_1 = float(inp2[0])
                    inp2_2 = float(inp2[1])

                    dinp1 = abs(inp1_2 - inp2_2) * 53
                    dinp2 = abs(inp1_1 - inp2_1) * 69

                    data = [inp1_1, inp1_2, inp2_1, inp2_2, 'm']
                    for i in range(len(data)):
                        data[i] = str(data[i])

                    xstr = '\n Klicks: {}\n Miles : {}'

                    try:
                        result = constructUrl(data=data, api='coord_matrix')  # ask the internet
                        if result != None or type(result) != None:
                            w(xstr.format(result[0], result[1]))
                    except:
                        a = toKM(head.Round((dinp1 ** 2) + (dinp2 ** 2)).trim() ** .5)
                        w(xstr.format(a[0], a[1]))
                except IOError:
                    head.ib(disterr)
            else:
                head.ib(disterr)
    except KeyboardInterrupt:
        head.bc()

def mkcxepre():
    cxe = api_parse(api='extendchange')
    w()
    a = ''
    for i in range(len(cxe)):
        if len(cxe[i][2]) == 7:
            a += cxe[i][2] + '0' + sp * 4 + cxe[i][1] + sp * 4 + cxe[i][0] + nl
        else:
            a += cxe[i][2] + sp * 4 + cxe[i][1] + sp * 4 + cxe[i][0] + nl
    return a
    
def mkcxe():
    cxe = mkcxepre().split('\n')
    
    for i in range(len(cxe)):
        diff = 60 - len(cxe[i])
        if diff != 0:
            cxe[i] += sp * diff + nl
    a = ''
    for i in range(len(cxe)):
        a += cxe[i]
        
    for i in range(len(a)):
        head.s(0.005)
        if a[i] == '\n':
            head.s(0.7)
        w(a[i], end='')

# also invented here
def money():  # $$$
    eq = '  ==  '
    try:
        # try to format the string
        f = '║'  # unicode > you
        interest = nl + sp * 4 + f + nl + sp * 4 + f + ' gur pheerag H.F. vagrerfg engr vf: ' + str(
            getInterest()) + '%'
    except:
        interest = ''  # nope.
    try:
        w()
        crr = constructUrl(api='exchangec')  # pronounced "exchange-c" or "exchange-eck"
        try:
            p1 = sp*4 + '╠: '
            o = ' ('
            m = ')'
            n = t
            y = []
            def fmtstr(swid=2):
                fstr = nl
                for i in range(len(crr)):
                    if i != 10:
                        fstr += p1 + crr[i][0] + o + crr[i][1] + m + sp + crr[i][2] + nl
                    else:
                        fstr += sp * 4 + '╚: ' + crr[10][0] + o + crr[10][1] + m + sp + crr[10][2]
                return fstr

            def iterstr(i,u):
                if i != 10:
                    return p1 + crr[i][0] + o + crr[i][1] + m + sp * u + crr[i][2] + nl
                else:
                    return sp * 4 + '╚: ' + crr[10][0] + o + crr[10][1] + m + sp * u + crr[10][2]

            lpstr = fmtstr().split('\n')
            spstr = lpstr
            for i in range(len(lpstr)):
                if lpstr[i] == '':
                    pass
                else:
                    spstr[i] = lpstr[i]

            for i in range(len(spstr)):
                y.append(len(spstr[i]))
            x = []
            for i in range(len(y)):
                if y[i] == '' or y[i] == 0:
                    pass
                else:
                    x.append(y[i])
            w()
            mlen = max(x)
            fin = nl
            diff = ['','','','','','','','','','','']
            for i in range(len(spstr)-1):
                diff[i] = abs(mlen - x[i])
                if diff:
                    fin += iterstr(i,diff[i] + 1)

            crr_fmt = head.e(fin)

        except:
            crr_fmt = ''
            n = t
    except:
        crr_fmt = ''
        n = t
    try:
        vl = {0: (['usd', 80], 'cny'), 1: (['jpy', 800], 'chf'), 2: (['myr', 1], 'inr')}

        exstr = []

        for i in range(len(vl)):
            exstr.append(
                str(vl[i][0][1]) +
                sp + vl[i][0][0].upper() + eq +
                str(
                    head.Round(
                        concur(
                            crr, vl[i][0][1], vl[i][0][0], vl[i][1])).trim()) +
                sp + vl[i][1].upper())

        if crr_fmt == '':
            crr_fmt = '\n   ╚:'

        astring = head.e('''

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
    ╠═══: v   100   .25    12      1   ᚛᚛ 128.0731
    ╚═══: 4  24.89  .28    1       1   ᚛᚛ 31.8532

  5═╦═[R]kpunatr Pheerapvrf:
    ║
    ╠═══: r fubjnyy     ᚛᚛ [rkgraqrq pheerapl yvfg]
    ╠═══: r fubeganzr   ᚛᚛ [eryngvir pbairefvba yvfg]
    ╠═══: r n:nzg o     ᚛᚛ NZG N  ==  NZG O
    ╠═══: r hfq:80 pal  ᚛᚛ {}
    ╠═══: r wcl:800 pus ᚛᚛ {}
    ╠═══: r zle: vae    ᚛᚛ {}
    ║{}
'''.format('{', interest, head.e(exstr[0]), head.e(exstr[1]), head.e(exstr[2]), crr_fmt))  # docstrings? no.

        for i in range(len(astring)):
            head.s(.001)
            w(astring[i], end='')

        while 1:  # loop until KeyboardInterrupt
            b = ['usd', 'eur', 'gbp', 'inr', 'aud', 'cad', 'sgd', 'chf', 'myr', 'jpy', 'cny']

            ip = sp.join(head.q(head.e(nl + ': ')).split()).lower().split(sp)
            if len(ip) == 1:
                pass
            elif ip[0] == 'e' and ip[1] == 'showall':
                try:
                    mkcxe()
                except KeyboardInterrupt:
                    pass

            elif ip[0] == 'e' and ip[1] in b:
                try:
                    rt, fed, x, v = [[], [], [], '']

                    for i in range(len(b)):
                        rt.append([b[i], crr[i][2]])
                        fed.append(str(rt[i][0]))

                    for i in range(len(rt)):
                        if ip[1] in fed[i]:
                            pass
                        else:
                            x.append(
                                sp + head.Round(
                                    concur(
                                        crr, 1, ip[1], fed[i])).trim(4)[:6] +
                                sp * 3 + str(
                                    rt[i][0]).upper() + sp * 2 + crr[i][0] + nl)

                    for i in range(len(x)):
                        try:
                            v += x[i]
                        except:
                            pass
                    finstr = nl + ' 1 ' + crr[b.index(ip[1])][0] + ' is:' + nl * 2 + v
                    splstr = finstr.split(nl)
                    ln = []
                    for i in range(len(splstr)):
                        ln.append(len(splstr[i]))
                        diff = 40 - ln[i]
                        if diff != 0:
                            splstr[i] += sp * diff + nl
                    v = ''
                    for i in range(len(splstr)):
                        v += splstr[i]
                        
                    for i in range(len(v)):
                        head.s(0.003)
                        if v[i] == nl:
                            head.s(0.5)
                        w(v[i], end='')
                except KeyboardInterrupt:
                    pass

            elif len(ip) < 3:
                pass  # do nothing if the input is out of range
            else:  # if it's the right length...
                try:
                    ip[0] = int(ip[0])
                except:
                    w(end='')

                if ip[0] == 1:  # bindings = better ui direction
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
                        n = t
                        mo, sl, mf = ip
                        ip = [mo, sl, mf, n]  # try to assign it
                    except ValueError:
                        mo = ip[0]
                        n = t
                        sl = ip[1]
                        mf = ip[2]  # if that fails, assign more robustly
                elif ip[0] == 'i':
                    try:
                        mo, sl, mf, x1, x2 = ip  # try to assign it
                    except:
                        head.ib('expected 5 tokens but got garbage instead')
                elif ip[0] == 'm':  # m sub tax tip paid
                    try:
                        mo = ip[0]
                        sl = ip[1]
                        mf = ip[2]
                        x1 = ip[3]
                        x2 = ip[4]
                    except:
                        pass
                elif ip[0] == 'e':  # e curr_a:00.00 curr_b
                    if ip == [ip[0], ip[0], ip[0]]:
                        mkcxe()
                    else:
                        try:
                            mo = ip[0]
                            sl = ip[1].split(':')
                            mf = ip[2]
                        except:
                            pass
                else:
                    head.ib()

                try:
                    sl = float(sl)  # try to convert to float
                    if mo != 'e':
                        mf = float(mf)  #
                    if mo == 'i' or mo == 'm':
                        x1 = float(x1)  # interest-calc specific
                        x2 = float(x2)
                except:
                    pass

                try:
                    if mo == 't':  # repls r kool
                        tax = float(mf * .01 + n)  # try pronouncing 'float' sometime.
                        food = sl  # total up the food
                        if tax >= 2:  # why the hell are you paying triple on tax?!?!
                            head.ib('are you *seriously* paying like, triple on tax??')  # that's a fail!
                        w('-> ' + str(head.Round((food * tax) + food).trim())) # math.to_str
                    elif mo == 'c':  # repls r kool
                        result = toCoin(mf - sl)
                        w(result[0] + nl + result[1])
                    elif mo == 'i':
                        init = sl
                        if mf:
                            interest = mf
                        else:
                            interest = .25
                        repeat = x1
                        years = x2
                        w('-> ' + str(head.Round(init * ((interest / repeat) + 1) ** (repeat * years).trim(4))))
                    # extended options
                    elif mo == 'm':  # mo sl mf x1,2
                        sub = sl
                        tax = float(mf * .01 + n)
                        tip = x1
                        paid = x2
                        resultstr = toCoin(((sub * tax) + sub) - paid)
                        w(resultstr[0] + resultstr[1])
                    elif mo == 'e':  # mo sl mf
                        if crr != '':
                            if len(sl) == 2:
                                if sl[1] == '':
                                    sl[1] = '1'
                                w('->', str(sl[1]), sl[0].upper(), ' == ',
                                  str(head.Round(concur(crr, sl[1], sl[0], mf)).trim()), mf.upper())
                            else:
                                head.ib('money: invalid syntax (list index not within range)')
                        else:
                            pass
                            # test if a file containing stored rates exists and if so, read it ?
                    else:
                        head.ib('money: operation unsupported')  # fail
                except OSError:
                    head.ib('money: bad input')
    except KeyboardInterrupt:
        head.bc()  # handle CTRL-C nicely
    #though my testing, the next two can't be triggered by any input.
    except IOError:
        head.ib() # who knows what kind of junk the repl gets subjected to; just blame errors on the user.
# this is a comment
# invented here
def converTemp():
    try:
        astring = head.e('''
 GrzcPbaireg ERCY {

  [sebz] [gb] [inyhr] -> inyhr
     S    P     32    -> 0P
     p    x     67    -> -206.13 X

  [sebz] [inyhr0] -> h:inyhr1 h:inyhr2
     S      32    -> P:0 X:-273.15
     x      0     -> S:523.68 P:273.15''')  # NOT a docstring!!
        for i in range(len(astring)):
            w(astring[i], end='')
        while 1:
            ip = sp.join(head.q(head.e('\n: ')).split()).lower().split(sp)  # split the input on spaces
            lip = len(ip)  # get the number of tokens
            ulist = ['c', 'f', 'k']  # make a list of units
            c = 'Pragvtenqr / Prypvhf'  # this *is* a docstring... kinda.
            f = 'Sneraurvg'
            k = 'Xryivaf'
            cvVal = 'cvrt: TypeError: expected a certain type but got garbage instead'
            cvDom = 'cvrt: Input/OutputError: domain not authoritative for range'
            if lip == 2:  # if just two tokens,
                try:
                    su, tmp = ip  # try to makeuseof
                except ValueError:
                    head.ib(cvVal)  # fail
                try:
                    tmp = float(tmp)  # if the one that should be a number, isn't a number...
                except ValueError:
                    ib(cvVal)  # fail!
                if su in ulist:  # if it's in the list...
                    try:
                        ulist.remove(su)  # remove it!
                        # for some reason a generator / list comprehension didn't work here.
                        reslist = [cvrt(tmp, su, ulist[0]),
                                   cvrt(tmp, su,
                                        ulist[1])]  # list of results NOT including the input! clever, eh?
                        restr = '-> {}:{} {}:{}'.format(ulist[0],
                                                        head.Round(reslist[0]).trim(),
                                                        ulist[1],
                                                        head.Round(reslist[1]).trim())  # make it look nice
                        w(restr.upper())  # uppercase it, and print
                    except SyntaxError:
                        head.ib(cvDom)  # fail!
                else:
                    head.ib(cvVal)  # f a i l !
            elif lip == 3:  # if three tokens...
                try:
                    su, eu, tmp = ip  # try to iterate over them
                except ValueError:
                    head.ib(cvVal)
                try:
                    tmp = float(tmp)  # try to cast float
                except ValueError:
                    pass  # let error pass, knowing either it will be or was handled
                try:
                    w('-> ' + head.Round(cvrt(tmp, su, eu)).trim(), eu.upper())  # evaluate it & print
                except IOError:
                    head.ib(cvDom)  # fail!
            elif lip == 1:
                if ip[0] == 'c':
                    head.r(c)  # docstrings...
                elif ip[0] == 'f':
                    head.r(f)  #
                elif ip[0] == 'k':
                    head.Ar(k)  #
                else:
                    pass  # some input should pass silently.
            else:
                pass  # *vomits*
    except KeyboardInterrupt:
        head.bc()  # handling CTRL-C is important.

# Definitely Not Invented Anywhere Ever.
def madlib():  # I wanted it to display on one line, which means change your shell's width, close it, reopen it, and rerun the program.
    try:
        u = '_'
        sh = '\n "{}!" ur fnvq {} nf ur whzcrq vagb uvf pbairegvoyr {} naq qebir bss jvgu uvf {} jvsr.{}'  # russian.

        inp = head.q(head.e(sh.format(u * 13,
                            u * 8,
                            u * 6,
                            u * 11,
                            nl + sp * 2 + 'rkpynzngvba' + sp * 13 + 'nqireo' + sp * 37 + 'abha' + sp * 26 + 'nqwrpgvir' + nl * 2) \
                  + '\n glcr jbeqf sbe gur fcnprf va gur beqre va juvpu gurl nccrne {\n : ')).split(' ')
        for i in range(len(inp)):  # iterate over the input to ROT13 it
            inp[i] = head.e(inp[i])  #
        if len(inp) < 4:
            head.ib('libmadglibmadglib: input not within range')  # fail on not enough input
        else:
            r(sh.format(inp[0],
                        inp[1],
                        inp[2],
                        inp[3],
                        nl))  # format strings are literal hell and I hate everything about them.
    except KeyboardInterrupt:
        head.bc()

# invented not here, but elsewhere, here.
def cvrtRepl():  # simple read-eval-print-loop conversion suite with plenty of functions
    def pqstr():
        if netget('http://isup.me') != None:  # simple test for network i/o
            a = ''' ║      ╠═⇒ Vagrerfg Engr Npphzhyngbe
 ║      ╚═⇒ Rkpunatr Pheerapvrf'''
        else:
            a = ' ║      ╚═⇒ Vagrerfg Engr Npphzhyngbe'
        qstring = '''                                 ␣       ␣
Glcr gur Pbeerfcbaqvat Yrggre // Pebjarq Ahzore // PGEY-P gb rkvg {}
         ⠉            ⠉
    ␣   ╔═════════════════════════
 ╔═ 1 ══╣ Genafnpgvbaf Pnyphyngbe
 ║      ║ ⠉
 ║      ╠═⇒ Gvc Pnyphyngbe
 ║      ╠═⇒ Punatr Rahzrengbe
 ║      ╠═⇒ Zrny Gbgnyyre
{}
 ║  ␣   ╔══════════════════════
 ╠═ 2 ══╣ Pbaireg Grzcrengherf
 ║      ║ ⠉
 ║      ╠═⇒ Pragvtenqr
 ║      ╠═⇒ Sneraurvg
 ║      ╚═⇒ Xryivaf
 ║  ␣   ╔═════════════════════════════
 ╠═ 3 ══╣ Qvfgnapr Orgjrra Gjb Cbvagf
 ║      ║ ⠉
 ║      ╠═⇒ Xvybzrgerf
 ║      ╚═⇒ Zvyrf
 ║  ␣   ╔══════════════════
 ╠═ 4 ══╣ Znqyvo Trarengbe
 ║      ║ ⠉
 ║      ╚═⇒ Znqyvo Pbafgehpgbe
 ║      ╔═════
 ╚═ ? ══╣ '''.format('{', a)  # also NOT a docstring. how do you make those again...? """ docstring """ ?
        for i in range(len(qstring)):
            head.s(.002)
            w(head.e(qstring[i]), end='')
        return ''

    while 1:
        try:
            try:
                w(nl, 'main startup in', t1.show(stop=True), 'sec', nl)
            except:
                pass
            f = head.q(pqstr()).lower().split(' ')[0]
            try:
                f = int(f)
                fcomp = {0: 'NULL', 1: 't', 2: 'c', 3: 'd', 4: 'm', 5: 'i'}
                if f in fcomp:
                    f = fcomp[f]
                else:
                    head.bc()
                    head.r()
                    head.bo()
                    head.r('\nzarzbavp abg qrsvarq!\n')
                    head.s(.75)
                    head.bc()
            except:
                pass
            if f == 'r':
                head.bc()
                head.r4e()  # i need my toolkit of REPLS handy.
            elif f == 'b':
                head.bc()
                head.rB64()  #
            elif f == 'h':
                head.bc()
                head.r()
                head.bo()
                header()
                head.r()
                head.bc()  # r() without a string argument just prints a newline
            elif f == 'f':
                head.bc()
                head.rFib()  #
            elif f == 'gz':
                head.bc()
                head.garbage(2000)
            elif f == 'g':
                head.bc()
                head.garbage()  # spits out garbage forever in small blocks.
            elif f == 'i':
                head.bc()
                head.immediate()
            #
            elif f == 't' or f == 'e':
                head.bc()
                money()  # choices, choices
            elif f == 'c':
                head.bc()
                converTemp()
            elif f == 'd':
                head.bc()
                distance()
            elif f == 'm':
                head.bc()
                madlib()
            elif f == 'zx':
                head.bc()
                zx()
            elif f == '':
                head.bc()  # read junk
            else:
                head.ib()
                head.bc()  # read more junk
        except KeyboardInterrupt:
            head.bc()
            break  # make CTRL-C prettier
            # except:r('\nshapgvba haqre pbafgehpgvba');bc();r()

# invented here
def constructUrl(data='', api=''):  # format data into a URL, to send it to api_parse
    constructErr = 'apiurlconstructor: malformed or nonexistent api or query'
    try:
        if api != 'coord_matrix':
            data = str(data)  # as str
        elif api == 'coord_matrix':  # api names: invented here
            urlquery = 'http://boutler.com/gps/distance/?from='
            try:
                urlquery_data = urlquery + data[0] + '+' + data[1] + '&to=' + data[2] + '+' + data[3] + '&units=' + data[4]
            except TypeError:
                head.ib('coord_matrix: malformed data supplicant')
            except NameError:
                pass
            except ValueError:
                head.ib('coord_matrix: malformed data supplicant')

            try:
                return api_parse(page=urlquery_data, api='coord_matrix')  # return result
            except requests.exceptions.ConnectionError:
                head.ib('coord_matrix: malformed query')  # rejected!

        elif api == 'exchangec':
            urlquery_data = ''
            try:
                return api_parse(api='exchangec')
            except requests.exceptions.ConnectionError:
                head.ib('exchangec: malformed query or protocol failure')
            except:
                pass

        elif api == 'extendchange':
            urlquery_data = ''
            try:
                return api_parse(api='extendchange')
            except requests.exceptions.ConnectionError:
                head.ib('exchangec: malformed query or protocol failure')
            except:
                pass

        else:
            head.ib(constructErr)
    except:
        pass

# definitely invented here
def getInterest():  # placeholder callable
    return api_parse(api='interest')

# not invented here
def api_parse(page='', api=''):  # parse a webpage

    # get a page
    tree = netget(page)

    # returns federally set interest rate as float
    if api == 'interest':
        # take a webpage which has a predictable structure
        tree = netget(
            'http://www.global-rates.com/interest-rates/central-banks/central-bank-america/fed-interest-rate.aspx')

        if tree != None:
            # open a file for writing
            f = open('INT', 'w')
            # use XPath to identify the tag holding the value
            rate = tree.xpath('//*[@id="lbl_centralebankpercentage"]/text()')
            # split it to get the number
            result = str(rate[0])[:6]  # 0.250&nbsp;% -> 0.250
            f.write(result)
            # make it a number
            return float(result)
        else:
            f = open('INT', 'r')
            return f.read().split('\n')[0]

    elif api == 'coord_matrix':

        distance = tree.xpath('/html/body/form/font/form/p/table/tbody/tr[2]/td[2]/text()')
        result = distance.split(' ')[0]
        return result
        # method chaining makes me happy but I never get to do any in Python aka PEP8-thon :(
        # return netget(page).xpath('/html/body/form/font/form/p/table/tbody/tr[2]/td[2]/text()').split(' ')[0]

    elif api == 'exchangec':
        b = ['usd', 'eur', 'gbp', 'inr', 'aud', 'cad', 'sgd', 'chf', 'myr', 'jpy', 'cny']
        B = []
        for i in range(len(b)):
            B.append(b[i].upper())

        locales = {0: ['United States Dollar', B[0], b[0]],
                   1: ['European Union Euro', B[1], b[1]],
                   2: ['British Pound Sterling', B[2], b[2]],
                   3: ['Indian Rupee', B[3], b[3]],
                   4: ['Australian Dollar', B[4], b[4]],
                   5: ['Canadian Dollar', B[5], b[5]],
                   6: ['Singapore Dollar', B[6], b[6]],
                   7: ['Swiss Franc', B[7], b[7]],
                   8: ['Malaysian Ringgit', B[8], b[8]],
                   9: ['Japanese Yen', B[9], b[9]],
                   10: ['Chinese Yuan Renminbi', B[10], b[10]]}
        # Verbatim from this (>>!!non-obfuscated!!<<) website: "<!-- WARNING: Automated extraction of rates is prohibited under the Terms of Use. -->"
        # WHAT MAKES YOU THINK THAT WILL STOP ME.
        # HONESTLY.
        base_query = 'http://www.xe.com/currencyconverter/convert/?Amount=1'
        tree, urlqueries, final_query, valist = [[], [], [], []]

        for i in range(len(locales)):  # in theory these could be chained together but ???
            urlqueries.append('&From=' + B[0] + '&To=' + B[i])

        for i in range(len(urlqueries)):
            final_query.append(base_query + urlqueries[i])

        t1 = head.Timer(1)
        for i in range(len(final_query)):
            sri = str(i + 1)
            if i < len(final_query) - 1:
                w('Get #' + sri + ', ', end='')
            elif i == len(final_query) - 1:
                w('Get #' + sri + '...', nl + 'Got', sri, 'objects in', t1.show(stop=True,units='msec'), 'msec')
            valist.append(netget(final_query[i], silent=True))
        # we now have a set of 11 html documents!
        try:
            for i in range(len(
                    valist)):  # "don't use bots on our stuff!" - unobfuscated website who make it very easy to use bots on their stuff
                tree.append(valist[i].xpath(
                    '//*[@id="contentL"]/div[1]/div[1]/div/span/table/tbody/tr[1]/td[3]/text()'))
            for i in range(len(locales)):
                locales[i][2] = tree[i][0][:6]
        except:
            pass

        if netget('http://isup.me') != None:  # if there's a connection, write to the file
            f = open('CRR', 'w')
            for i in range(len(locales)):
                f.write(locales[i][2] + nl)

        result = open('CRR', 'r').read().split('\n')

        for i in range(len(locales)):
            try:
                locales[i][2] = result[i]
            except:
                pass

        # sometimes when online, this fails to be set. so, because it will always be 1, we can set it.

        locales[0][2] = '1.0000'

        if locales != None:
            return locales

    elif api == 'extendchange':

        b = ['usd', 'eur', 'gbp', 'inr', 'aud', 'cad', 'sgd', 'chf', 'myr', 'jpy', 'cny', 'nzd',
             'thb', 'huf', 'aed', 'hkd', 'mxn', 'zar', 'php', 'sek', 'idr', 'sar', 'brl', 'try',
             'kes', 'krw', 'egp', 'iqd', 'nok', 'kwd', 'rub', 'dkk', 'pkr', 'ils', 'pln', 'qar',
             'xau', 'omr', 'cop', 'clp', 'twd', 'ars', 'czk', 'vnd', 'mad', 'jod', 'bhd', 'xof',
             'lkr', 'uah', 'ngn', 'tnd', 'ugx', 'ron', 'bdt', 'pen', 'gel', 'xaf', 'fjd', 'vef',
             'byr', 'hrk', 'uzs', 'bgn', 'dzd', 'irr', 'dop', 'isk', 'xag', 'crc', 'syp']

        B = []
        for i in range(len(b)):
            B.append(b[i].upper())

        locales = {0: ['United States Dollar', B[0], b[0]], 1: ['European Union Euro', B[1], b[1]],
                   2: ['British Pound Sterling', B[2], b[2]], 3: ['Indian Rupee', B[3], b[3]],
                   4: ['Australian Dollar', B[4], b[4]], 5: ['Canadian Dollar', B[5], b[5]],
                   6: ['Singapore Dollar', B[6], b[6]], 7: ['Swiss Franc', B[7], b[7]],
                   8: ['Malaysian Ringgit', B[8], b[8]], 9: ['Japanese Yen', B[9], b[9]],
                   10: ['Chinese Yuan Renminbi', B[10], b[10]], 11: ['New Zealand Dollar', B[11], b[11]],
                   12: ['Thai Baht', B[12], b[12]], 13: ['Hungarian Forint', B[13], b[13]],
                   14: ['Emirati Dirham', B[14], b[14]], 15: ['Hong Kong Dollar', B[15], b[15]],
                   16: ['Mexican Peso', B[16], b[16]], 17: ['South African Rand', B[17], b[17]],
                   18: ['Philippine Peso', B[18], b[18]], 19: ['Swedish Krona', B[19], b[19]],
                   20: ['Indonesian Rupiah', B[20], b[20]], 21: ['Saudi Arabian Riyal', B[21], b[21]],
                   22: ['Brazilian Real', B[22], b[22]], 23: ['Turkish Lira', B[23], b[23]],
                   24: ['Kenyan Shilling', B[24], b[24]], 25: ['South Korean Won', B[25], b[25]],
                   26: ['Egyptian Pound', B[26], b[26]], 27: ['Iraqi Dinar', B[27], b[27]],
                   28: ['Norwegian Krone', B[28], b[28]], 29: ['Kuwaiti Dinar', B[29], b[29]],
                   30: ['Russian Ruble', B[30], b[30]], 31: ['Danish Krone', B[31], b[31]],
                   32: ['Pakistani Rupee', B[32], b[32]], 33: ['Israeli Shekel', B[33], b[33]],
                   34: ['Polish Zloty', B[34], b[34]], 35: ['Qatari Riyal', B[35], b[35]],
                   36: ['Gold Ounce', B[36], b[36]], 37: ['Omani Rial', B[37], b[37]],
                   38: ['Colombian Peso', B[38], b[38]], 39: ['Chiliean Peso', B[39], b[39]],
                   40: ['Taiwan New Dollar', B[40], b[40]], 41: ['Argentine Peso', B[41], b[41]],
                   42: ['Czech Koruna', B[42], b[42]], 43: ['Vietnamese Dong', B[43], b[43]],
                   44: ['Moroccan Dirham', B[44], b[44]], 45: ['Jordanian Dinar', B[45], b[45]],
                   46: ['Bahraini Dinar', B[46], b[46]], 47: ['CFA Franc', B[47], b[47]],
                   48: ['Sri Lankan Rupee', B[48], b[48]], 49: ['Ukrainian Hryvnia', B[49], b[49]],
                   50: ['Nigerian Naira', B[50], b[50]], 51: ['Tunisian Dinar', B[51], b[51]],
                   52: ['Ugandan Shilling', B[52], b[52]], 53: ['Romanian New Leu', B[53], b[53]],
                   54: ['Bangladeshi Taka', B[54], b[54]], 55: ['Peruvian Nuevo Sol', B[55], b[55]],
                   56: ['Georgian Lari', B[56], b[56]], 57: ['Central African CFA Franc BEAC', B[57], b[57]],
                   58: ['Fijian Dollar', B[58], b[58]], 59: ['Venezuelan Bolivar', B[59], b[59]],
                   60: ['Belarusian Ruble', B[60], b[60]], 61: ['Croatian Kuna', B[61], b[61]],
                   62: ['Uzbekistani Som', B[62], b[62]], 63: ['Bulgarian Lev', B[63], b[63]],
                   64: ['Algerian Dinar', B[64], b[64]], 65: ['Iranian Rial', B[65], b[65]],
                   66: ['Dominican Peso', B[66], b[66]], 67: ['Icelandic Krona', B[67], b[67]],
                   68: ['Silver Ounce', B[68], b[68]], 69: ['Costa Rican Colon', B[69], b[69]],
                   70: ['Syrian Pound', B[70], b[70]]}

        # Verbatim from this (>>!!non-obfuscated!!<<) website: "<!-- WARNING: Automated extraction of rates is prohibited under the Terms of Use. -->"
        # WHAT MAKES YOU THINK THAT WILL STOP ME.
        # HONESTLY.
        base_query = 'http://www.xe.com/currencyconverter/convert/?Amount=1'
        tree, urlqueries, final_query, valist = [[], [], [], []]

        for i in range(len(locales)):  # in theory these could be chained together but ???
            urlqueries.append('&From=' + B[0] + '&To=' + B[i])

        for i in range(len(urlqueries)):
            final_query.append(base_query + urlqueries[i])

        t1 = head.Timer(1)
        for i in range(len(final_query)):
            sri = str(i + 1)
            if i < len(final_query) - 1:
                w('Get #' + sri + ', ', end='')
            elif i == len(final_query) - 1:
                w('Get #' + sri + '...', nl + 'Got', sri, 'objects in', t1.show(stop=True, units='msec'), 'msec')
            valist.append(netget(final_query[i], silent=True))
        # we now have a set of 11 html documents!
        try:
            for i in range(len(valist)):
                # "don't use bots on our stuff!" - unobfuscated website who make it very easy to use bots on their stuff
                tree.append(valist[i].xpath(
                    '//*[@id="contentL"]/div[1]/div[1]/div/span/table/tbody/tr[1]/td[3]/text()'))
            for i in range(len(locales)): # *tries* to ensure that the highly problematic unicode character '\xa0' is never written
                x,y = (list(tree[i][0]), list(tree[i][0]))
                for n in range(len(y)-1):
                    x[n] += y[n]
                tree[i][0] = ''.join(x)
                locales[i][2] = tree[i][0][:7]
        except:
            pass
        
        try:
            if netget('http://isup.me') != None:  # if there's a connection, write to the file
                f = open('CRR_EXTEND', 'w')
                for i in range(len(locales)):
                    f.write(locales[i][2] + nl)

            result = open('CRR_EXTEND', 'r').read().split('\n')

            for i in range(len(locales)):
                try:
                    locales[i][2] = result[i]
                except:
                    pass
        except FileNotFoundError:
            pass
        # sometimes when online, this fails to be set. so, because it will always be 1, we can set it.

        for i in range(len(locales)):
            stng = locales[i][2]
            for n in range(len(stng)):
                charAt = stng[n]
                if charAt in head.string.digits or charAt in dt or charAt in nl:
                    pass
                else:
                    x = list(locales[i][2])
                    x.remove(charAt)
                    locales[i][2] = ''.join(x)

        locales[0][2] = '1.000000'
              
        if locales != None:
            return locales
        else:
            head.ib('extendchange: unable to open file for writing/reading')
    else:
        head.ib('api_parse: malformed query or no such api')

# not invented here
def netget(url='', method='get', header=None, postdata=None, silent=False):
    neterr = 'netget: requests: operation unsupported: malformed protocol'
    try:
        # try to get the page & put it in a var
        try:
            if method == 'get':
                page = head.requests.get(url)

            elif method == 'post':
                if header and postdata:
                    page = requests.post(url, header, postdata)  # WIP: DO NOT USE
                else:
                    head.ib(neterr)
            else:
                head.ib(neterr)
        except:
            pass
        if page and silent != True:
            # chromiumesque loading:
            loading = '\nTransferring data between <you> and ' + '<' + url + '>' + dt * 10
            for i in range(len(loading)):
                head.s(.001)
                w(loading[i], end='')
            else:
                w(nl)
        return head.html.fromstring(page.text)  # return parseable HTML
    except:
        pass  # fail silently.

# *so* not invented here.
if head.main.__file__ is __file__:
    cvrtRepl()
else:
    head.garbage()  # if calling this script from another file, spit out garbage forever.
