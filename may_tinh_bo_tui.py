def tinh(a, phop_tinh, b):
    if phop_tinh == "+":
        return a + b
    elif phop_tinh == "-":
        return a - b
    elif phop_tinh == "*":
        return a * b
    elif phop_tinh == "/":
        if b != 0:
            return a / b
        else:
            return "Loi: Khong the chia cho 0"
    else:
        return "Phep tinh khong hop le"

if __name__ == "__main__":
    print("=== MAY TINH BO TUI (console) ===")
    while True:
        bieu_thuc = input("Nhap bieu thuc (vd: 5 + 3), hoac 'thoat' de dung: ").strip()
        if bieu_thuc.lower() == "thoat":
            print("Tam biet!")
            break
        try:
            a_str, phop_tinh, b_str = bieu_thuc.split()
            ket_qua = tinh(float(a_str), phop_tinh, float(b_str))
            print("Ket qua:", ket_qua)
        except ValueError:
            print("Dinh dang khong hop le, vi du dung: 5 + 3")