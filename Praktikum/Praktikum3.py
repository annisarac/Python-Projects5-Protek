try:
    file = open('d:/data2.txt' , 'r')
    
    sum = 0
    for data in file:
        try:
            sum = sum + int(data)
        
        except ValueError:
            continue

    print(sum)

except FileNotFoundError:
    print('File tidak di temukan')
