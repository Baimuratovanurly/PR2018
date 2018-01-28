
# coding: utf-8

# In[ ]:

from pyDatalog import pyDatalog
def twice(a):
    return a+a
pyDatalog.create_terms('X,Y,Z,Arr')

print('Set the X var to 1')
print(X==1)
print()
print('Assignment of 2 Vars')
print((X==True) & (Y==False))
print()

print('Assignment n times, to n values')
print(Arr.in_((0,1,2,3,4)))
print()

print('Just another case N assignment')
print(Arr.in_(range(5)))
print()

print('Filtering')
print(X.in_(range(5)) & (X<2))
print()

print('Term of function')
pyDatalog.create_terms('twice')
print((X==2) & (Y==twice(X)))
print()
print('Combination Assignment and Filtering')
print(X.in_(range(5)) & 
     Y.in_(range(5)) & 
     (Z==X*Y))
print(len(Z))

