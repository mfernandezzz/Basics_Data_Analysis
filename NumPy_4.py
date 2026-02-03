import numpy as np

#Why are NumPy arrays faster than regular Python lists?
#NumPy does not perform type checking while iterating through objects, NumPy uses fixed types and NumPy uses contiguous memory,

#What will the following code print?
b = np.array([[1.0, 2.0, 3.0], [3.0, 4.0, 5.0]])
print(b) #an array with two rows and three columns with the specified numbers, without the zero.

#What code would change the values in the 3rd column of both of the following NumPy arrays to 20?
a = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
a[:, 2] = 20 #the first parameter corresponds to all the rows and the second one to the column
print(a)

#What will the following code print?
c = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(np.full_like(a, 100))

#What is another way to produce the following array?
c = np.zeros((7, 7))
#print(c)
dOne = np.ones((5, 5))
dOne[2, 2] = 5
#print(dOne)
c[1:-1, 1:-1] = dOne
print(c)

#What is the value of d after running the following code?
d = np.array([1, 2, 3, 4, 5])
e = d
e[2] = 20
print(d)
print(e)

#What is the value of f after running the following code?
g = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(g)
f = np.max(g, axis=1).sum() #when the value of axis is one, correspond to the row. When is set to 0, correspond to the column.
print(f) #if the axis parameter is set to 1, the result is 15; if the axis parameter is set to 0, the result is 40.

#What code would produce the following array?
h = np.ones((2, 4))
print(h)
i = h.reshape((4, 2))
print(i)

#Given a file named data.txt with these contents:
#29, 97, 32, 100, 45
#15, 88, 5, 75, 22
#What code would produce the following array?
#[29, 32, 45, 15, 5, 22]
#Example with a data file:
#filedata = np.genfromtxt('data.txt', delimiter=',')
#outputt = filedata[filedata < 50]
#Example with a NumPy array:
dataTXT = np.array([[29, 97, 32, 100, 45], [15, 88, 5, 75, 22]])
output = dataTXT[dataTXT < 50]
print(output)

#Given the following NumPy array, answers the respective questions.
thirteen = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25], [26, 27, 28, 29, 30]])
print(thirteen)
#What code will obtain an array with the numbers 11, 12, 16, 17?
print(thirteen[2:4,:2])
#What code will obtain an array with the numbers 2, 8, 14, 20?
print(thirteen[[0, 1, 2, 3], [1, 2, 3, 4]]) #the first list correspond to the rows, and the second list correspond to the columns.
#What code will obtain an array with the numbers 4, 5, 24, 25, 29, 30?
print(thirteen[[0, 4, 5], 3:])