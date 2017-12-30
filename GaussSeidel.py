# Trabalho Prático de Métodos Numéricos - Parte 2
# Método de Gauss-Seidel para resolução de sistemas lineares
# Professor(a): Lilian Ferreira Berti
# Universidade Federal de Mato Grosso do Sul
# Aluno: Daniel de Faria Godoi (danielfgodoi@gmail.com)

import sys
from sympy import *

# Method for checking the relative error given xk and xk+1 using the infinite norm
def relativeError(xk, xk_1):

	if max(xk) == 0 and max(xk_1) == 0:
		return 1

	n = int(len(xk))

	max_num = 0
	for i in range(n):
		x = xk_1[i] - xk[i]
		if x < 0:
			x *= -1
		if x > max_num:
			max_num = x
	
	max_den = 0
	for i in range(n):
		x = xk_1[i]
		if x > max_den:
			max_den = x

	if max_den == 0:
		print("error=0\n")
		return 0
	
	else:
		print("error=" + str(float(max_num/max_den)) + "\n")
		return float(max_num/max_den)

def lineCriterion(A):
	diag = 0
	criterion = []
	n = int(len(A[0]))
	
	for i in range(n):
		sum = 0
		for j in range(n):
			if i == j:
				diag = A[i][i]
			else:
				sum += A[i][j]
		criterion.append(sum/diag)

	print("Line criterion: ", criterion)
	max_value = max(criterion)
	if max_value < 1:
		return True
	else:
		return False

# Method for executing the Gauss-Seidel Method given
# the matrix A
# the matrix b
# the initial approximation vector
# the error bound (aka epsilon)
def run(A, b, x0, e):

	print("Starting Gauss-Seidel Method => calculate x based on A, b and x0\n")

	k = 0
	n = int(len(A[0]))
	xk = x0[:]
	xk_1 = x0[:]
	max_it = 1000

	while relativeError(xk, xk_1) >= e and k < max_it:
		xk = xk_1[:]
		for i in range(n):
			x = b[i]
			for j in range(n):
				if j == i:
					pass
				elif j < i:
					x = x - (A[i][j] * xk_1[j])
				else:
					x = x - (A[i][j] * xk[j])
			x *= 1./A[i][i]
			xk_1[i] = x

		print("k=", k)
		print("x"+str(k)+"=" + str(xk))
		print("x"+str(k+1)+"=" + str(xk_1))
		k += 1

	print("\nCriteria met!\nEnding Gauss-Seidel Method.\n")
	return xk_1

# This function will be executed only if running Gauss-Seidel script alone
def main(argv):
	A = []
	b = []
	x0 = []
	e = 0

	# Read matrix A and b from input
	print("\nInput matrix A of size nxn")

	# Matrix A
	A.append(input().split())
	n = len(A[0])
	i = 0
	for x in range(len(A[0]) - 1):
		A.append(input().split())
		i += 1
		if len(A[i]) != n:
			print("\nThe input line does not match the matrix size")
			exit()
	
	# Convert all values to float
	for i, val in enumerate(A):
		for j, val in enumerate(A[i]):
			A[i][j] = float(val)

	# Matrix b
	print("\nInput matrix b of size nx1")
	b = input().split()
	if len(b) != n:
		print("\nThe input line does not match the matrix size")
		exit()
	for i, val in enumerate(b):
		b[i] = float(val)

	# Initial approximation
	print("\nInput initial approx. vector of size nx1")
	x0 = input().split()
	if len(x0) != n:
		print("\nThe input line does not match the matrix size")
		exit()
	for i, val in enumerate(x0):
		x0[i] = float(val)

	# Epsilon (error)
	e = input("\nInput Epsilon (error bound): ")
	e = sympify(e).evalf()

	print("\nMatrix size:", n)
	
	print("A = ", end='')
	for i, val in enumerate(A):
		if i != 0:
			print("   ", A[i])
		else:
			print(A[i])
			
	print("b =", b)
	print("x0 =", x0)
	print("e =", e, "\n")

	criterion = lineCriterion(A)
	if criterion:
		print("Line Criteria met! Running Gauss-Seidel Method.")
		x = run(A, b, x0, e)
		print("The solution is x=" + str(x))
	
	else:
		print("Line Criterion were not met! Ending program.")

if __name__ == "__main__":
	main(sys.argv)