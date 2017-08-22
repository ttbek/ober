#!/usr/bin/env python
'''
============================================================
Test segment grouping operations. 


Created on January 11, 2012
@author: Oren Livne <livne@uchicago.edu>
============================================================
'''
import unittest, numpy as np, impute as im, itertools

#data = [((4   , 1411), (17087656, 32965049, 15.877, 0), (2, 0)),
#        ((1413, 3215), (33013062, 51089213, 18.076, 1), (1, 2)),
#        ((0   , 3218), (16484792, 51156933, 34.672, 1), (1, 3)),
#        ((4   , 2551), (17087656, 44974493, 27.887, 1), (1, 4)),
#        ((2569, 3215), (45198494, 51089213, 5.891, 0), (0, 4)),
#        ((0   , 3218), (16484792, 51156933, 34.672, 1), (0, 5)),
#        ((4   , 100), (17087656, 27006698, 9.919, 0), (0, 6)),
#        ((805 , 3215), (27119061, 51089213, 23.970, 1), (1, 6)),
#        ((2   , 2650), (17075353, 45881315, 28.806, 0), (11, 21)),
#        ((2657, 3218), (45940934, 51156933, 5.216, 2), (10, 21)),
#        ((1   , 576), (17065079, 25228089, 8.163, 0), (31, 11)),
#        ((600 , 3218), (25444874, 51156933, 25.712, 2), (10, 31)),
#        ((2   , 1978), (17075353, 37206341, 20.131, 2), (10, 41)),
#        ((2019, 3218), (37509844, 51156933, 13.647, 0), (41, 11)),
#        ((0   , 3218), (16484792, 51156933, 34.672, 3), (51, 11)),
#        ((2   , 301), (17075353, 20993519, 3.918, 0), (61, 11)),
#        ((334 , 3218), (21363960, 51156933, 29.793, 2), (10, 61))]

data = [((50  , 100), (17087656, 32965049, 15.877, 0), (2, 0)),
        ((0   , 100), (16484792, 51156933, 34.672, 1), (1, 3)),
        ((50  , 100), (17087656, 44974493, 27.887, 1), (1, 4)),
        ((0   , 100), (16484792, 51156933, 34.672, 1), (0, 5)),
        ((50  , 100), (17087656, 27006698, 9.919, 0), (0, 6)),
        ]
haps = [0, 1, 2, 3, 4, 5, 6, 7]
s = im.segment.segment_data_to_segment_set(data)
d = s.to_group_to_color(haps)
print d
im.plots.plot_hap_coloring(s, haps)
