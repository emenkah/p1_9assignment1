import sys
cmd = sys.argv[1]

import numpy as np
import matplotlib.pyplot as plt

def func(arg):
    xval = np.arange(-5.0, 5.0, 0.1)
 
    if arg == '1':
        f = lambda x:x
        yval = f(xval)
        #print yval
    elif arg == '2':
        yval = np.sin(xval) 
        #print yval
    elif arg == '3':
        yval = np.cos(xval)
        #print yval
    elif arg == '4':
        yval = np.tan(xval)
        #print yval
    else:
        print 'yval would be populated by a diff function'
	
    plt.plot(xval, yval)
    plt.show()


test = func(cmd)
