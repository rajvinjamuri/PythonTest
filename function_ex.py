import numpy as np

vacationMatrix = np.array({1,2,3],[4,5,6],[7,8,9])
row_size = 3
columm_size = 3

def resetMatrix(my_matrix, my_row_size, my_column_size):
	print(my_matrix)
	for i in my_row_size:
		for j in my_column_size:
			my_matrix[i, j] = my_matrix[i,j]*2
			print("iterated")
	print(my_matrix)
	print("done")

resetMatrix(vacationMatrix,3,3)
print("done done")

