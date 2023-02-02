db= {1:['Rice', 20], 2:['Puri-Bhaji', 50], 3:['Puran-Poli', 100], 4:['Bhaji-Bhakari', 100], 5:['Edali', 30], 6:['Dosa', 40], 7:['Uthappa', 40], 8:['Vada-Sambhar', 30], 9:['Vada-Pav', 20], 10:['Samosa', 25], 11:['Poha', 25], 12:['Upama', 30], 13:['Biryani', 100], 14:['Chicken65', 80], 15:['Tandur', 25], 16:['Lolipop', 25], 17:['Tea', 10], 18:['Green-Tea', 15], 19:['Cold-Coffee', 25], 20:['Hot-Coffee', 20],}

print('\t\t ...Welcome To Hotel Sahyadri...')

print('''
                \t\t\t\tMenu''')
print('_'*100)
print('''
        A=Veg               B=South-Indian     C=Break-Fast       D=Non_Veg          E=Tea

        1=Rice              5=Edali            9=Vada-Pav         13=Biryani         17=Tea
        2=Puri-Bhaji        6=Dose             10=Samosa          14=Chicken65       18=Green-Tea
        3=Puran-Poli        7=Uthappa          11=Poha            15=Tandur          19=Cold-Coffee
        4=Bhaji-Bhakari     8=Vada-Sambhar     12=Upama           16=Lolipop         20=Hot-Coffee
                  
                  ''')
print('*'*100)
l=[]
while True:
    ch=int(input('Enter Your Order Number:'))


    q=int(input('Enter Quantity:'))


    t=(ch,q)
    l.append(t)
    choice=input('Do You Want To Continue y/n:')
    if choice=='n':

        print('_'*75)
        s=0
        print("{m:<15}| {u:^15}| {q:^15}| {t:^15}|".format(m='Menu', u='UnitPrice',q='Quantity',t='Total'))
        print('_'*75)
        for i in l:

            print("{:<15}|{:^15}|{:^15}|{:^15}|".format(db[i[0]][0],db[i[0]][1],i[1],db[i[0]][1]*i[1]))
            print('_'*75)
            s=s+db[i[0]][1]*i[1]
            
            s2=s/100*105
        print('Total Bill is=',s)
            
        print('GST is 5%')
        print('Total bill is =',s2)
        print('With Including GST')
        print('\t\t\t!!Thank You___Visit Again!!')
        print('*'*75)

        break