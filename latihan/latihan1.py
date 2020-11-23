try :
    file = input('Masukan nama file : ')

    print('Isi file' , file , 'adalah : ')
    file1 = open(file , 'r')
    print(file1.read())

except FileNotFoundError :
    print('File tidak di temukan')
except UnicodeDecodeError :
    print('File tidak bisa di buka')
