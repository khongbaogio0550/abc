def la_so_chinh_phuong(n):
    for i in range(1, n + 1):
        if i**2 == n:
            return True
    return False
def la_so_doi_xung(n):
    str_n = str(n)
    return str_n == str_n[::-1]

def la_so_nguyen_to(n):
    if n <= 1:
        return False  # Số không lớn hơn 1 không phải số nguyên tố
    #Sử dụng vòng lặp for để kiểm tra có tồn tại ước số nào khác lớn hơn 1 không
    for i in range(2, n):
        if n % i == 0: 
            return False  # Chỉ cần tìm thấy 1 ước số là biết không phải số nguyên tố
    return True  # Là số nguyên tố
def chu_so_lon_nhat(n):
    return max(map(int, str(n)))

def chu_so_nho_nhat(n):
    return min(map(int, str(n)))

def tang_dan(n):
    str_n = str(n)
    return all(str_n[i] <= str_n[i + 1] for i in range(len(str_n) - 1))

def giam_dan(n):
    str_n = str(n)
    return all(str_n[i] >= str_n[i + 1] for i in range(len(str_n) - 1))
# Nhập số nguyên dương n
n = int(input("Nhap mot so nguyen duong n: "))

# Kiểm tra và in kết quả
if la_so_doi_xung(n):
    print(f"{n} la so doi xung.")
else:
    print(f"{n} khong phai la so doi xung.")

if la_so_chinh_phuong(n):
    print(f"{n} la so chinh phuong.")
else:
    print(f"{n} khong phai la so chinh phuong.")

if la_so_nguyen_to(n):
    print(f"{n} là số nguyên tố.")
else:
    print(f"{n} không phải là số nguyên tố.")

print(f"Chữ số lớn nhất của {n} là: {chu_so_lon_nhat(n)}")
print(f"Chữ số nhỏ nhất của {n} là: {chu_so_nho_nhat(n)}")

if tang_dan(n):
    print(f"Các chữ số của {n} tăng dần.")
elif giam_dan(n):
    print(f"Các chữ số của {n} giảm dần.")
else:
    print(f"Các chữ số của {n} không tăng dần và không giảm dần.")