# PROGRAM SISTEM PERSAMAAN LINEAR

Program ini adalah program untuk menyelesaikan sistem persamaan linear dengan menggunakan dua metode yakni gauss dan gauss jordan. Input dapat melalui keyboard ataupun input dengan file .txt. Keluaran berupa solusi dari sistem persamaan linear yang diinputkan.

## **Struktur Folder**
### 1. Data Uji
Berisi file test bereksistensi .txt. File tersebut berisi bagian-bagian dari SPL yang hendak dicari solusinya. File .txt terdiri dari variabel dan persamaan linearnya namun dalam bentuk matriks augmented. Pada folder ini juga nantinya solusi untuk SPL akan ditulis.

### 2. Source Code
Berisi source code program sistem persamaan liner

## **Instalasi**
untuk dapat menjalankan program kita harus menginstal interpreter pyhton dan library numpy terlebih dahulu
### 1. Windows
* Download interpreter pyhton untuk windows di https://www.python.org/
* Buka file instalasi dengan double click lalu instal interpreter python
* Untuk menginstal library numpy buka cmd lalu ketikan teks berikut lalu enter
    ```
      pip install numpy
    ```
### 2. Mac Os
* Download interpreter pyhton untuk mac os di https://www.python.org/
* Click kanan file instalasi, klik open, lalu instal interpreter python
* Untuk menginstal library numpy buka terminal dan ketikan teks berikut lalu enter
    ```
      pip install numpy
    ```

### 3. Linux
* Jika anda menggunakan distribusi linux ubuntu, buka terminal dan ketikan teks berikut, lalu tekan enter
    ```
      sudo apt install python3
    ```
* Untuk distrubusi linux lainnya sesuaikan dengan package manager yang digunakan
* Untuk menginstal library numpy buka terminal dan ketikan teks berikut lalu enter
    ```
      pip install numpy
    ```

## **Tutorial Membuat File Test**
* Pertama buat file test bereksitensi .txt dan letakkan di folder Data Uji
* Buka file test lalu tuliskan nilai-nilai yang menggambar SPL, yaitu : banyak varibel, banyak persamaan, variabel, dan persamaan SPL dalam bentuk matriks augmented
* Tuliskan kata kunci terlebih dahulu sebelum menulis suatu nilai. Berikut beberapa aturan kata kunci.

  | Kata kunci | Kegunaan                           |
  | -----      | ---                                |
  | n_var      | kata kunci untuk banyak variabel   |
  | n_pers     | kata kunci untuk banyak persamaan  |
  | var        | kata kunci untuk banyak persamaan  |
  | baris      | kata kunci untuk baris pada matriks augmented  |

* Jika masih bingung lihat contoh file test pada folder Data Uji
