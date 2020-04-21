ROWS = 4
COLUMNS = 5
matrix1 = [ [0 for i in range(COLUMNS)] for j in range(ROWS) ]
print(matrix1)
matrix2 = [ [0 for i in range(COLUMNS)] * ROWS ]
print(matrix2)
matrix3 = [0] * COLUMNS
print(matrix3)
matrix4 = [[0] * COLUMNS] * ROWS
print(matrix4)