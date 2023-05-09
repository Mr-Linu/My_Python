import numpy as np

a = np.array([20, 30, 40, 50])
b = np.arange(4)
print(a)
print(b)
c = a - b
print(c)
print(a**2)

A = np.array([[1, 1], [0, 1]])
B = np.array([[2, 0], [3, 4]])

# elementwise multiplication
print(" elementwise multiplication \n", A*B)

# matrix multiplication
print("matrix multiplication \n", A@B)

# matrix multiplication
print("matrix multiplication \n", A.dot(B))

# Some operations, such as += and *=, act in place to modify an existing array rather than create a new one.
a = np.ones((2,3), dtype=int)
b = np.random.random((2,3))

print(a)
a *= 3
print(a)

b += a
print(b)

print(b.sum())
print(b.max())
print(b.sum(axis=1))
print(b.cumsum(axis=1))

# UNIVERSAL FUNCTIONS
print("B \n", B)
print("Exponent of B\n", np.exp(B))

print("B \n", B)
print("sqrt of B\n", np.sqrt(B))
