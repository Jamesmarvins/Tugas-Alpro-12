def baca_konten_berkas(nama_file):
    try:
        with open(nama_file, 'r') as file:
            konten = file.read()
            return konten.lower().split()
    except FileNotFoundError:
        print(f"Berkas '{nama_file}' tidak ditemukan.")
    except PermissionError:
        print(f"Tidak dapat membaca berkas '{nama_file}'.")

def cari_kata_umum(file_pertama, file_kedua):
    kata_dalam_file_pertama = baca_konten_berkas(file_pertama)
    kata_dalam_file_kedua = baca_konten_berkas(file_kedua)

    if kata_dalam_file_pertama and kata_dalam_file_kedua:
        kata_umum = set(kata_dalam_file_pertama) & set(kata_dalam_file_kedua)
        return kata_umum
    return set()

def program_utama():
    file_pertama = input("Masukkan nama berkas pertama: ")
    file_kedua = input("Masukkan nama berkas kedua: ")

    kata_umum = cari_kata_umum(file_pertama, file_kedua)

    if kata_umum:
        print("Kata-kata yang muncul pada kedua berkas:")
        for kata in kata_umum:
            print(kata)

if __name__ == "__main__":
    program_utama()