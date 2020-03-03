#!/usr/bin/env python
#
# max_temperature_reduce.py - Calculate maximum temperature from NCDC Global
#                             Hourly Data - Reducer part
#import collections
import sys

#res = {}
last_val = None
cpt = 0
#max_val = -sys.maxint
# loop through the input, line by line
for line in sys.stdin:
  # each line contains a key and a value separated by a tab character
  (key, val) = line.strip().split("\t")
  # Hadoop has sorted the input by key, so we get the values
  # for the same key immediately one after the other.
  # Test if we just got a new key, in this case output the maximum
  # temperature for the previous key and reinitialize the variables.
  # If not, keep calculating the maximum temperature.
  if last_val and last_val != val:
    print "%s\t%s" % (last_val, cpt)
    #res[last_val] = cpt
    cpt = 1
  else:
    cpt += 1
  last_val = val

# we've reached the end of the file, output what is left
if last_val:
  #res[last_val] = cpt
  print "%s\t%s" % (last_val, cpt)

'''
od = collections.OrderedDict(sorted(res.items()))

for k, v in od.iteritems():
'''
