import numpy as np

class SPL :
    n_var = 0
    n_pers = 0
    matriks_awal = []
    matriks_akhir = []
    var = []

    unik = False
    tak_terbatas = False
    tak_ada = False

    def __init__(self, banyak_persamaan:int, banyak_variable:int):
        self.n_pers = banyak_persamaan
        self.n_var = banyak_variable
    
    def input_data_spl(self):
        print(f"Inputkan variabel dalam bentuk {self.n_var}x1")

        for i in range(self.n_var):
            v = input()
            self.var.append(v)

        print(f"\nInputkan koefisien variable setiap persamaan liner dalam bentuk matriks {self.n_pers}x{self.n_var}:")

        for i in range(self.n_pers) :
            entry = list(map(float, input().split())) 
            self.matriks_awal.append(entry)
        
        print(f"\nInputkan nilai konstanta setiap persamaan linear dalam bentuk matriks {self.n_pers}x1:")

        konstanta = []

        for i in range(self.n_pers) :
            konst = float(input())
            konstanta.append(konst)

        for i in range(self.n_pers):
            self.matriks_awal[i].append(konstanta[i])

        self.matriks_akhir = self.matriks_awal.copy()
        
        self.matriks_awal = np.array(self.matriks_awal)
        self.matriks_akhir = np.array(self.matriks_akhir)

    def tampilkan_data_spl(self):
        v = ""
        for var in self.var :
            v = v + var + " "
        
        print(f"Var : {v}")

        print("Matriks Augmented Awal :")

        m = len(self.matriks_awal)

        MA = ""
        for x in range(m):
            for y in self.matriks_awal[x]:
                MA = MA + str(y) + "\t"
            MA = MA + "\n"

        print(MA)

        print("Matriks Augmented Akhir :")

        m = len(self.matriks_akhir)

        MA = ""
        for x in range(m):
            for y in self.matriks_akhir[x]:
                MA = MA + str(y) + "\t"
            MA = MA + "\n"

        print(MA)

        print(f"Unik : {self.unik}")
        print(f"Tak terbatas : {self.tak_terbatas}")
        print(f"Tak ada : {self.tak_ada}")
        
    def tentukan_jenis_solusi_spl(self):
        m = len(self.matriks_akhir) - 1 
        n = len(self.matriks_akhir[m]) 

        for i in range(n) :
            if self.matriks_akhir[m][i] == 0 :
                self.unik = False
                self.tak_terbatas = True

                if i == n-1 :
                    self.tak_ada = False
                    break

                self.tak_ada = True

            else :
                if i < n-1 :
                    self.unik = True
                    self.tak_terbatas = False
                    self.tak_ada = False
                    break

                self.tak_terbatas = False

                if i == n-1 :
                    self.tak_ada = True
                    break

                self.tak_ada = False




