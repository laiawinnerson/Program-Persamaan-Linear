import numpy as np
import os

def tampilkan_matriks(matriks):
    m = len(matriks)

    tampil = ""
    for x in range(m):
        for y in matriks[x]:
            tampil = tampil + str(y) + "\t"
        tampil = tampil + "\n"

    print(tampil)

def tukar_posisi(matriks, baris_1, baris_2):
    n = len(matriks[0])

    for i in range(n) :
        tmp = matriks[baris_1][i]
        matriks[baris_1][i] = matriks[baris_2][i]
        matriks[baris_2][i] = tmp

def banyak_nol(matriks):
    n = 0
    
    for i in range(len(matriks)):
        if matriks[i] == 0 :
            n = n + 1
        else:
            break
    
    return n

def rapikan_matriks(matriks): #1
    m = len(matriks)

    for i in range(m):
        for j in range(m - i - 1):
            A = matriks[j]
            B = matriks[j+1]
            if banyak_nol(B) < banyak_nol(A) :
                tukar_posisi(matriks, j, j +1)

def gauss_jordan(matriks_list):
    A = np.array(matriks_list)

    rapikan_matriks(A)

    m = len(A)
    n = len(A[0])

    satu_utama_i_sebelum = -1
    satu_utama_j_sebelum = -1

    for j in range(n-1) :
        status =  bool()

        satu_utama_i = 0
        satu_utama_j = 0

        # menentukan apakah semua entry dalam 
        # dalam suatu kolom bernilai nol 
        for i in range(m):
             if A[i][j] == 0:
                status = status or False
             else :
                status = status or True

        if status == False:
            continue
    
        # menentukan satu utama
        for i in range(m):
            if A[i][j] != 0 and i > satu_utama_i_sebelum and j > satu_utama_j_sebelum:
                A[i] = A[i] / A[i][j]
                satu_utama_i = i
                satu_utama_j = j
                break

        if satu_utama_j <  satu_utama_j_sebelum or satu_utama_i < satu_utama_i_sebelum:
            continue
        
        # melakukan operasi obe
        for i in range(m):
            if i == satu_utama_i:
                continue

            k = A[i][j]
            A[i] = A[i] - k*A[satu_utama_i]
    
        satu_utama_i_sebelum = satu_utama_i
        satu_utama_j_sebelum = satu_utama_j
    
    return A

def gauss(matriks_list):
    A = np.array(matriks_list)
    rapikan_matriks(A)
    m = len(A)
    n = len(A[0])

    satu_utama_i_sebelum = -1
    satu_utama_j_sebelum = -1

    for j in range(n-1) :
        status =  bool()

        satu_utama_i = 0
        satu_utama_j = 0

        # menentukan apakah semua entry dalam 
        # dalam suatu kolom bernilai nol 
        for i in range(m):
             if A[i][j] == 0:
                status = status or False
             else :
                status = status or True

        if status == False:
            continue
    
        # menentukan satu utama
        for i in range(m):
            if A[i][j] != 0 and i > satu_utama_i_sebelum and j > satu_utama_j_sebelum:
                A[i] = A[i] / A[i][j]
                satu_utama_i = i
                satu_utama_j = j
                break

        if satu_utama_j <  satu_utama_j_sebelum or satu_utama_i < satu_utama_i_sebelum:
            continue
        
        # melakukan operasi obe
        for i in range(i, m):
            if i == satu_utama_i:
                continue

            k = A[i][j]
            A[i] = A[i] - k*A[satu_utama_i]
    
        satu_utama_i_sebelum = satu_utama_i
        satu_utama_j_sebelum = satu_utama_j
    
    return A

