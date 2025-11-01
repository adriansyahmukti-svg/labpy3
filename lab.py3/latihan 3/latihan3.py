saldo = 1000000
print("selamat datang di atm sederhana!\n")

while True:
    print(f"\nsaldo saat ini:rp", {saldo})
    print("1. tarik uang")
    print("2. keluar")

    menu = input("pilih menu (1\2): ")

    if menu == "1":
        jumlah = int(input("masukan jumlah penarikan: "))
        if jumlah <= saldo:
            saldo = saldo - jumlah
            print("penarikan berhasil!\n")
        else:
            print("saldo tidak mencukupi!\n")

    elif menu == "2":
            print("terima kasih telah mengunakan atm sederhana!")
            break
    else:
        print("pilihan tidak valid")
        
    if saldo == 0:
        print("saldo anda habis, anda tidak bisa menarik lagi. ")
