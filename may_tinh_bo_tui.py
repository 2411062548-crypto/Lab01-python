import tkinter as tk
from tkinter import messagebox
def click_nut(gia_tri):
    hien_tai = bien_hien_thi.get()
    bien_hien_thi.set(hien_tai + str(gia_tri))
def xoa_tat():
    bien_hien_thi.set("")
def tinh_toan():
    try:
        bieu_thuc = bien_hien_thi.get()
        ket_qua = eval(bieu_thuc)
        bien_hien_thi.set(str(ket_qua))
    except ZeroDivisionError:
        messagebox.showerror("Loi", "Khong the chia cho so 0!")
        bien_hien_thi.set("")
    except Exception:
        messagebox.showerror("Loi", "Bieu thuc khong hop le!")
        bien_hien_thi.set("")
cua_so = tk.Tk()
cua_so.title("May tinh bo tui")
cua_so.geometry("320x420")
cua_so.resizable(False, False)
bien_hien_thi = tk.StringVar()
entry_hien_thi = tk.Entry(cua_so, textvariable=bien_hien_thi, font=("Arial", 18), justify="right")
entry_hien_thi.grid(row=0, column=0, columnspan=4, padx=10, pady=15, ipady=8)
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3)
]
for (text, r, c) in buttons:
    if text == '=':
        btn = tk.Button(cua_so, text=text, width=5, height=2, font=("Arial", 14), bg="lightgreen", command=tinh_toan)
    elif text == 'C':
        btn = tk.Button(cua_so, text=text, width=5, height=2, font=("Arial", 14), bg="lightcoral", command=xoa_tat)
    else:
        btn = tk.Button(cua_so, text=text, width=5, height=2, font=("Arial", 14), command=lambda t=text: click_nut(t))
    btn.grid(row=r, column=c, padx=5, pady=5)
cua_so.mainloop()