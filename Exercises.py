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
def biggerIsGreater(w):
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


