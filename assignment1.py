import sys
cmd = sys.argv[1]

import numpy as np
import matplotlib.pyplot as plt

def func(arg):
    xval = np.arange(-3.0, 3.0, 0.1)
 
    if arg == '1':
    	f = lambda x:x
        yval = f(xval)
        print "Usage: yval is filled from lambda function(x), cmd argument = ", arg
        plt.plot(xval, yval)
        plt.show()
        #print yval

    elif arg == '2':
    	f = lambda x:x**2
        yval = f(xval)
        print "Usage: yval is filled from lambda function(x**2), cmd argument = ", arg
        plt.plot(xval, yval)
        plt.show()

    elif arg == '3':
    	f = lambda x:x**3
        yval = f(xval)
        print "Usage: yval is filled from lambda function(x**3), cmd argument = ", arg
        #print yval
        plt.plot(xval, yval)
        plt.show()

    elif arg == '4':
        print "Usage: yval is filled from sine function, cmd argument = ", arg
        yval = np.sin(xval) 
        #print yval
        plt.plot(xval, yval)
        plt.show()

    elif arg == '5':
        print "Usage: yval is filled from cosine function, cmd argument = ", arg
        yval = np.cos(xval)
        #print yval
        plt.plot(xval, yval)
        plt.show()

    elif arg == '6':
        print "Usage: yval is filled from tan function, cmd argument = ", arg
        yval = np.tan(xval)
        #print yval
        plt.plot(xval, yval)
        plt.show()

    else:
        print "Usage: yval would be populated by a diff function, cmd argument =",arg
	


test = func(cmd)
