#Exercise 1
from collections import Counter
n=int(input())
lst= list()
for _ in range(n):
    lst.append(input())
x=Counter(lst)
print(len(x))
print(*x.values());

#Exercise 2
def big(w):
    w = list(w)
    i = len(w) - 1
    while i > 0 and w[i - 1] >= w[i]:
        i -= 1
    if i <= 0:
        return 'no answer'
    j = len(w) - 1
    while w[j] <= w[i - 1]:
        j -= 1
    w[i - 1], w[j] = w[j], w[i - 1]
    w[i:] = w[len(w) - 1:i - 1:-1]
    return ''.join(w);

#Exercise 3
import math
import os
import random
import re
import sys

def bomber(n,grid):
    if n== 1:
        return grid
    if n%2 ==0:
        return ['O'*c for i in range (r)]
    n//=2
    for k in range ((n+1)%2 +1):
        newgrid =[['O']*c for i in range(r)]
        def set (x,y):
            if 0<=x<= k and 0<=y<=c:
                newgrid[x][y]='.'
        xi=[0,0,0,1,-1]
        yi=[0,-1,1,0,0]
    for x in range (r):
        for y in range (c):
            if grid[x][y]=='O':
                for i,j in zip (xi,yi):
                    set (x+i,y+j)
    grid = newgrid
    return ["".join(x) for x in grid];


