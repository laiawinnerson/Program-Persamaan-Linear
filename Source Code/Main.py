from Gauss_Jordan import gauss, gauss_jordan
from SPL import SPL

if __name__ ==  "__main__":
    var = int(input("Banyak varible : "))
    pers = int(input("Banyak persamaan : "))

    print("")

    A = SPL(pers, var)
    A.input_data_spl()

    print("\nMetode :")
    print("1. Gauss(1)")
    print("2. Gauss-Jordan(2)")
    metode = int(input("Pilihan (1/2):"))

    if(metode == 1):
        gauss(A.matriks_akhir)
    elif(metode == 2):
        gauss_jordan(A.matriks_akhir)

    A.tentukan_jenis_solusi_spl()

    print("")

    A.tampilkan_data_spl()

