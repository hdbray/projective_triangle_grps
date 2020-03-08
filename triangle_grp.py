import csv
import numpy as np
import matplotlib.pyplot as plt

from generate_matrices import mp 
# mp will multiply a list of matrices iteratively

def proj(v, central_vector, projection_matrix): 
    w=mp([central_vector,v])
    a=[v[0]/w,v[1]/w,v[2]/w]
    return mp([projection_matrix,a])

######### ######### ######### ######### ######### #########
###### functions to create tilings
######### ######### ######### ######### ######### #########

def draw_lines(list_of_vectors):
#   input is a list of vectors in R^2, each stored as a list of 2 real
#   numbers
    for i in range(len(list_of_vectors)-1):
        plt.plot([list_of_vectors[i][0],list_of_vectors[i+1][0]],[list_of_vectors[i][1],list_of_vectors[i+1][1]], color='blue')

def plot_points(list_points):
#   input is a list of vectors in R^2, each stored as a list of 2 real
#   numbers
    for p in list_points:
        plt.plot([p[0]], [p[1]], marker='o', markersize=.5, color='red')

def lines_tiling(matrices,fund_tri,affine_center,proj_matrix): 
    fig = plt.figure()
    ax = fig.add_subplot()
    ax.set_aspect("equal")
#   matrices is a list of 3x3 matrices, stored as
#   lists of lists 
#   fund_tri is a list of vectors in R^3
#   affine_center is a vector in R^3 to center the affine chart
#   proj_matrix is a 2x3 to project from R^3 to R^2
#   draws the projection of the orbit of the fundamental triangle under the
#   listed matrices
    E0=fund_tri[0]
    E1=fund_tri[1]
    E2=fund_tri[2]
    for A in matrices:
            draw_lines([proj(np.dot(A,E0),affine_center,proj_matrix),proj(np.dot(A,E1),affine_center,proj_matrix),proj(np.dot(A,E2),affine_center,proj_matrix),proj(np.dot(A,E0),affine_center,proj_matrix)])
    plt.show()

def colored_tiling(matrices,fund_tri,affine_center,proj_matrix):
#   matrices is a list of 3x3 matrices, stored as lists of lists
#   draws the projection of the orbit of the filled fundamental triangle
#   under the listed matrices
    fig = plt.figure()
    ax = fig.add_subplot()
    ax.set_aspect("equal")
    E0=fund_tri[0]
    E1=fund_tri[1]
    E2=fund_tri[2]
    for A in matrices:
        x_coordinates=[proj(np.dot(A,E0),affine_center,proj_matrix)[0],proj(np.dot(A,E1),affine_center,proj_matrix)[0],proj(np.dot(A,E2),affine_center,proj_matrix)[0],proj(np.dot(A,E0),affine_center,proj_matrix)[0]]
        y_coordinates=[proj(np.dot(A,E0),affine_center,proj_matrix)[1],proj(np.dot(A,E1),affine_center,proj_matrix)[1],proj(np.dot(A,E2),affine_center,proj_matrix)[1],proj(np.dot(A,E0),affine_center,proj_matrix)[1]]
        plt.fill(x_coordinates, y_coordinates, "b")
    plt.show()

def colored_tiling_of_csv(csv_file,fund_tri,affine_center,proj_matrix,save_fig=True):
#   input is the name of a csv file as a string
#   the csv file stores a list of 3x3 matrices
#   note that the csv file must be in the same folder as this script
    fig = plt.figure()
    ax = fig.add_subplot()
    ax.set_aspect("equal")
    E0=fund_tri[0]
    E1=fund_tri[1]
    E2=fund_tri[2]
    the_file=open(csv_file+'.csv','r')
    reader = csv.reader(the_file)
    lines = list(reader)
    for k in range(len(lines)//3):
        A=[]
        for i in range(3*k,3*k+3):
            A.append([float(j) for j in lines[i]])
        x_coordinates=[proj(np.dot(A,E0),affine_center,proj_matrix)[0],proj(np.dot(A,E1),affine_center,proj_matrix)[0],proj(np.dot(A,E2),affine_center,proj_matrix)[0],proj(np.dot(A,E0),affine_center,proj_matrix)[0]]
        y_coordinates=[proj(np.dot(A,E0),affine_center,proj_matrix)[1],proj(np.dot(A,E1),affine_center,proj_matrix)[1],proj(np.dot(A,E2),affine_center,proj_matrix)[1],proj(np.dot(A,E0),affine_center,proj_matrix)[1]]
        plt.fill(x_coordinates, y_coordinates, "b")
    plt.show()
    if save_fig==True:
        plt.savefig(csv_file+'.png')
    the_file.close()


