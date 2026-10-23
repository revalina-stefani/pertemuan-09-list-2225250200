
# Praktik Pertemuan 09: Analisis Nilai Mahasiswa

# Fungsi untuk menghitung rata-rata
def rata_rata(data):
    if len(data) == 0:
        return 0
    return sum(data) / len(data)


# Fungsi untuk mengambil nilai yang lulus
def nilai_lulus(data, batas=60):
    lulus = []
    for nilai in data:
        if nilai >= batas:
            lulus.append(nilai)
    return lulus


# Data nilai 10 mahasiswa
nilai = [78, 55, 90, 67, 60, 82, 45, 71, 88, 59]

# Mengolah data
banyak = len(nilai)
total = sum(nilai)
minimum = min(nilai) if banyak > 0 else 0
maksimum = max(nilai) if banyak > 0 else 0
rata = rata_rata(nilai)
lulus = nilai_lulus(nilai)
belum_lulus = banyak - len(lulus)

# Menampilkan hasil analisis
print("=== ANALISIS NILAI MAHASISWA ===")
print(f"Seluruh nilai       : {nilai}")
print(f"Banyak data         : {banyak}")
print(f"Total nilai         : {total}")
print(f"Rata-rata           : {rata:.2f}")
print(f"Nilai minimum       : {minimum}")
print(f"Nilai maksimum      : {maksimum}")
print(f"Batas kelulusan     : 60")
print(f"Nilai mahasiswa lulus: {lulus}")
print(f"Jumlah lulus        : {len(lulus)}")
print(f"Jumlah belum lulus  : {belum_lulus}")
