import sys
cmd = sys.argv[1]

import numpy as np
import matplotlib.pyplot as plt

def func(arg):
    xval = np.arange(-5.0, 5.0, 0.1)
 
    if arg == '1':
        f = lambda x:x
        print "Usage: yval is filled from lambda function, cmd argument = ", arg
        yval = f(xval)
        #print yval
        plt.plot(xval, yval)
        plt.show()
    elif arg == '2':
        print "Usage: yval is filled from sine function, cmd argument = ", arg
        yval = np.sin(xval) 
        #print yval
        plt.plot(xval, yval)
        plt.show()
    elif arg == '3':
        print "Usage: yval is filled from cosine function, cmd argument = ", arg
        yval = np.cos(xval)
        #print yval
        plt.plot(xval, yval)
        plt.show()
    elif arg == '4':
        print "Usage: yval is filled from tan function, cmd argument = ", arg
        yval = np.tan(xval)
        #print yval
        plt.plot(xval, yval)
        plt.show()

    else:
        print "Usage: yval would be populated by a diff function, cmd argument =",arg
	


test = func(cmd)
