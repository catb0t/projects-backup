#!/usr/bin/env python3

import re; print(re.findall(r'^([\d|\w]+) import ([\d|\w|,| |*]+)$', ' '.join('$ARGS'.split(' ')[1:])))
