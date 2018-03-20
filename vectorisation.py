#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 19:47:01 2018

@author: aditya
"""

import numpy as np
a=np.array([1,2,3,4])
print(a)

import time

a=np.random.rand(1000000)
b=np.random.rand(1000000)

tic=time.time()
c=np.dot(a,b)
toc=time.time()

print(c)

print("vectorised version:"+str(1000*(toc-tic))+"ms")

c=0
tic=time.time()
for i in range(1000000):
    c+=a[i]*b[i]
 
toc=time.time()

print(c)

print("for loop:"+str(1000*(toc-tic))+"ms")    



"""
import time

a=np.random.rand(1000000)
b=np.random.rand(1000000)

tic=time.time()
c=np.dot(a,b)
toc=time.time()

print(c)

print("vectorised version:"+str(1000*(toc-tic))+"ms")

c=0
tic=time.time()
for i in range(1000000):
    c+=a[i]*b[i]


toc=time.time()

print(c)

print("for loop:"+str(1000*(toc-tic))+"ms")

output:

250345.884972
vectorised version:1.7895698547363281ms
250345.884972
for loop:593.548059463501ms
"""
