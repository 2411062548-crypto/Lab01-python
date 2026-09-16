#bai4.1
chuoi_so = "25"
so = int(chuoi_so)
print(so, type(so))
so_thuc = float("3.14")
print(so_thuc, type(so_thuc))
danh_sach = list((1, 2, 3)) # tuple -> list
bo_ba = tuple([4, 5, 6]) # list -> tuple
tap_hop = set([1, 2, 2, 3, 3, 3]) # list -> set (tu loai bo trung lap)
tu_dien = dict([("a", 1), ("b", 2)]) # list cac tuple -> dict
print(danh_sach, bo_ba, tap_hop, tu_dien)
#bai4.2
# int("abc")
# Lỗi: ValueError vì "abc" không phải số
# int("3.14")
# Lỗi: ValueError vì "3.14" là số thực, không thể ép trực tiếp sang int
so_hop_le = int(float("3.14"))
print(so_hop_le)
#bai4.3
ket_qua = 5 + 2.5
print(ket_qua, type(ket_qua))
ket_qua_2 = "Điểm: " + str(8.5)
print(ket_qua_2)