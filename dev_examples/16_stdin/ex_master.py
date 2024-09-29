import numpy as np


n = input('Geben Sie n ein:')

if n.isnumeric():
    n = int(n)
else:
    n = 5


v = 0.5 * np.ones(2 * n - 1)
A = np.eye(2 * n) + np.diag(v, k=1) + np.diag(v, k=-1)


b = np.zeros(2 * n)
b[1:-1:2] = np.arange(1, n)
b[-1] = n


x = np.linalg.solve(A, b)
check = np.dot(A, x) - b

print(f'check {1*(check == 0)}')


error_limit = 1E-8

if all(np.abs(check) < error_limit):
    print('Check successful')
else:
    print('Check unsuccessful')


# Alternative: 
#if all(np.isclose(check, 0, atol = error_limit)):
#    print('Check successful')
#else:
#    print('Check unsuccessful')

#$META title "Lineare Gleichungssysteme, Diagonalmatrix, Probe"
#$STRUCTURALTEST structural_test
#$PROPERTY inputAnswers ["12"]
#$PROPERTY file "ex.py"
#$TESTVAR eye
#$PROPERTY allowedOccuranceRange [1,1]
#$TESTVAR diag
#$PROPERTY allowedOccuranceRange [1,2]

#$VARIABLETEST test1
#$PROPERTY inputAnswers ["12"]
#$TESTVAR n
#$TESTVAR A
#$TESTVAR b
#$TESTVAR check
#$TESTVAR error_limit

#$VARIABLETEST test2
#$PROPERTY inputAnswers ["7.2"]
#$TESTVAR n
#$TESTVAR A
#$TESTVAR b
#$TESTVAR check
#$TESTVAR error_limit


#$STDOUTTEST outtest
#$PROPERTY inputAnswers ["12"]
#$TESTVAR stdout
#$PROPERTY qualification contains
#$PROPERTY pattern "Check successful"