# Trabalho Prático de Métodos Numéricos - Parte 2
# Método de Gauss-Seidel para resolução de sistemas lineares
# Professor(a): Lilian Ferreira Berti
# Universidade Federal de Mato Grosso do Sul
# Aluno: Daniel de Faria Godoi (danielfgodoi@gmail.com)

import sys
from sympy import *

import GaussSeidel

def parser(argv):
	# Check if user wants to use the default matrix or input a new one
	print("Please, choose one of the options below")
	print("1. Input a new linear system (A and b) and the initial approximation vector")
	print("2. Use the default matrix and choose the value of w")
	opt = input("Option: ")

	A = []
	b = []
	x0 = []
	e = 0

	if opt == str(1):
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

	elif opt == str(2):
		# Defined matrix A and w as specified in item 2
		w = float(input("\nValue of w: "))
		
		A = [[1.,			float(w),		float(w**2),	0.,			0.],
			[float(w),		1.,				float(w),		w**2,		0.],
			[float(w**2),	float(w),		1.,				float(w),	float(w**2)],
			[0.,			float(w**2),	float(w),		1.,			float(w)],
			[0.,			0.,				float(w**2),	float(w),	1.]]
		
		b = [1., 1., 1., 1., 1.]

		n = int(len(A))	
		for x in range(n):
			x0.append(0.)

		e = 10**(-6)
		e = sympify(e).evalf()

	else:
		print("\nThis option is not available! Please, try again...")
		exit()

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
	
	return A, b, x0, e

def main(argv):
	# Parse needed variables
	A, b, x0, e = parser(sys.argv)
	# Run Gauss-Seidel Method using the matrices A, b and initial vector x0
	criterion = GaussSeidel.lineCriterion(A)
	if criterion:
		print("Line Criteria met! Running Gauss-Seidel Method.")
		x = GaussSeidel.run(A, b, x0, e)
		print("The solution is x=" + str(x))
	
	else:
		print("Line Criterion were not met! Ending program.")

if __name__ == "__main__":
	main(sys.argv)
