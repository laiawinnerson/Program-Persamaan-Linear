def tukar_posisi(matriks, baris_1:int, baris_2:int):
    n = len(matriks[0])

    tmp_1 = matriks[baris_1].copy()
    tmp_2 = matriks[baris_2].copy()
    matriks[baris_1] = tmp_2.copy()
    matriks[baris_2] = tmp_1.copy()

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

def gauss_jordan(matriks_akhir):
    rapikan_matriks(matriks_akhir)

    m = len(matriks_akhir)
    n = len(matriks_akhir[0])

    satu_utama_i_sebelum = -1
    satu_utama_j_sebelum = -1

    for j in range(n-1) :
        status =  bool()

        satu_utama_i = 0
        satu_utama_j = 0

        for i in range(m):
             if matriks_akhir[i][j] == 0:
                status = status or False
             else :
                status = status or True

        if status == False:
            continue
    
        for i in range(m):
            if matriks_akhir[i][j] != 0 and i > satu_utama_i_sebelum and j > satu_utama_j_sebelum:
                matriks_akhir[i] = matriks_akhir[i] / matriks_akhir[i][j]
                satu_utama_i = i
                satu_utama_j = j
                break

        if satu_utama_j <  satu_utama_j_sebelum or satu_utama_i < satu_utama_i_sebelum:
            continue
        
        for i in range(m):
            if i == satu_utama_i:
                continue

            k = matriks_akhir[i][j]
            matriks_akhir[i] = matriks_akhir[i] - k*matriks_akhir[satu_utama_i]
    
        satu_utama_i_sebelum = satu_utama_i
        satu_utama_j_sebelum = satu_utama_j

def gauss(matriks_akhir):
    rapikan_matriks(matriks_akhir)

    m = len(matriks_akhir)
    n = len(matriks_akhir[0])

    satu_utama_i_sebelum = -1
    satu_utama_j_sebelum = -1

    for j in range(n-1) :
        status =  bool()

        satu_utama_i = 0
        satu_utama_j = 0

        for i in range(m):
             if matriks_akhir[i][j] == 0:
                status = status or False
             else :
                status = status or True

        if status == False:
            continue
    
        for i in range(m):
            if matriks_akhir[i][j] != 0 and i > satu_utama_i_sebelum and j > satu_utama_j_sebelum:
                matriks_akhir[i] = matriks_akhir[i] / matriks_akhir[i][j]
                satu_utama_i = i
                satu_utama_j = j
                break

        if satu_utama_j <  satu_utama_j_sebelum or satu_utama_i < satu_utama_i_sebelum:
            continue

        for i in range(i, m):
            if i == satu_utama_i:
                continue

            k = matriks_akhir[i][j]
            matriks_akhir[i] = matriks_akhir[i] - k*matriks_akhir[satu_utama_i]
    
        satu_utama_i_sebelum = satu_utama_i
        satu_utama_j_sebelum = satu_utama_j