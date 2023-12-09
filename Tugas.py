import pandas as pd

# Nama  : Rizkya Wildani Yahya
# NRP   : 152022191
# Kelas : DD

data = {'Nama': ['John', 'Jane', 'Bob', 'Alice'],
        'Usia': [25, 35, 30, 28],
        'Gaji': [50000, 60000, 70000, 55000]}

# Membuat DataFrame dari data karyawan
karyawan_df = pd.DataFrame(data)

# Pertanyaan 1
# Menambahkan 5% dari gaji saat ini untuk setiap karyawan
for index, row in karyawan_df.iterrows():
    karyawan_df.at[index, 'Gaji'] = (lambda x: x + x * 0.05)(row['Gaji'])

# Pertanyaan 2
# Menampilkan DataFrame setelah peningkatan gaji 5%
print("Data Karyawan setelah peningkatan gaji 5%:")
print(karyawan_df)
print("\nRingkasan Perubahan:")
print(karyawan_df.describe())

# Pertanyaan 3
# Menambahkan 2% dari gaji saat ini untuk karyawan yang usianya di atas 30 tahun
for index, row in karyawan_df.iterrows():
    if row['Usia'] > 30:
        karyawan_df.at[index, 'Gaji'] = (lambda x: x + x * 0.02)(row['Gaji'])

# Pertanyaan 4
# Menampilkan DataFrame setelah peningkatan gaji tambahan dan ringkasan hasilnya
print("\nData Karyawan setelah peningkatan gaji tambahan:")
print(karyawan_df)
print("\nRingkasan Perubahan setelah peningkatan gaji tambahan:")
print(karyawan_df.describe())

# ---------------------------- #
# Buat Branch Baru pada repository github berikut dengan format KELAS_NRP_NAMA
# https://github.com/diashfirdaus-cyber/Pemdas_Itenas.git
# ---------------------------- #

# Catatan:

# Gunakan loop for dan fungsi lambda untuk mengimplementasikan operasi yang diminta.
# Pastikan untuk menyimpan hasil perubahan pada DataFrame.
# Tampilkan hasil dan ringkasan dengan jelas.
# Jangan lupa untuk menyesuaikan persentase peningkatan gaji sesuai dengan cerita.