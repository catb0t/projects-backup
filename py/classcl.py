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

class Timer(object):

    def __init__(self, uniq_id):
        self.uniq_id = uniq_id
        self.started = time.time()
        
    def show(self, stop=False, units='sec'):
        timediff = time.time() - self.started
        if stop == True:
            del self.started
        if units == 'sec':
            return timediff
        elif units == 'msec':
            return timediff * 1000
        elif units == 'micsc':
            return timediff * 1000000
        elif units == 'min':
            return timediff / 60
      
    def stop(self):
        timenow = time.time()
        timediff = self.started - timenow
        timedict = {'diff':timediff, 'start':self.started, 'end':timenow}
        del self.started
        return timedict
