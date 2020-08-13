#!/usr/bin/env python

import sys

for line in sys.stdin:
    line = line.strip()
    words = line.split(" ")
    key = words[0]
    cantidad = int(words[1])
    print "%s\t%d" % (key, cantidad)
