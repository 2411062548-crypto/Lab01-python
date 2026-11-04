import pandas as pd
df = pd.read_csv("diem_sinh_vien.csv")
print(df.head())
print(df.shape)
print(df.columns.tolist())
diem_trung_binh_mon = df.groupby("mon_hoc")["diem"].mean()
print(diem_trung_binh_mon)
print("Vien trung binh toan bo:", df["diem"].mean())
print("Diem cao nhat:", df["diem"].max())
print("Diem thap nhat:", df["diem"].min())
diem_sinh_vien_gioi = df[df["diem"] >= 8.0]
print(diem_sinh_vien_gioi)
sinh_vien_khong_dat = df[df["diem"] < 5.0]
print(sinh_vien_khong_dat)