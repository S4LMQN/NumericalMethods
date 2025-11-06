import numpy as np

def upper_m_solver(u_m, b):
    n = len(b)
    x = [0 for i in range(n)]
    sum_prod = 0
    for i in range(-1, -n-1, -1):
        for j in range(-1,i,-1):
            sum_prod += x[j] * u_m[i,j]
        x[i] = (b[i] - sum_prod) / u_m[i,i]
        sum_prod = 0
    return x

def lower_m_solver(lower, b):
    n = len(b)
    x = [0 for i in range(n)]
    sum_prod = 0
    for i in range(n):
        for j in range(i):
            sum_prod += x[j] * lower[i, j]
        x[i] = (b[i] - sum_prod) / lower[i,i]
        sum_prod = 0
    return x

def lu_doolittle(a):
    n = len(a)
    l = np.identity(len(a))
    u = np.zeros_like(l)

    for j in range(len(a)):
        for i in range(len(a)):
            if i > j:
                s = sum([l[i,p] * u[p,j] for p in range(j)])
                l[i,j] = (a[i,j] - s) / u[j,j]
            else:
                s = sum([l[i,p] * u[p,j] for p in range(i)])
                u[i,j] = a[i,j] - s
    return l,u

def cholesky_decomposition(a):
    n = len(a)
    l = np.zeros_like(a, dtype=np.float64)

    for j in range(n):
        for i in range(n):
            if j > i:
                l[i,j] = 0
            elif i == j:
                x = a[i,i] - sum([l[i,k]**2 for k in range(j)])
                if x != 0:
                    l[i,j] = (x)**0.5
                else:
                    l[i,j] = 0
            else:
                l[i,j] = (a[i,j] - sum([l[i,k] * l[j,k] for k in range(j)]))/(l[j,j])

    return l

def linear_solver_lu(a, b):
    l, u = lu_doolittle(a)
    y = lower_m_solver(l, b)
    x = upper_m_solver(u, y)
    return x

def lu_determinant(a):
    l,u = lu_doolittle(a)
    product = 1
    for i in range(len(u)):
        product = product * u[i,i]
    return product

def partial_pivot(m, b, i_min):
    n = len(m)
    p_row = i_min
    max = 0

    for i in range(i_min, n):
        if abs(m[i,i_min]) > max:
            max = m[i,i_min]
            p_row = i

    temp = np.array(m[i_min,])
    m[i_min,] = np.array(m[p_row,])
    m[p_row,] = temp

    b_temp = np.int64(b[i_min])
    b[i_min] = np.int64(b[p_row])
    b[p_row] = b_temp

    return m, b

def lu_gauss(matrix):
    n = len(matrix)
    l = np.identity(n)
    u = np.array(matrix)

    a = 0
    while a < n - 1:
        for i in range(a + 1, n):
            m = u[i,a] / u[a,a]
            l[i,a] = m
            for j in range(n):
                u[i,j] = u[i,j] - m * u[a,j]
        a += 1

    return l, u

def is_dominant_matrix(m):
    pass

def p_metric(v1, v2, p = 2):
    sum = 0
    for i in range(len(v1)):
        if p == 1:
            sum += np.abs(v1[i] - v2[i])
        else:
            sum += (v1[i] - v2[i])**p
    if p == 1:
        return sum
    else:
        return sum**(1/p)

# Solve linear equations using iterative jacobi method.
def iterative_jacobi(a, b, h = 0.001):
    n = len(a)
    v = np.array([0 for i in range(n)], dtype=np.float64)
    temp = v.copy()

    while True:
        for i in range(n):
            s = np.double(sum([temp[k] * a[i,k] for k in range(n) if k != i]))
            v[i] = (b[i] - s) / a[i,i]

        if sum([(v[i] - temp[i])**2 for i in range(n)]) < h:
            break
        else:
            temp = v.copy()

    return v

matrix_A = np.array([
    [9,2,3],
    [1,12,9],
    [4,6,14]
])

vec_b = np.array([7,2,2])
print(iterative_jacobi(matrix_A, vec_b))
print(linear_solver_lu(matrix_A, vec_b))

symmetric_positve_matrix = np.array([
    [4,12,-16],
    [12,37,-43],
    [-16,-43,98]
])

m = np.array([
    [0,0],
    [0,1]
])

print(cholesky_decomposition(symmetric_positve_matrix))