# Stack overflow source : https://stackoverflow.com/questions/16071310/bug-or-meant-to-be-numpy-raises-valueerror-too-many-boolean-indices-for-repe

import numpy as np

def subtract_smooth(x, y):
    y_new = y - median_filter(x, y, 1.)
    return  y_new

def median_filter(x, y, width):
    y_new = np.zeros(y.shape)
    for i in range(len(x)):
        y_new[i] = np.median(y[np.abs(x - x[i]) < width * 0.5])
    return y_new

subtract_smooth(np.array([ 1 , 2 , 3 , 4 , 5 ]),np.array([ 4 , 5 , 6 , 7 ,8 ]))