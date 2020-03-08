import csv
import numpy as np
import matplotlib.pyplot as plt

### this script will generate group elements that can written as a
### product of given generators length up to n
### and then write the matrices to different csv files

###### ###### ###### ###### ###### ###### ###### ###### ###### ######
# matrix multiplication
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
# generate group elements as a list
###### ###### ###### ###### ###### ###### ###### ###### ###### ######

# this function returns a list of all matrices which can be written as a
# product of exactly n generators
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
    return list_these_matrices[-1]#[len(list_these_matrices)-1]



###### ###### ###### ###### ###### ###### ###### ###### ###### ######
### generate group elements and write to csv
###### ###### ###### ###### ###### ###### ###### ###### ###### ######

# if the write mode is 'a' then this function will create a new file or
# append to an existing file. 
# if the write mode is 'w' then this function will create a new file and
# overwrites an existing file of the same name

def write_group_elts(n,genset,name_of_file,write_mode='w'):
### input a natural number, a list of matrices, and a string to name file
    if n<10:
        the_file=open(name_of_file+'0'+str(n)+'.csv',write_mode) 
    else:
        the_file=open(name_of_file+str(n)+'.csv',write_mode) 
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
###### ###### ###### ###### ###### ###### ###### ###### ###### ######

# this function which will generate group elts length up to n and write n
# many csv files, each containing elements of the group which can be
# expressed as a product of exactly k many generators for k up to n

def write_group_elts_multi_list(n,genset,name_of_file,write_mode='w'):
### input a natural number, a list of matrices, and a string to name file
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

