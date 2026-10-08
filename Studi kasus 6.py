import json
import os

path = r"C:\Users\Dhinotea\Documents\Praktikum DDP\Nilai mahasiswa.json"

def muat_data():
    if not os.path.exists(path):
        return []
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def simpan_data(data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


def tampilkan_data():
    data = muat_data()
    if len(data) == 0:
        print("Belum ada data nilai.")
        return
    print("\n=== Daftar Nilai Mahasiswa ===")
    for i, mhs in enumerate(data, start=1):
        print(f"{i}. {mhs['nama']} | NIM {mhs['nim']} | Nilai {mhs['nilai']}")


def tambah_data():
    nama = input("Nama  : ")
    nim = input("NIM   : ")

    while True:
        try:
            nilai = float(input("Nilai : "))
            if 0 <= nilai <= 100:
                break
            print("Nilai harus antara 0 dan 100.")
        except ValueError:
            print("Masukkan angka yang valid.")

    data = muat_data()
    data.append({"nama": nama, "nim": nim, "nilai": nilai})
    simpan_data(data)
    print("Data berhasil disimpan.")


while True:
    print("\n=== Sistem Pencatatan Nilai ===")
    print("1. Lihat semua data")
    print("2. Tambah data baru")
    print("3. Keluar")
    pilihan = input("Pilih menu (1-3): ")

    if pilihan == "1":
        tampilkan_data()
    elif pilihan == "2":
        tambah_data()
    elif pilihan == "3":
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak valid.")