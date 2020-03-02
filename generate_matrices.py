import csv
import numpy as np
#import sympy
import matplotlib.pyplot as plt
import time
start_time = time.time()

### this script will (eventually) generate all group elements that can written as a
### product of length up to n
### and then write the matrices to different csv files
### for right now it is just writing a single file. by later i will have it
### write a folder and put all the files in that folder



###### ###### ###### ###### ###### ###### ###### ###### ###### ######
#matrix multiplication
###### ###### ###### ###### ###### ###### ###### ###### ###### ######

def mp(list_of_matrices):
    X = np.identity(len(list_of_matrices[0]))
    for matrix in list_of_matrices:
        X = np.dot(X,matrix)
    return X.tolist()

def pow(matrix,exponent):
    if exponent==0:
        return np.identity(len(matrix))
    elif exponent>0:
        return mp([matrix for i in range(exponent)])
    else:
        return mp([np.linalg.inv(matrix) for i in range(abs(exponent))])

###### ###### ###### ###### ###### ###### ###### ###### ###### ######
#matrix multiplication
###### ###### ###### ###### ###### ###### ###### ###### ###### ######

def group_elts(n,genset):
    list_these_matrices=[ [] for i in range(n+1)]
    list_these_matrices[0]=[(np.identity(len(genset[0]))).tolist()]
    with_duplicate_matrices=[ [] for i in range(n+1)]
    with_duplicate_matrices[0]=[(np.identity(len(genset[0]))).tolist()]
    for j in range(n):
        for i in list_these_matrices[j]:
            for A in genset:
                with_duplicate_matrices[j+1].append(mp([A,i]))
                with_duplicate_matrices[j+1].append(mp([i,A]))
        for k in with_duplicate_matrices[j+1]:
            if k not in list_these_matrices[j+1]:
                list_these_matrices[j+1].append(k)
    return list_these_matrices[len(list_these_matrices)-1]

###### ###### ###### ###### ###### ###### ###### ###### ###### ######
### actually write the file here
###### ###### ###### ###### ###### ###### ###### ###### ###### ######

### name the csv you'd like to write here:
#name_your_matrix_list='abelian_group'
#
##the_file=open(name_your_matrix_list+'/'+name_your_matrix_list+'.csv','a')
##the_file=open(name_your_matrix_list+'.csv','a') # to write a new file, or
##append anto existing file
#the_file=open(name_your_matrix_list+'.csv','w') #to overwrite an existing
##file
#write = csv.writer(the_file)
#
#for M in group_elts(2):
#    write.writerows(M)



###### ###### ###### ###### ###### ###### ###### ###### ###### ######
### function which will generate group elts length up to n and write to csv
###### ###### ###### ###### ###### ###### ###### ###### ###### ######

#name_your_matrix_list='abelian_group'

#is the write mode is 'a' then this will create a new file or append to an
#existing file. the write mode w will overwrite an existing file
def write_group_elts(n,genset,name_of_file,write_mode='w'):
    if n<10:
        the_file=open(name_of_file+'0'+str(n)+'.csv',write_mode) #to overwrite an existing
    else:
        the_file=open(name_of_file+str(n)+'.csv',write_mode) #to overwrite an existing
    write = csv.writer(the_file)
    list_these_matrices=[ [] for i in range(n+1)]
    list_these_matrices[0]=[(np.identity(len(genset[0]))).tolist()]
    with_duplicate_matrices=[ [] for i in range(n+1)]
    with_duplicate_matrices[0]=[(np.identity(len(genset[0]))).tolist()]
    for j in range(n):
        for i in list_these_matrices[j]:
            for A in genset:
                with_duplicate_matrices[j+1].append(mp([A,i]))
                with_duplicate_matrices[j+1].append(mp([i,A]))
        for k in with_duplicate_matrices[j+1]:
            if k not in list_these_matrices[j+1]:
                list_these_matrices[j+1].append(k)
                if j==n-1:
                    write.writerows(k)
    the_file.close()


###### ###### ###### ###### ###### ###### ###### ###### ###### ######
### function which will generate group elts length up to n and write n many
### csv files, each containing elements of the group which can be expressed
### as a product of exactly k many generators for k up to n
###### ###### ###### ###### ###### ###### ###### ###### ###### ######

### required input a natural number, a list of matrices, a string
def write_group_elts_multi_list(n,genset,name_of_file,write_mode='w'):
    list_these_matrices=[ [] for i in range(n+1)]
    list_these_matrices[0]=[(np.identity(len(genset[0]))).tolist()]
    with_duplicate_matrices=[ [] for i in range(n+1)]
    with_duplicate_matrices[0]=[(np.identity(len(genset[0]))).tolist()]
    for j in range(n):
        if j<9:
            the_file=open(name_of_file+'0'+str(j+1)+'.csv',write_mode) 
        else:
            the_file=open(name_of_file+str(j+1)+'.csv',write_mode) 
        write = csv.writer(the_file)
        for i in list_these_matrices[j]:
            for A in genset:
                with_duplicate_matrices[j+1].append(mp([A,i]))
                with_duplicate_matrices[j+1].append(mp([i,A]))
        for k in with_duplicate_matrices[j+1]:
            if k not in list_these_matrices[j+1]:
                list_these_matrices[j+1].append(k)
                write.writerows(k)
        the_file.close()


#n=25
#write_group_elts_multi_list(n,generators,'abelian_grp_elts')



#B=[[2,-1,-3],[-1,2,-1],[-1,-1,2]]
#
#L1=(np.linalg.inv(B))[0]
#L2=(np.linalg.inv(B))[1]
#L3=(np.linalg.inv(B))[2]
#
#R23=np.identity(3)-[(np.transpose(B))[0],[0,0,0],[0,0,0]]
#R13=np.identity(3)-[[0,0,0],(np.transpose(B))[1],[0,0,0]]
#R12=np.identity(3)-[[0,0,0],[0,0,0],(np.transpose(B))[2]]
#
#generators=[R23,R13,R12]

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
#generators=[R23,R13,R12]

print(generators)

n=7

#write_group_elts_multi_list(n,generators,'3_3_6_tri_grp')

#write_group_elts(n,generators, '3_3_6_tri_grp')