def jenis_solusi(matriks): #2
    solusi_unik  = False
    solusi_tak_terbatas = False
    solusi_tak_ada = False

    m = len(matriks) - 1 #baris
    n = len(matriks[m]) #kolom

    for i in range(n) :
        if matriks[m][i] == 0 :
            solusi_unik = False
            solusi_tak_terbatas = True

            if i == n-1 :
                solusi_tak_ada = False
                break

            solusi_tak_ada = True

        else :
            if i < n-1 :
                solusi_unik = True
                solusi_tak_terbatas = False
                solusi_tak_ada = False
                break

            solusi_tak_terbatas = False

            if i == n-1 :
                solusi_tak_ada = True
                break

            solusi_tak_ada = False
            
    return solusi_unik, solusi_tak_terbatas, solusi_tak_ada

def tampilkan_solusi(matriks, variable):
    m = len(matriks) ##baris
    n = len(matriks[0])##kolom

    tampil = ""

    unik, tak_terbatas, tak_ada = jenis_solusi(matriks)

    if unik == False :
        m = m -1 ##jika solusi tak unik maka baris terakhir tak ditampilkan

    tambah = False

    for i in range(m) :
        tambah = False
        for j in range(n) :
            if matriks[i][j] == 0 :
                if j == n-1 :
                    tampil = tampil + " = " + str(matriks[i][j])
            else :
                if j == n-1 :
                    tampil = tampil +  " = " + str(matriks[i][j])
                elif j == 0:
                    if matriks[i][j] == 1 :
                        tampil = tampil + variable[j]
                    elif matriks[i][j] == -1 :
                        tampil = tampil + "-" + variable[j]
                    else :
                        tampil = tampil + str(matriks[i][j])  + variable[j]
                else :
                    if  tambah == True: 
                        tampil = tampil + " + "

                    if matriks[i][j] == 1 :
                        tampil = tampil + variable[j]
                    elif matriks[i][j] == -1 :
                        tampil = tampil + "-" + variable[j]
                    else :
                        tampil = tampil + str(matriks[i][j]) + variable[j]                     
                tambah = True
        tampil = tampil + "\n"
    print(tampil)

def input_file(nama_file):
    path = os.getcwd() 
    path1 = os.path.join(path, 'Data Uji')
    os.chdir(path1) 
    
    n_var = int()
    n_pers = int()
    var = []
    matriks = []

    file = open(nama_file, "r")

    data = file.read().replace("\n", " ")
    data =  data.split(" ")

    state = str()
    for a in data:
        if a == 'n_var':
            state = 'n_var'
            continue
        elif a == 'n_pers' :
            state = 'n_pers'
            continue
        elif a == 'var' :
            state = 'var'
            continue
        elif a == 'baris' :
            state = 'baris'
            continue
        elif a == "" :
            continue

        if state == 'n_var' :
            n_var = int(a)
        if state == 'n_pers':
            n_pers = int(a)
        if state == 'var' :
            var.append(a)
        if state == 'baris' :
            matriks.append(float(a))

    matriks = np.array(matriks).reshape(n_pers, n_var + 1)
    file.close()
    
    os.chdir(path) 
    return matriks, var

def solusi_txt(test_file, jenis_solusi, matriks, var, metode):
    solusi_txt = test_file.replace(".txt", "")
    solusi_txt = solusi_txt + "_solusi_" + metode + ".txt"

    path = os.getcwd() #
    path1 = os.path.join(path, 'Data Uji')
    os.chdir(path1) #

    file = open(solusi_txt, "x")

    m = len(matriks)
    n = len(matriks[0])
      
    file.write("Matriks augmented terakhir :\n")

    for i in range(m) :
        for j in range(n) :
            file.write(str(matriks[i][j]))
            file.write("   ")
        file.write("\n")

    file.write("\nJenis solusi :")
    file.write(jenis_solusi)
    file.write("\n\n")

    if jenis_solusi != "unik" :
        m = m - 1

    if jenis_solusi == "tak ada":
        exit()

    tambah = False
    for i in range(m) :
        tambah = False
        for j in range(n) :
            if matriks[i][j] == 0 :
                if j == n-1 :
                    file.write(" = ")
                    file.write(str(matriks[i][j]))
            else :
                if j == n-1 :
                    file.write(" = ")
                    file.write(str(matriks[i][j]))
                elif j == 0:
                    if matriks[i][j] == 1 :
                        file.write(var[j])
                    elif matriks[i][j] == -1 :
                        file.write("-")
                        file.write(var[j])
                    else :
                        file.write(str(matriks[i][j]))
                        file.write(var[j])
                else :
                    if  tambah == True: 
                        file.write(" + ")

                    if matriks[i][j] == 1 :
                        file.write(var[j])
                    elif matriks[i][j] == -1 :
                        file.write("-")
                        file.write(var[j])
                    else :
                        file.write(str(matriks[i][j]))
                        file.write(var[j])                       
                tambah = True
        file.write("\n")
    file.close()
    
    path2 = os.path.join(path, 'Source Code')#
    os.chdir(path2)#

