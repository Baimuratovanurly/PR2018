
# coding: utf-8

# In[ ]:

a = input().split() 
l = len(a)
for i in range(l):
    a[i] = int(a[i])
print(a)
t = int(input())
arr.sort()
print(a)
s = len(a)
out = 0
for i in range(t):
    out = out + a[s-1]
    s = s-1
print(out)

