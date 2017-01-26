class ApiParser(object):

    def __init__(self, page='', data=''):
        api_list = ['exchange', 'extendchange', 'distance', 'interest']
        if api in api_list:
            self.api = api
        else:
            raise ValueError('unsupported api!')
        self.page = page

    # sends its own requests thus no page need be supplied
    def exchange(self):
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

        base_query='http://www.xe.com/currencyconverter/convert/?Amount=1'
        tree = []
        urlqueries = []
        final_query = []
        valist = []

        for i in range(len(locales)):
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
        try:
            for i in range(len(valist)):  # "don't use bots on our stuff!" - unobfuscated website who make it very easy to use bots on their stuff
                tree.append(valist[i].xpath(
                    '//*[@id="contentL"]/div[1]/div[1]/div/span/table/tbody/tr[1]/td[3]/text()'))
            for i in range(len(locales)):
                locales[i][2] = tree[i][0][:6]
        except:
            raise requests.exceptions.ContentDecodingError('parse failed')

        if netget('http://isup.me') != None:  # if there's a connection, write to the file
            database = open('crr.db', 'w')
            for i in range(len(locales)):
                database.write(locales[i][2] + nl)

        result = database.read().split(nl)
        database.close()
        for i in range(len(locales)):
            try:
                locales[i][2] = result[i]
            except:
                pass
        try:
            for i in range(len(locales)):
                locales[i] = float(locales[i])
        except:
            raise TypeError('assertion failed!')

        if locales != None:
            return locales

    def extendchange(self):

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

        base_query = 'http://www.xe.com/currencyconverter/convert/?Amount=1'
        tree = []
        urlqueries = []
        final_query = []
        valist = []

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
            raise requests.exceptions.ContentDecodingError('parse failed')

        if netget('http://isup.me') != None:  # if there's a connection, write to the file
            database = open('CRR_EXTEND.db', 'w')
            for i in range(len(locales)):
                database.write(locales[i][2] + nl)

        result = database.read().split('\n')
        database.close()
        for i in range(len(locales)):
            try:
                locales[i][2] = result[i]
            except:
                pass

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

        if locales != None:
            return locales
