
class xyctl_class():

    def __init__(self):
        """x/y control"""
        self.UP = chr(65)  # A
        self.DN = chr(66)
        self.LT = chr(67)
        self.RT = chr(68)  # D

        self.DIRS = frozenset([self.UP, self.DN, self.LT, self.RT])  # membership

        self.DIRCALC = {
            self.UP: (0, 1),
            self.DN: (0, -1),
            self.LT: (-1, 0),
            self.RT: (1, 0),
        }
        self.saved = []

    def _abs_matrix_calc(self, adj_x, adj_y):
        cur_x, cur_y = xyctl.getter()
        new_x, new_y = (
            (cur_x + adj_x),
            (cur_y + adj_y)
        )

        if (new_x * new_y) < (self.term_size()[2]):
            return new_x, new_y
        else:
            util.writer(CHAR.BEL)
            raise ValueError

    def getter(self):
        """return cursor's position in terminal"""
        util.writer(CHAR.ESC + "[6n")
        pos = until("R", raw=True)
        util.writer(CHAR.CRR + CHAR.NUL * (len(pos) + 1) + CHAR.CRR)
        pos = pos[2:].split(";")
        pos[0], pos[1] = int(pos[1]), int(pos[0])
        return pos

    def absolute_setter(self, new_x, new_y):
        """set cursor position by absolute coords"""
        util.writer(CHAR.ESC + "[{};{}H".format(new_x, new_y))

    def adjust_xy(self, adj_x, adj_y):
        """adjust cursor by increments"""
        new_x, new_y = xyctl._abs_matrix_calc(adj_x, adj_y)
        xyctl.absolute_setter(new_x, new_y)

    def savepos(self):
        """save the cursor's position by appending it to a list"""
        coords = self.getter()
        self.saved.append(coords)
        return coords

    def popsaved(self, idx=-1):
        """get last saved cursor pos by popping from list, or idx"""
        new = self.saved.pop(idx)
        if new:
            self.absolute_setter(*tuple(new))
            return new

# unix

def term_size(self):
    """get terminal size on posix"""
    h, w, hp, wp = struct.unpack(
        'HHHH',
        self.fcntl.ioctl(
            0, self.termios.TIOCGWINSZ, struct.pack('HHHH', 0, 0, 0, 0)
        )
    )
    return w, h, w * h

# windows

def term_size(self, details=False):
    """get terminal winsize on nt"""
    # https://gist.github.com/jtriley/1108174#file-terminalsize-py-L31
    # stdin handle is -10
    # stdout handle is -11
    # stderr handle is -12
    h    = self.ctypes.windll.kernel32.GetStdHandle(-12)
    csbi = self.ctypes.create_string_buffer(22)
    res  = self.ctypes.windll.kernel32.GetConsoleScreenBufferInfo(h, csbi)
    if res:
        juicy_data = struct.unpack("hhhhHhhhhhh", csbi.raw)
        (
            bufx, bufy,
            curx, cury,
            wattr,
            left, top,
            right, bottom,
            maxx, maxy
        ) = juicy_data
        sizex = right - left + 1
        sizey = bottom - top + 1
        ret = sizex, sizey, sizex * sizey, juicy_data
        return ret if details else ret[:len(ret) - 1]
    else:
        raise ValueError(
            "ctypes.windll.kernel32.GetConsoleScreenBufferInfo: "
            + repr(res)
        )

        xyctl  = xyctl_class()
        xyctl.term_size = reader.term_size
