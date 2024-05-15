def data_pribadi(nim, nama, alamat) :
    data = nama, nim, alamat
    data = tuple(data)
    print(data)
    print()
    print(f"NIM         : {nim}")
    print(f"NAMA        : {nama}")
    print(f"ALAMAT      : {alamat}")
    print()
    print(f"NIM             : {tuple(nim)}")
    print(f"NAMA DEPAN      : {tuple(nama.split()[0])}")
    print(f"NAMA TERBALIK   : {tuple(nama.split()[::-1])}")


nim = "71230995"
nama = "Alven Tendrawan"
alamat = "Bantul, DI Yogyakarta"
data_pribadi(nim, nama, alamat)