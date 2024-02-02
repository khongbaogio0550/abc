def tinh_tong(a, b, n):
    tong = 0
    for i in range(1, n):
        if i % a == 0 and i % b != 0:
            tong += i
    return tong

# Nhập 3 số nguyên a, b, n với a, b < n
a = int(input("Nhập số nguyên a (a < n): "))
b = int(input("Nhập số nguyên b (b < n): "))
n = int(input("Nhập số nguyên n: "))

# Kiểm tra điều kiện a, b < n
if a < n and b < n:
    ket_qua = tinh_tong(a, b, n)
    print(f"Tổng các số nguyên dương nhỏ hơn {n} chia hết cho {a} nhưng không chia hết cho {b} là: {ket_qua}")
else:
    print("Điều kiện không thỏa mãn. Vui lòng nhập lại a, b sao cho a < n và b < n.")