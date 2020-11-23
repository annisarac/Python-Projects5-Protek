print('----------------------------------------')
print('PROGRAM MENGHITUNG BILANGAN BULAT')
print('----------------------------------------')

bilangan = 0
jumlah = 0
while True :
    try :
        bil = int(input('Masukan bilangan bulat : ' ))
        bilangan += bil
        jumlah += 1
        lanjut = str(input('Lagi (y/n)? : '))
        if lanjut == 'y' :
            True
        elif lanjut == 'n' :
            break
        else :
            print('Inputan invalid')
            break
        
    except ValueError :
        print('Bukan bilangan bulat')

rerata = bilangan / jumlah
print('Rata-ratanya adalah: ' , rerata)
