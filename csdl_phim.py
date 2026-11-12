import sqlite3

TEN_FILE_CSDL = "phim_yeu_thich.db"

def ket_noi_csdl():
    return sqlite3.connect(TEN_FILE_CSDL)

def tao_bang_neu_chua_co():
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()
    con_tro.execute("""
        CREATE TABLE IF NOT EXISTS phim (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ten_phim TEXT NOT NULL,
            dao_dien TEXT NOT NULL,
            the_loai TEXT NOT NULL,
            da_xem INTEGER NOT NULL DEFAULT 0
        )
    """)
    ket_noi.commit()
    ket_noi.close()

def them_phim(ten_phim, dao_dien, the_loai):
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()
    con_tro.execute(
        "INSERT INTO phim (ten_phim, dao_dien, the_loai, da_xem) VALUES (?, ?, ?, 0)",
        (ten_phim, dao_dien, the_loai)
    )
    ket_noi.commit()
    ket_noi.close()

def lay_toan_bo_phim():
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()
    con_tro.execute("SELECT id, ten_phim, dao_dien, the_loai, da_xem FROM phim ORDER BY id")
    ket_qua = con_tro.fetchall()
    ket_noi.close()
    return ket_qua

def xoa_phim(id_phim):
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()
    con_tro.execute("DELETE FROM phim WHERE id = ?", (id_phim,))
    ket_noi.commit()
    ket_noi.close()

def danh_dau_da_xem(id_phim):
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()
    con_tro.execute("UPDATE phim SET da_xem = 1 WHERE id = ?", (id_phim,))
    ket_noi.commit()
    ket_noi.close()

def thong_ke_theo_the_loai():
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()
    con_tro.execute("SELECT the_loai, COUNT(*) FROM phim GROUP BY the_loai")
    ket_qua = con_tro.fetchall()
    ket_noi.close()
    return ket_qua

def tao_du_lieu_mau():
    tao_bang_neu_chua_co()
    phim_mau = [
        ("Inception", "Christopher Nolan", "Hanh dong"),
        ("Avatar", "James Cameron", "Khoa hoc vien tuong"),
        ("Titanic", "James Cameron", "Tinh cam"),
        ("The Dark Knight", "Christopher Nolan", "Hanh dong"),
        ("Spirited Away", "Hayao Miyazaki", "Hoat hinh")
    ]
    
    for ten_phim, dao_dien, the_loai in phim_mau:
        them_phim(ten_phim, dao_dien, the_loai)
        
    danh_dau_da_xem(1)
    
    print("Tao thanh cong file phim_yeu_thich.db va nap du lieu mau!")

if __name__ == "__main__":
    tao_du_lieu_mau()