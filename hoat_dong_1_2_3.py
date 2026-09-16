#bai1.1
sinh_vien = {
    "ho_ten": "Nguyen Van A",
    "nam_sinh": 2004,
    "diem_tb": 8.5
}

# Truy xuất theo khóa
print(sinh_vien["ho_ten"])

# Truy xuất an toàn bằng get()
print(sinh_vien.get("diem_tb"))

# Nếu khóa không tồn tại thì get() trả về giá trị mặc định
print(sinh_vien.get("lop", "Chua co"))
#bai1.2
sinh_vien = {
    "ho_ten": "Nguyen Van A",
    "nam_sinh": 2004,
    "diem_tb": 8.5
}
# 1. Thêm khóa "lop"
sinh_vien["lop"] = "CNTT01"
# 2. Sửa điểm trung bình
sinh_vien["diem_tb"] = 9.0
# 3. In thông tin sinh viên
print(sinh_vien)
# 4. Xóa khóa "diem_tb" và lấy giá trị vừa xóa
diem_cu = sinh_vien.pop("diem_tb")
# 5. In dictionary sau khi xóa
print(sinh_vien, "- diem da xoa:", diem_cu)
# 6. Cập nhật/thêm nhiều khóa cùng lúc
sinh_vien.update({
    "nam_sinh": 2003,
    "email": "a@example.com"
})
# 7. In kết quả cuối cùng
print(sinh_vien)
#bai2
diem_mon_hoc = {
    "Toan": 8.0,
    "Ly": 7.5,
    "Hoa": 9.0,
    "Van": 6.5
}
# 1. Duyệt qua các key (tên môn)
for mon in diem_mon_hoc.keys():
    print(mon)
# 2. Duyệt qua các value (điểm)
for diem in diem_mon_hoc.values():
    print(diem)
# 3. Duyệt qua cả key và value
for mon, diem in diem_mon_hoc.items():
    print(f"{mon}: {diem}")
# 4. Tính điểm trung bình
tong_diem = 0
for diem in diem_mon_hoc.values():
    tong_diem = tong_diem + diem
print("Diem trung binh:", round(tong_diem / len(diem_mon_hoc), 2))

#bai3.1
diem_mon_hoc = {"Toan": 8.0, "Ly": 7.5, "Hoa": 9.0, "Van": 6.5}
# 1. Tạo dictionary điểm cộng 0.5 cho mỗi môn
diem_cong_diem = {mon: round(diem + 0.5, 2)
                  for mon, diem in diem_mon_hoc.items()}
print(diem_cong_diem)
# 2. Chuyển tên môn học thành chữ in hoa
ten_mon_viet_hoa = {mon.upper(): diem
                    for mon, diem in diem_mon_hoc.items()}
print(ten_mon_viet_hoa)
#bai3.2
mon_hoc_ky1 = {"Toan", "Ly", "Hoa", "Van"}
mon_hoc_ky2 = {"Toan", "Anh", "Tin", "Van"}
# Giao: môn học chung của 2 học kỳ
print(mon_hoc_ky1 & mon_hoc_ky2)
# Hợp: tất cả môn học của cả 2 học kỳ
print(mon_hoc_ky1 | mon_hoc_ky2)
# Hiệu: môn chỉ có ở học kỳ 1
print(mon_hoc_ky1 - mon_hoc_ky2)
# Hiệu: môn chỉ có ở học kỳ 2
print(mon_hoc_ky2 - mon_hoc_ky1)
# Phần bù đối xứng: môn chỉ xuất hiện ở một trong hai học kỳ
print(mon_hoc_ky1 ^ mon_hoc_ky2)


