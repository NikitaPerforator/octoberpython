a=4*25*50*100
mb=a/1024**2
cout=1
while mb<=1.44:
    mb+=mb
    cout+=1
print("Количество книг, помещающихся на дискету:",cout)
