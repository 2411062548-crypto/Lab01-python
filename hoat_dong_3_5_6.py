a = 17
b = 5
print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a / b =", a / b)
print("a // b =", a // b)
print("a % b =", a % b)
print("a ** b =", a ** b)
#bai5.2
diem = 6.5
tuoi = 20

print(6.5 <= diem < 8.0 and diem >= 6.5)
print(tuoi < 18 or tuoi >= 60)
print(not (diem < 5))
#bai5.3
x = 10

x += 5
print("x =", x)

x -= 5
print("x =", x)

x *= 5
print("x =", x)

x /= 5
print("x =", x)

x //= 2
print("x =", x)

x **= 2
print("x =", x)

danh_sach = [1, 2, 3, "python"]

print(3 in danh_sach)

danh_sach_2 = danh_sach
print(danh_sach is danh_sach_2)


#bai5.4
print(2 + 3 * 4 ** 2)                  
print((2 + 3) * 4 ** 2)                
print(10 > 5 and 3 < 1 or not False) 

   
#bai6.1
bien = 10
print(bien, type(bien))

bien = "Xin chao"
print(bien, type(bien))

bien = 3.14
print(bien, type(bien))

bien = True
print(bien, type(bien))
#bai6.2
ho_ten = "Nguyen Van A"
diem_toan = 8.0
diem_ly = 7.5
diem_hoa = 9.0

# Tính điểm trung bình
dtb = (diem_toan + diem_ly + diem_hoa) / 3


la_gioi = dtb >= 8.0
la_kha = dtb >= 6.5 and dtb < 8.0
la_trung_binh = dtb >= 5.0 and dtb < 6.5
la_yeu = dtb < 5.0


print(ho_ten, "- DTB:", round(dtb, 2))
print("Dat loai Gioi?", la_gioi)
print("Dat loai Kha?", la_kha)
print("Dat loai Trung binh?", la_trung_binh)
print("Dat loai Yeu?", la_yeu)
print("Kieu du lieu cua la_gioi:", type(la_gioi))