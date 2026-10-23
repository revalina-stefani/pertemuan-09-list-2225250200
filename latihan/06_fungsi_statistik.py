
# Latihan 6: Fungsi Statistik

# Fungsi untuk menghitung rata-rata
def rata_rata(data):
    if len(data) == 0:
        return 0
    return sum(data) / len(data)

# Data nilai mahasiswa
nilai = [75, 80, 65, 90, 88]

# Menampilkan rata-rata
print(f"Rata-rata = {rata_rata(nilai):.2f}")

