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

global wlist, noun, atcl, ajds

def getwords():
    try:
        wordoc = open('words','r').read()
        if wordoc == None or wordoc == '':
            ib('wordy: bad database: file exists but self.process does not have sufficient permissions to open it for reading')
    except:
        ib('wordy: bad database: necessary dictionary unable to be opened for reading (no such file or directory)')
    wlist = wordoc.split('\n')
    return wlist

def getetc():
    try:
        etc = open('etc','r').read()
        if etc == None or etc == '':
            ib('wordy: bad database: file exists but self.process does not have sufficient permissions to open it for reading')
    except:
        ib('wordy: bad database: necessary dictionary unable to be opened for reading (no such file or directory)')
    etclist = etc.split('\n')
    return etclist

def getall():
    try:
        pass
    except:
        pass

def craft():
    wlist = getwords()
    x = []
    for i in xr(random.randint(0,10)):
        x.append(wlist[random.randint(0,l(wlist))])
    return x

def salt():
    meat = craft()

    for i in xr(l(meat)):
        if meat[i] in noun:
            if meat[i-1] in adj:
                pass

def wordyRepl():
    try:
        while 1:
            inp = q(': ')
            if inp != None:
                salt()

    except KbInt:
        pass


if main.__file__ == __file__:
    wordyRepl()
else:
    pass
