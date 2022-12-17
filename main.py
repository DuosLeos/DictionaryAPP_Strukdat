import DataStructure as ds
import os
import csv
os.system('cls')

tree = ds.RedBlackTree()  # initialize RB-tree
DICTIONARY_NAME = "bahasa indonesia"


def readFile(fileName):
    file = open(fileName, "r")
    for i in file:
        if not tree.search(i.rstrip('\n')):
            tree.insert(i.rstrip('\n'))
    file.close()

def deleteFile(fileName):
    with open(fileName , "r") as fp:
        lines = fp.readlines()

    with open(fileName , "w") as fp:
        halo = input("Kata yang ingin dihapus: ")
        for line in lines:
            if line.strip("\n") != halo :
                fp.write(line)


while True:
    print("\n========================================= SELAMAT DATANG ==============================================")
    print("                         --- A P L I K A S I   K A M U S   B A H A S A ---                          ")
    print("\nApa yang ingin kamu cari?")
    opsi = input(
        "1- Load Kamus\"" + DICTIONARY_NAME +"\"    \t2- Tampilkan Jumlah Kata\n"
        "3- Masukkan Kata                   \t4- Cek Kata\n"
        "5- Tampilkan Tinggi Tree           \t6- Tampilkan Node Hitam Dalam Tree\n"
        "7- Delete kamus                    \t8- Keluar\n"
        "> ")
    

    if opsi == '1':
        readFile(DICTIONARY_NAME + ".txt")
        print(DICTIONARY_NAME + " loaded SUKSES!")

    elif opsi == '2':
        print(DICTIONARY_NAME + ' saat ini berisi ' + str(tree.number_of_nodes) + ' kata!')

    elif opsi == '3':
        s = str(input("Tulis kata yang ingin di inputkan: ")).strip()
        with open("bahasa indonesia.txt", "a+") as myfile:
            myfile.write(str(s)+'\n')
        if tree.search(s.lower()):
            print("\"" + s + "\" sudah ada dalam kamus")
        elif len(s) > 0 and not s.isspace():
            tree.insert(s.lower())
            print('\"' + s + '\" Kata Berhasil Di Inputkan')
        else:
            print('Gagal di inputkan')
        

    elif opsi == '4':
        s = str(input("Masukkan Kata Untuk Di Cek: ")).strip()
        if tree.search(s.lower()):
            print("\"" + s + '\" DITEMUKAN!')
        else:
            print("\"" + s + '\" TIDAK ADA DALAM KAMUS')

    elif opsi == '5':
        print(tree.heightOfTree(tree.root, 0))

    elif opsi == '6':
        print(tree.getBlackHeight())
    
    elif opsi == '7':
        s = str(input("Tulis kata yang ingin di hapus: "))
        with open("bahasa indonesia.txt", "r") as fp:
            lines = fp.readlines()
        with open("bahasa indonesia.txt", "w") as fp:
            for line in lines:
                if line.strip("\n") != s:
                    fp.write(line)
   
    elif opsi == '8':
        print("Terimakasih Sudah Menggunakan Aplikasi Ini! :)")
        break

    print()
