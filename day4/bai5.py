def viet_nguoc_lai(n):
    str_n = str(n)
    return str_n[::-1]
n = int(input("Nhập số nguyên dương n là: "))
print (f"{n} được viết ngược lại là: {viet_nguoc_lai(n)}")