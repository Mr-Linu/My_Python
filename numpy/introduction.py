import numpy as np
from numpy import pi

# creating a numpy array
a = np.arange(15).reshape(3, 5)
print(a)
print(a.size)
print(a.shape)
print(a.ndim)
print(a.dtype)
print(type(a))

# creating a numpy array from list
b = np.array([[4, 6, 2], [5, 4, 3]])
print(b)
print(type(b))

# creating a numpy array from list and indicating the type
c = np.array([[4, 6, 2], [-5, 4, 3]], dtype=complex)
print(c)
print(type(c))

# creating arrays with ones, zeros and empty
ones = np.ones([2, 3])
zeros = np.zeros([2, 3])
empty = np.empty((2, 3))

print(ones)
print(zeros)
print(empty)

# creating arrays with linspace : - takes number of elements to generate
linspace = np.linspace(0, 3, 9)
print(linspace)

print("\n printing pi * 2 as x")
x = np.linspace(0, 2 * pi, 100)
print(pi, pi*2)
print(x)

print("\n print sin x ")
f = np.sin(x)
print(f)

