list_data = input("Masukkan data dalam list (pisahkan dengan koma): ").split(",")
set_data = set(list_data)

print("\nList sebelum konversi:", list_data)
print("Set setelah konversi:", set_data)

set_data = input("\nMasukkan data dalam set (pisahkan dengan koma): ").split(",")
list_data = list(set_data)

print("\nSet sebelum konversi:", "{" + ", ".join(set_data) + "}")
print("List setelah konversi:", list_data)

tuple_data = tuple(input("\nMasukkan data dalam tuple (pisahkan dengan koma): ").split(","))
set_data = set(tuple_data)

print("\nTuple sebelum konversi:", tuple_data)
print("Set setelah konversi:", set_data)

set_data = input("\nMasukkan data dalam set (pisahkan dengan koma): ").split(",")
tuple_data = tuple(set_data)

print("\nSet sebelum konversi:", "{" + ", ".join(set_data) + "}")
print("Tuple setelah konversi:", tuple_data)