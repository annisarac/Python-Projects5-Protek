try :
    NamaFile = input('Masukan nama file : ')
    file1 = open(NamaFile , 'r')
    file = open(NamaFile , 'a')
    
    while True :
        data = input('Data yang mau ditambahkan : ')
        file.write(data)
    
        tambah = str(input('Mau lagi (y/n) : '))
        if tambah == 'y' :
            True
        elif tambah == 'n' :
            break
        else :
            print('Inputan invalid')
            break

    file.close()

except FileNotFoundError:
    print('File tidak di temukan')
