import csv
import numpy as np
import matplotlib.pyplot as plt

from generate_matrices import *
from triangle_grp import *

import random as r

# make sure you have installed 
# * Python   3.7 * Numpy   1.18.1 * Matplotlib   3.1.3
# before running this code. if you use anaconda, you can set up the
# environment 'matrixgroups' as  instructed in the readme 


######### ######### ######### ######### ######### #########
###### centering affine chart at the vector v0
######### ######### ######### ######### ######### #########

# the affine chart will be parallel to the orthogonal complement of v0; it
# will be the set of solutions to the system v0 dot x = 1. Change v0 to
# change the affine chart (you will likely have to do this if you choose a
# different fundamental triangle)

v0=[1,1,1]

######### ######### ######### ######### ######### #########
###### project from R^3 to R^2 with the matrix M
######### ######### ######### ######### ######### #########

M=[[1,0,-1],[0,-1.73205081,0]]

# this linear transformation will map e1 to e1, e2 to -sqrt(3)e2, and e3 to
# -e1

######### ######### ######### ######### ######### #########
###### generators of the group
######### ######### ######### ######### ######### #########

# if fundamental triangle for the action of the group is not the standard
# triangle with vertices e1, e2, e3, then you will need to either change
# coordinates, or change the fundamental triangle in the subsequent
# section. You may also need to change the affine chart.

######### ######### ######### ######### ######### #########
##### EXAMPLE 1
##### (3,3,6) triangle group
######### ######### ######### ######### ######### #########
#R1=[[-1.,0.,0.],[1.,1.,0.],[3.,0.,1.]]
#R2=[[1.,1.,0.],[0,-1.,0.],[0.,1.,1.]]
#R3=[[1.,0.,1.],[0,1.,1.],[0.,0.,-1.]]
#
#generators=[R1,R2,R3]

#file_name=3_3_6_tri_grp

######### ######### ######### ######### ######### #########
##### EXAMPLE 2
##### 1- parameter family of (2,3,infty) triangle group
######### ######### ######### ######### ######### #########

## choose parameter r>1
## beware floating point!
## there is surely a better way to deal with the floating point issues

#r=1.5
#
#R0=[[-1.,0.,0.],[0.,1.,0.],[2*r,0.,1.]]
#R1=[[1.,0.,0.],[0,-1.,0.],[0.,2.,1.]]
#R2=[[1.,0.,2.],[0,1.,.5],[0.,0.,-1.]]
# 
#generators=[R0,R1,R2]
#
#my_file_name = '2_3_infty_tri_grp'

######### ######### ######### ######### ######### #########
##### EXAMPLE 3
##### 1- parameter family of (2,3,5) triangle group
######### ######### ######### ######### ######### #########

k=5
a00=r.uniform(-k,k)
a01=r.uniform(-k,k)
a02=r.uniform(-k,k)
#a10=r.uniform(-k,k)
#a11=r.uniform(-k,k)
#a12=r.uniform(-k,k)
#
#M=[[a00,a01,a02],[a10,a11,a12]]


v0=[-3,-1,1]
#v0=[a00,a01,a02]
#v0=[1,1,1] #this one is strange

print(v0)

S=[[v0[0],0,0],[0,v0[1],0],[0,0,v0[2]]]
#S=np.identity(3)
#M=[[0,2,1],[0,0,-1]]
M=np.dot([[1,0,-1],[0,-1.73205081,0]],S)

r=1 # free parameter, must be positive
c=.65450849718 # cos(pi/5)^2 # must be fixed for this example
#
R0=[[-1.,0.,0.],[0.,1.,0.],[2*c,0.,1.]]
R1=[[1.,0.,0.],[0,-1.,0.],[0.,r/2.,1.]]
R2=[[1.,0.,2.],[0,1.,2*r],[0.,0.,-1.]]
# 
generators=[R0,R1,R2]
#
my_file_name = '2_3_5_tri_grp'

#print([-1/(2*c-1),0,2*c/(2*c-1)])
#print(mp([M,[-1/(2*c-1),0,2*c/(2*c-1)]]))
#print([0,-1/(-1+r/2),r/(2*(-1+r/2))])
#print(mp([M,[0,-1/(-1+r/2),r/(2*(-1+r/2))]]))
#print([2/(2+2*r-1),2*r/(2+2*r-1),-1/(2+2*r-1)])
#print(mp([M,[2/(2+2*r-1),2*r/(2+2*r-1),-1/(2+2*r-1)]]))

######### ######### ######### ######### ######### #########
###### choice of fundamental triangle
######### ######### ######### ######### ######### #########

# the default triangle used to generate the tiling has vertices e0, e1, e2.
# change the vectors below to change the fundamental triangle.

e0=[1,0,0]
e1=[0,1,0]
e2=[0,0,1]
fundamental_tri=[e0,e1,e2]

######### ######### ######### ######### ######### #########
###### create tiling from list
######### ######### ######### ######### ######### #########

n=1
list_of_matrices=group_elts(n,generators)
colored_tiling(list_of_matrices,fundamental_tri, v0, M)

#colored_tiling([R1],fundamental_tri, v0, M)
#colored_tiling([R1,np.identity(3)],fundamental_tri, v0, M)

#print(proj(mp([R1,e1]),v0,M))

######### ######### ######### ######### ######### #########
###### generate the group and write to a text file
######### ######### ######### ######### ######### #########

#n=1

# write csv which will be called 'my_file_namen.csv' with all group
# elements that can be written as a product of exactly n generators:

#write_group_elts(n,generators,my_file_name)

# write n many csv files, each containing all group elements that can be
# written as a product of exactly k generators from k up to n

#write_group_elts_multi_list(n,generators,'my_file_name')

######### ######### ######### ######### ######### #########
###### create tiling from a text file
######### ######### ######### ######### ######### #########

#
#if n<10:
#    colored_tiling_of_csv(my_file_name+'0'+str(n),fundamental_tri, v0,M)
#else:
#    colored_tiling_of_csv(my_file_name+str(n),fundamental_tri, v0,M)

#colored_tiling([R0,R1,R2],fundamental_tri,v0,M)


#colored_tiling_of_csv('2_3_5_tri_grp01', fundamental_tri,v0,M)


