#SORU 1
y = input("Gün-Ay-Yıl:  ")
u,s,f = y.split("-")
e = {"01":"Ocak", "02":"Şubat", "03":"Mart", "04": "Nisan", "05": "Mayıs", "06": "Haziran", "07": "Temmuz","08":"Ağustos","09":"Eylül","10": "Ekim","11":"Kasım","12":"Aralık"}
print(u,e[s], f)


#SORU 2
y=int(input("Sayı Giriniz: "))

if y < 0:
    print(y, "Negatif Sayı ! , sonuç hesaplanamıyor.")
    
elif 9 > y >= 0:
    u = 1
    for s in range(1, y + 1):
        u = u * s
    f= u * 3
    print("Sonuç: ",f)
    
elif 9 <= y < 16:
    e = 0
    for m in range((2*y)+1):
        if m % 2 != 0:
            continue
        e+=m
    print("Sonuç: ",e)
    
elif y >= 16:
    print("Girilen Sayı 16 veya 16'dan Büyük ! , sonuç hesaplanamıyor.")



#SORU 3
y=[]
u = {"a":"1","b":"2","c":"3","d":"4","e":"5","f":"6","g":"7","h":"8","i":"9","j":"10","k":"11","l":"12","m":"13","n":"14","o":"15","p":"16","q":"17","r":"18","s":"19","t":"20","u":"21","v":"22","w":"23","x":"24","y":"25","z":"26",}
s=[] #sifre


f = [[1 , 2 , -1],
     [2 , 5 , 2 ],
     [-1 ,-2 ,2 ]]

# "yusufkork" (9 harf) harflerine karşılık gelen sayılar
e = [[25 , 21 , 19],
     [21 , 6 , 19],
     [15 , 18 , 11]]


m = [[0,0,0],  
          [0,0,0],  
          [0,0,0]]  


for r in 'yusufkork':
    y.append(u[r])
print(" 'yusufkork' : İsmine Karşılık Gelen Sayılar : ")
print("______________________________________")
print(" ")

k1=y[0],y[1],y[2]
o=y[3],y[4],y[5]
a=y[6],y[7],y[8]
print(k1)
print(o)
print(a)
print(" ")
print(" ")
print("Sayıların Matrisi : ")
print("______________________________________")


for z in range(len(f)):  
   for y2 in range(len(e[0])):  
       for u2 in range(len(e)):  
           m[z][y2] += f[z][u2] * e[u2][y2]  
for s2 in m: 
    print(s2)  
    s.append(s2)
print("")
print(s)
    

#SORU 4
y=[]
for u in range(1,37 + 1):
   if u > 1:
       for s in range(2,u):
           if (u % s) == 0:
               break
       else:
           y+=[u]
         
print("Asal Sayılar Listesi: ")
print(y)


