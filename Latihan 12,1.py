n = int(input("Masukkan jumlah kategori: "))

apps = {}
for i in range(n):
    kategori = str(input(f"Masukkan nama kategori ke-{i+1}: "))
    set_apps = set()
    for j in range(5):
        app = str(input(f"Masukkan nama aplikasi ke-{j+1}: "))
        set_apps.add(app)
    apps[kategori] = set_apps

list_apps = [apps[kategori] for kategori in apps]
hasil = set.intersection(*list_apps)

print("Aplikasi yang ada di semua kategori:", hasil)