import sys
cmd = sys.argv[1]

import numpy as np
import matplotlib.pyplot as plt

def func(arg):
    xval = np.arange(-3.0, 3.0, 0.1)
    f = lambda x:x
 
    if arg == '1':
        print "Usage: yval is filled from lambda function, cmd argument = ", arg
        yval = f(xval)
        #print yval
        plt.plot(xval, yval)
        plt.show()

    else:
        print "Usage: yval would be populated by a diff function, cmd argument =",arg
	


test = func(cmd)
