
def for_loop_sample():
    # Loop angka2dd
    for i in range(3):
        # 0 <= i < 3
        print(i)
    
    # Loop list
    buah = ["apel", "jeruk", "pisang"] 
    for b in buah:
        print(b)
    
    # Loop dengan index
    nama = ["Budi", "Ani"]
    for i, n in enumerate(nama):
        print(f"{i+1}. {n}")
    
    # 4. Loop melalui dictionary
    siswa = {
        "nama": "Budi",
        "umur": 15,
        "kelas": "9A"
    }

    print(siswa['nama'])
    for key, value in siswa.items():
        print(f"{key}: {value}")
    
    # 5. Nested loop (loop bersarang)
    for i in range(3):
        for j in range(2):
            print(f"i={i}, j={j}")
    

if __name__ == "__main__":
    for_loop_sample()
