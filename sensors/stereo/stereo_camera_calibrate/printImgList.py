#for i in range(500,2000,20):
#for i in [600, 620, 640, 660, 680, 700, 760, 780, 800, 820, 840, 860, 880, 1040, 1060, 1080, 1120, 1100, 1160, 1180, 1260, 1280, 1300, 1320, 1340, 1360, 1380, 1400, 1420, 1440, 1540, 1560, 1580, 1600, 1720, 1800, 1820, 1840, 1860, 1880, 1900, 1940, 1960, 1980]:

import sys

for i in range(1,int(sys.argv[1]) + 1):
    print "img/cam1-%05d.ppm" % i
    print "img/cam2-%05d.ppm" % i
    