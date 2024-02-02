def tim_uscln(a, b):
    while b != 0:
        # Gán giá trị của b vào biến temp
        temp = b
        # Tìm phần dư của a chia cho b và gán giá trị mới cho b
        b = a % b
        # Gán giá trị của temp (giữa) vào a
        a = temp
    # Kết quả là giá trị cuối cùng của a sau khi b trở thành 0
    return a

# Nhập giá trị từ bàn phím
a = int(input("Nhập số nguyên dương a: "))
b = int(input("Nhập số nguyên dương b: "))

# Kiểm tra và tính USCLN
if a > 0 and b > 0:
    uscln = tim_uscln(a, b)
    print(f"Ước số chung lớn nhất của {a} và {b} là: {uscln}")
else:
    print("Vui lòng nhập số nguyên dương.")