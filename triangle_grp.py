import csv
import numpy as np
import sympy
import matplotlib.pyplot as plt

from generate_matrices import mp 
# mp will multiply a list of matrices iteratively


######### ######### ######### ######### ######### #########
###### generators of the group
######### ######### ######### ######### ######### #########

# choose generators for your group here. 
# if fundamental triangle for the action of the group is not the standard
# triangle with vertices e1, e2, e3, then you will need to either change
# coordinates, or change the fundamental triangle in the subsequent
# section. You may also need to change the affine chart.

B=[[2,-1,-3],[-1,2,-1],[-1,-1,2]]

L1=(np.linalg.inv(B))[0]
L2=(np.linalg.inv(B))[1]
L3=(np.linalg.inv(B))[2]
 
R23=np.identity(3)-[(np.transpose(B))[0],[0,0,0],[0,0,0]]
R13=np.identity(3)-[[0,0,0],(np.transpose(B))[1],[0,0,0]]
R12=np.identity(3)-[[0,0,0],[0,0,0],(np.transpose(B))[2]]

S=np.matrix(np.transpose([L1,L2,L3]), dtype='float')
Sinv=np.linalg.inv(S)

newR23=mp([Sinv,R23,S])
newR13=mp([Sinv,R13,S])
newR12=mp([Sinv,R12,S])

generators=[newR23,newR13,newR12]

# beware of floating point when building your generators

######### ######### ######### ######### ######### #########
###### choice of fundamental triangle
######### ######### ######### ######### ######### #########

# the triangle used to generate the tiling has vertices E1, E2, E3. Change
# the vectors below to change the fundamental triangle.

E1=[1,0,0]
E2=[0,1,0]
E3=[0,0,1]

######### ######### ######### ######### ######### #########
###### centering affine chart at the vector v0
######### ######### ######### ######### ######### #########

# the affine chart will be parallel to the orthogonal complement of v0; it
# will be the set of solutions to the system v0 dot x = 1. Change v0 to
# change the affine chart (you will likely have to do this if you choose a
# different fundamental triangle)

v0=[1,1,1]

######### ######### ######### ######### ######### #########
###### projecting to R^2 with the matrix M
######### ######### ######### ######### ######### #########

M=[[1,0,-1],[0,-1.73205081,0]]

# this linear transformation will map e1 to e1, e2 to -sqrt(3)e2, and e3 to
# -e1

def proj(v, central_vector=v0): 
    w=mp([central_vector,v])
    a=[v[0]/w,v[1]/w,v[2]/w]
    return mp([M,a])

######### ######### ######### ######### ######### #########
###### functions to create tilings
######### ######### ######### ######### ######### #########

def draw_lines(list_of_vectors):
#   input is a list of vectors in R^2, each stored as a list of 2 real
#   numbers
    for i in range(len(list_of_vectors)-1):
        plt.plot([list_of_vectors[i][0],list_of_vectors[i+1][0]],[list_of_vectors[i][1],list_of_vectors[i+1][1]], color='blue')


def lines_tiling(matrices):
#   input is a list of 3x3 matrices, stored as
#   lists of lists 
#   draws the projection of the orbit of the fundamental triangle under the
#   the listed matrices
    for A in matrices:
        draw_lines([proj(np.dot(A,E1)),proj(np.dot(A,E2)),proj(np.dot(A,E3)),proj(np.dot(A,E1))])

def colored_tiling(matrices):
#   input is a list of 3x3 matrices, stored as lists of lists
#   draws the projection of the orbit of the filled fundamental triangle
#   under the the listed matrices
    for A in matrices:
        x_coordinates=[proj(np.dot(A,E1))[0],proj(np.dot(A,E2))[0],proj(np.dot(A,E3))[0],proj(np.dot(A,E1))[0]]
        y_coordinates=[proj(np.dot(A,E1))[1],proj(np.dot(A,E2))[1],proj(np.dot(A,E3))[1],proj(np.dot(A,E1))[1]]
        plt.fill(x_coordinates, y_coordinates, "b")

def colored_tiling_of_csv(csv_file):
#   input is the name of a csv file as a string
#   the csv file stores a list of 3x3 matrices
#   note that the csv file must be in the same folder as this script
    the_file=open(csv_file+'.csv','r')
    reader = csv.reader(the_file)
    lines = list(reader)
    for k in range(len(lines)//3):
        A=[]
        for i in range(3*k,3*k+3):
            A.append([float(j) for j in lines[i]])
        x_coordinates=[proj(np.dot(A,E1))[0],proj(np.dot(A,E2))[0],proj(np.dot(A,E3))[0],proj(np.dot(A,E1))[0]]
        y_coordinates=[proj(np.dot(A,E1))[1],proj(np.dot(A,E2))[1],proj(np.dot(A,E3))[1],proj(np.dot(A,E1))[1]]
        plt.fill(x_coordinates, y_coordinates, "b")
    the_file.close()

fig = plt.figure()
ax = fig.add_subplot()
ax.set_aspect("equal") 

colored_tiling_of_csv('3_3_6_tri_grp07')
#_tiling_of_csv('')
#lines_tiling(generators)
#colored_tiling(generators)

plt.show()

