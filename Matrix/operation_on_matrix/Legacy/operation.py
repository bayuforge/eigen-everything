def classic_multiplication(A:list, B:list):
    a_dimension = matrixTools.dimension_calculator(A) # row x col -> dict
    b_dimension = matrixTools.dimension_calculator(B) # row x col -> dict
    c_prime = [[0 for x in range(a_dimension["row"])] for x in range(b_dimension["column"])]
    c = []

    # row multiplication (dot product)
    for i in range(a_dimension["row"]):
        for j in range(b_dimension["column"]):
            c_prime[i] = B[j][i] * A[i][j]
            c_prime[i] = B[j+1][i] * A[i][j+1]

    # sum of dot product
    for m in range(a_dimension["row"]):
        for n in range(b_dimension["column"]):
            c[m][n] = c_prime[m][n] + c_prime[m][n+1]
    
    return c

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

class matrixTools():
    def column_traversal(a_dash:list):
        result = [row[0] for row in a_dash]

        return result

    def dimension_calculator(A:list):
        a_dash = [s[0] for s in A]
        
        dimension = {
            "row": len(a_dash),
            "column": int(len(A[0]))
        }

        return dimension
    
    #def dot_product_summation(A:list):
