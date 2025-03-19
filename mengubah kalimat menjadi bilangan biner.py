'''
fungsi ini mengubah setiap karakter dalam 
sebuah kalimat menjadi representasi binernya.
'''
def ubah_kalimat(kalimat):
    
    # inisialisasi string kosong untuk menyimpan hasil koverensi
    biner = ""
    '''
    mengambil nilai ASCII dari setiap huruf pada kalimat dan 
    mengubah nilai ASCII menjadi bilangan binner dengan pnjng 8 bit
    '''
    for i in kalimat:
        nilai_biner = bin(ord(i))[2:].zfill(8)
        # menambahkan hasil konversi ke dalam string ke biner
        biner += nilai_biner
    return biner

# input kalimat user
kalimat = input("Masukkan Kalimat: ")

# memanggil fungsi dan mengubah kalimat menjadi biner
hasil_biner = ubah_kalimat(kalimat)

# menampilkan hasil konversi code diatas
print("Kalimat dalam Bentuk Binner:",hasil_biner)