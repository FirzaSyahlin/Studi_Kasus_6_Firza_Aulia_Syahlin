# Studi_Kasus_6_Firza_Aulia_Syahlin
Nama: Firza Aulia Syahlin
I NIM: 2609116107

Penjelasan singkat Kode

Program ini menyimpan data nilai mahasiswa di file JSON, jadi datanya
nggak hilang walaupun programnya ditutup.

- muat_data() dipakai buat baca isi file JSON ke dalam list. Kalau file-nya
belum ada, hasilnya list kosong biar nggak error.

- simpan_data() kebalikannya, nulis list ke file pakai json.dump().

- Di tambah_data(), data lama dibaca dulu, terus data baru ditambah pakai
append(), baru disimpan lagi. Kalau langsung ditulis tanpa dibaca dulu,
data lama bakal ketimpa.

- tampilkan_data() nampilin semua data pakai for, dan menu utamanya pakai
while True supaya jalan terus sampai user pilih 3 buat keluar.

<img width="1004" height="839" alt="Screenshot 2026-10-08 221858" src="https://github.com/user-attachments/assets/b536599f-568c-45f4-a105-9494965c5213" />
