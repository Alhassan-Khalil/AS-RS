#!/usr/bin/env python

import numpy as np


## Storge [A1 , A2 ,A3]
##        [B1 , B2 ,B3]
##
storge = np.array([[1,0,3],[0,2,0]])

print(storge)


A1 = [storge[0,0] , (50 , 25)]
A2 = storge[0,1]
A3 = storge[0,2]
B1 = storge[1,0]
B2 = storge[1,1]
B3 = storge[1,2]

list = [A1, A2 , A3 ,B1 ,B2 ,B3]



print(list[0][1])
