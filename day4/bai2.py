def tinh_tong_tang_dan(n):
    S = 0
    for i in range(1, n + 1):
        S += i
    return S

def tinh_tong_binh_phuong(n):
    S = 0
    for i in range(1, n + 1):
        S += i**2
    return S

def tinh_tong_reciprocal(n):
    S = 0
    for i in range(1, n + 1):
        S += 1/i
    return S

def tinh_giai_thua(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def tinh_tong_giai_thua(n):
    S = 0
    for i in range(1, n + 1):
        S += tinh_giai_thua(i)
    return S

# Nhập số nguyên dương n
n = int(input("Nhập một số nguyên dương n: "))

# Tính và in kết quả
print(f"a. S = 1 + 2 + … + {n} = {tinh_tong_tang_dan(n)}")
print(f"b. S = 1^2 + 2^2 + … + {n}^2 = {tinh_tong_binh_phuong(n)}")
print(f"c. S = 1 + 1/2 + … + 1/{n} = {tinh_tong_reciprocal(n)}")
print(f"d. S = 1*2*…*{n} = {tinh_giai_thua(n)}")
print(f"e. S = 1! + 2! + … + {n}! = {tinh_tong_giai_thua(n)}")