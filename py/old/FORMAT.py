import os,datetime,sys,time;import __main__ as main #Who doesn't love a bit of ASCII art / styling??

nameovh=' Name:       ';namecnt='{0} <- {1}'.format(os.path.basename(main.__file__),os.path.basename(__file__))
authovh=' Author/s:   ';authcnt='Carter Stevens'
timeovh=' Finalised:  ';timecnt=time.strftime('%d.%m.%Y @ %H:%M:%S UTC',time.gmtime(os.stat(main.__file__).st_mtime))
gpl3ovh=' License:    ';gpl3cnt='GNU GPLv3 <fsf.org>'
x = 40;nbsp=' '
namestr=nameovh+namecnt;authstr=authovh+authcnt;timestr=timeovh+timecnt;gpl3str=gpl3ovh+gpl3cnt;

nameeol=(x-len(namestr)) * nbsp;autheol=(x-len(authstr)) * nbsp;timeeol=(x-len(timestr)) * nbsp;gpl3eol=(x-len(gpl3str)) * nbsp

#NAME line: main.py(from class.py) ...
#AUTHORS line: Carter Stevens, et al. ...
#TIME line: dd.mm.YYYY at HH:MM:SS ...
#LICENSE line: GNU GPLv3 <http://fsf.org> ...

print('''
       ________________________________________
      /                                        \\
      |{}|
      |{}{}|
      |{}{}|
      |{}{}|
      |{}{}|
      |{}|
      \\________________________________________/
'''\
      .format(\
         nbsp*x,\
         namestr,nameeol,\
         authstr,autheol,\
         timestr,timeeol,\
         gpl3str,gpl3eol,\
         nbsp*x
         )
      )
