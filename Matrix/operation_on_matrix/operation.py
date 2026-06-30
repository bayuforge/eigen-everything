def classic_multiplication(A:list, B:list):
    c = [0, 0]
    c_prime = [0, 0] # for storing the object
    A_dash = [] # another matrix to store the outer layer of matrix B
    first_matrix_length = len(A)
    second_matrix_length = len(B)

    # check outer layer for second matrix
    for i in range(first_matrix_length):
        A_dash.append(A[i][1]) # perform operation to find the last node in the matrix for each column
    first_outer = A_dash

    # check outer layer for the first matrix
    second_outer = B[0] # outer of the left-side is the first row

    length_a = len(first_outer)
    length_b = len(second_outer)

    if len(first_outer) == len(second_outer):
        # make an empty matrix C with the right size to fill in the transformation
        c_prime = [[0 for _ in range(len(first_outer))] for _ in range(len(second_outer))]
        #print(f"Empty C matrix: {C}")
        
        # do the transformation
        for i in range(length_a):
            for j in range(length_b):
                c_prime[i][j] = A[i][j] * B[i][j]
            for k in range(length_b):
                c[i][k] = c_prime[i][k] + c_prime[k][i]

        return c_prime
    else:
        print(first_outer, second_outer)
        print("Math error. Both matrix are not in the same dimensions!")


# Hadamard product is an element-wise multiplication operation on matrix
def hadamard_product(A:list, B:list):
    C:list = A
    first_matrix_length = len(A)
    second_matrix_length = len(B)

    if first_matrix_length != second_matrix_length:
        return "You need to have both the same matrix size! Hadamard Product is an element-wise operations."
    else:
        # element-wise multiplication operations
        for i in range(first_matrix_length):
            for j in range(second_matrix_length):
                C[i][j] = A[i][j] * B[i][j]
        
        return C


def addition(A:list, B:list):
    C:list = A
    first_matrix_length = len(A)
    second_matrix_length = len(B)
    
    if first_matrix_length != second_matrix_length:
        return "You need to have both the same matrix size! Matrix addition is an element-wise operations."
    else:
        # element-wise addition operations
        for i in range(first_matrix_length):
            for j in range(second_matrix_length):
                C[i][j] = A[i][j] + B[i][j]
        
        return C
