def tim_so_thoa_man():
    for i in range(10, 100):
        chuc, donvi = divmod(i, 10)
        if (chuc * donvi) == 2 * (chuc + donvi):
            print(i)

# Gọi hàm để tìm và in ra các số thỏa mãn
print("Các số thỏa mãn là:")
tim_so_thoa_man()