status = True
daftar_anggota = ["Zaid", "Belva", "Al", "Ririn", "Azka", "Johan", "Niyah", "Falih", "Juna", "Ibnu", "Adam"]

while status == True:
    print("==== MENU ====")
    print("1. Profile Kelompok")
    print("2. Bina Damping")
    print("3. Tambah Anggota")
    print("4. Daftar Anggota")
    print("5. Hapus Nama Anggota")
    print("6. Edit Nama Anggota")
    print("7. Keluar")
    
    pilihan = input("Pilih Menu : ")
    
    if pilihan == "1":
        print("=== INTERNET OF THINGS ===")
        print("Filosofi : Tulisan IOT Menjadi nama kelompok yang melambangkan keterhubungan dan inovasi")
        
    elif pilihan == "2":
        print("- Dzaky Ainur Rahman")
        print("- Muhammadancel Prinata")
        
    elif pilihan == "3":
        tambahan_anggota = input("Tambah Anggota : ")
        daftar_anggota.append(tambahan_anggota)
        
    elif pilihan == "4":
        print(f"Daftar Anggota = {daftar_anggota}")
        
    elif pilihan == "5":
        hapus = input("Masukkan nama yang dihapus: ")
        if hapus in daftar_anggota:
            daftar_anggota.remove(hapus)
            
    elif pilihan == "6":
        lama = input("Nama yang mau diganti: ")
        if lama in daftar_anggota:
            daftar_anggota.remove(lama)
            baru = input("Masukkan nama baru: ")
            daftar_anggota.append(baru)
            
    elif pilihan == "7":
        status = False