import numpy as np
import math
# Define the matrix
A = np.array([[3, -1, 1], [-1, 5, -1], [1, -1, 3]])

# Compute the eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)

# Print the results
print("Eigenvalues:")
print(eigenvalues)
print("Eigenvectors:")
eigenvectors[1][0] = math.floor(eigenvectors[1][0]*10)
eigenvectors[1][1] = math.floor(eigenvectors[1][1]*10)
eigenvectors[1][2] = math.floor(eigenvectors[1][2]*10)
print( eigenvectors)
