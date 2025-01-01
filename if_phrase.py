# Meminta input dari pengguna
def if_clause_sample():
    nilai = int(input("Masukkan nilai Anda: "))

    # Klausa if untuk memeriksa kondisi
    if nilai >= 90:
        print("Nilai Anda A. Luar biasa!")
    
    if nilai >= 80:
        print("Nilai Anda B. Bagus!")
    elif nilai >= 70:
        print("Nilai Anda C. Cukup.")
    elif nilai >= 60:
        print("Nilai Anda D. Perlu usaha lebih.")
    else:
        print("Nilai Anda E. Anda harus mengulang mata pelajaran ini.")

if __name__ == "__main__":
    if_clause_sample()
    

