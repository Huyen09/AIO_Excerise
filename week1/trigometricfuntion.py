import math

def factorial(n):
    result = 1
    for i in range(1,n+1):
        result *=i
    return result

# tinh sin
def approx_sin(x,n):
    sin_approx = 0
    for i in range(n+1):
        num = x**(2*i+1)
        coef = (-1)**i
        denom = factorial((2*i)+1)
        sin_approx += (coef)*((num)/(denom))
    return sin_approx

#tinh cos
def approx_cos(x,n):
    cos_approx = 0
    for i in range(n+1):
        coef = (-1)**i
        num = x**(2*i)
        denom = factorial(2*i)
        cos_approx += (coef)*((num)/(denom))
    return cos_approx

def approx_sinh(x,n):
    sinh_approx = 0
    for i in range(n+1):
        num = x**((2*i)+1)
        denom = factorial((2*i)+1)
        sinh_approx += (num)/(denom)
    return sinh_approx

def approx_cosh(x,n):
    cosh_approx = 0
    for i in range(n+1):
        num = x**(2*i)
        denom = factorial(2*i)
        cosh_approx += (num)/(denom)
    return cosh_approx

try:
    n = int(input("gia tri n: "))
    if n < 0:
        print("n must be grather than 0")
    else:
        x = float(input("Gia tri x: "))
        if x < (-2)*math.pi or x > 2*math.pi:
            print("x must be radian")
        else:
            res1 = approx_cos(x, n)
            res2 = approx_cosh(x, n)
            res3 = approx_sin(x, n)
            res4 = approx_sinh(x, n)

            # In kết quả theo yêu cầu
            print(f"cos({x:.2f}, {n}) = {res1:.5f}")
            print(f"cosh({x:.2f}, {n}) = {res2:.5f}")
            print(f"sin({x:.2f}, {n}) = {res3:.5f}")
            print(f"sinh({x:.2f}, {n}) = {res4:.5f}")
except ValueError as e:
        print(e)