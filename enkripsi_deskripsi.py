import string 
abjad = string.printable

def enkrip(pesan) :
    global abjad

    key = int(input('Masukan Key                 :  '))
    cipher = '' #menampilkan chiper enkripsi sesuai kaidah chiper caesar
    for i in pesan:
        if i in abjad:
            k = abjad.find(i) #menentukan variabel sebelumnya yang sudah dijadikan pemanggil
            k = (k + key)%100
            cipher = cipher+abjad[k]
        else:
            cipher = cipher + i
    return cipher

def dekrip(cipher) :
    global abjad
    key = int(input('Masukan Key                 :  '))
    pesan = '' #menampilkan pesan dekripsi sesuai kaidah chiper caesar
    for i in cipher: 
        if i in abjad:
            k = abjad.find(i) 
            k = (k - key)%100
            pesan = pesan+abjad[k]
        else: 
            pesan = pesan + i
    return pesan

if __name__ == '__main__':
    print('-------------------------------------------')
    print('|-----BY RANNY FEBRIANA (20190801298)-----|')
    print('-------------------------------------------')
  
    option = int(input('1. Enkripsi\n2. Dekripsi\nPilih Option                :  '))
    if option == 1:
        pesan = input('Masukan pesan (Plaintext)   :  ')
        print(enkrip(pesan))
    elif option == 2:
        cipher = input('Masukan pesan (Chipertext)  :  ')
        print(dekrip(cipher))
    else:
        print('Masukan option 1 atau 2!!')