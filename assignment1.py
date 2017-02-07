import sys
cmd = sys.argv[1]

import numpy as np
import matplotlib.pyplot as plt

def func(arg):
    xval = np.arange(-5.0, 5.0, 0.1)
    f = lambda x:x
 
    if arg == '1':
        yval = f(xval)
        #print yval
    else:
        print 'yval would be populated by a diff function'
	
    plt.plot(xval, yval)
    plt.show()


test = func(cmd)