# Main program
# menentukan jenis input
print("Tentukan jenis input :")
print("1. Input manual (1)")
print("2. Input dengan file (2)")
pil1 = int(input("Pilihan : "))
print("")

# menentukan metode
print("Jenis Metode :")
print("1. Gauss (1)")
print("2. Gauss-Jordan (2)")
pil2 = int(input("Pilihan : "))
print("")

if pil1 == 1 :
    # jika memilih input manual
    # mementukan banyak variable dan persamaan
    jml_variable = int(input("Banyak variable = "))
    jml_persamaan = int(input("Banyak persamaan = "))

    # menginputkan nilai-nilai entry pada matriks
    print(f"\nInputkan variable {jml_variable}x1:")
    variable = []
    for i in range(jml_variable) :
        v = str(input())
        variable.append(v)

    print(f"\nInputkan koefisien variable setiap persamaan liner dalam bentuk matriks {jml_persamaan}x{jml_variable}:")
    matriks_A = []
    for i in range(jml_persamaan) :
        baris = list(map(float, input().split())) 
        matriks_A.append(baris)

    matriks_B = []

    print(f"\nInputkan nilai konstanta setiap persamaan linear dalam bentuk matriks {jml_persamaan}x1:")
    for i in range(jml_persamaan) :
            c = float(input())
            matriks_B.append(c)

    for i in range(jml_persamaan):
        matriks_A[i].append(matriks_B[i]) 
        
    # menampilkan  matriks
    print("\nMatriks yang diperoleh :")
    tampilkan_matriks(matriks_A)

    # menampilkannya matriks hasil obe
    matriks_OBE_2 = []
    if pil2 == 1:
        matriks_OBE = gauss(matriks_A)
        print("\nMatriks augmented :")
        tampilkan_matriks(matriks_OBE)
        matriks_OBE_2 = gauss_jordan(matriks_OBE)
      
    elif pil2 == 2:  
        matriks_OBE_2 = gauss_jordan(matriks_A)
        print("\nMatriks augmented :")    
        tampilkan_matriks(matriks_OBE_2)

    unik, tak_terbatas, tak_ada = jenis_solusi(matriks_OBE_2)

    if unik == True :
        print("Jenis solusi : solusi unik \n")
        tampilkan_solusi(matriks_OBE_2, variable)
    elif tak_terbatas == True:
        print("Jenis solusi : solusi tak terbatas\n")
        tampilkan_solusi(matriks_OBE_2, variable)
    elif tak_ada == True :
        print("Jenis solusi : Tak ada solusi\n")

elif pil1 == 2:
    # jika memilih input file

    # menginput nama file(.txt)
    print("Masukkan nama file (.txt): ")
    file = input()

    # mengambil nilai yang dibutuhkan dari file
    A, var  = input_file(file)

    # menghasilkan matriks augmented
    if pil2 == 1:
        A2 = gauss(A)
        metode = "gauss"
    elif pil2 == 2:
        A2 = gauss_jordan(A)
        metode = "gauss-jordan"

    unik, tak_terbatas, tak_ada = jenis_solusi(A2)

    if unik == True :
        solusi = "unik"
    elif tak_terbatas == True:
        solusi = "tak terbatas"
    elif tak_ada == True :
        solusi = "tak ada"

    solusi_txt(file, solusi, A2, var, metode)
