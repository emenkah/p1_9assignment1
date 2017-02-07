import sys
cmd = sys.argv[1]

import numpy as np
import matplotlib.pyplot as plt

def func(arg):
    xval = np.arange(-5.0, 5.0, 0.1)
    f = lambda x:x
 
    if arg == '1':
    	f = lambda x:x
        yval = f(xval)
        #print yval

    elif arg == '2':
    	f = lambda x:x**2
        yval = f(xval)

    elif arg == '3':
    	f = lambda x:x**3
        yval = f(xval)

    else:
        print 'yval would be populated by a diff function'
	
    plt.plot(xval, yval)
    plt.show()


test = func(cmd)
