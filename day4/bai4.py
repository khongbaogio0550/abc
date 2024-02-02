def la_so_nguyen_to(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

def tinh_tong_so_nguyen_to(n):
    tong = 0
    for i in range(2, n):
        if la_so_nguyen_to(i):
            tong += i
    return tong

# Nhập giá trị n từ người dùng
n = int(input("Nhập giá trị n (0 < n < 50): "))

# Kiểm tra n để đảm bảo thỏa mãn điều kiện
if 0 < n < 50:
    ket_qua = tinh_tong_so_nguyen_to(n)
    print(f"Tổng các số nguyên tố nhỏ hơn {n} là: {ket_qua}")
else:
    print("Giá trị n không thỏa mãn điều kiện.")