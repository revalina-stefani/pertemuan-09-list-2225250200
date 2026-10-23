
# Latihan 5: Filter Kelulusan

# Data nilai mahasiswa
nilai = [75, 55, 80, 60, 45, 90]

# Menyimpan nilai yang lulus
lulus = []

for x in nilai:
    if x >= 60:
        lulus.append(x)

# Menampilkan hasil
print(f"Nilai lulus = {lulus}")
print(f"Jumlah lulus = {len(lulus)}")
