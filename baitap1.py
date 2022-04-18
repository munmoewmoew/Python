# bai 1
n = int(input("hay nhap gia tri cua n: "))
S = 0
for i in range(n+1):
    S += i
print ("gia tri cua S la: ", S)
# Bai 2:
n = int(input("hay nhap gia tri cua n: "))
S = 0
for i in range(n+1):
    S += i * i
print ("gia tri cua S la: ", S)
#BAI 3: 
n = int(input("Hay nhap gia tri cua n: "))
S = 0
if n <=0 :
    print("hay nhap gia tri n lon hon 0")
else:
    for i in range(n+1):
        S += float(1/i)
print ("gia tri cua S la: ", S)
#Bai 4:
n = int(input("Hay nhap gia tri cua n: "))
S = float(0)
if n <=0 :
    print("hay nhap gia tri n lon hon 0")
else: 
    for i in range(n+1):
        S += 1/ 2*i
print("Gia tri cua S la: ", S )
#Bai 5:
n = int(input("Hay nhap gia tri cua n: "))
S = float(1)
if n <=0 :
    print("hay nhap gia tri n lon hon 0")
else: 
    for i in range(n+1):
        S +=  1/(2*i+1)
        print(i)
print("Gia tri cua S la: ", S )
#bai 6:
n = int(input("Hay nhap gia tri cua n: "))
S = float(0)
if n <=0 :
    print("hay nhap gia tri n lon hon 0")
else:
    for i in range(n+1):
        S += 1/ (i*(i+1))
print ("gia tri cua S la:", S)
#Bai 7:
n = int(input("Hay nhap gia tri cua n: "))
S = float(0)
if n <=0 :
    print("hay nhap gia tri n lon hon 0")
else:
    for i in range(n+1):
        S += i/(i+1)
print ("gia tri cua S la: ", S)
#Bai 8:
n = int(input("Hay nhap gia tri cua n: "))
S = float(0)
if n <=0 :
    print("hay nhap gia tri n lon hon 0")
else:
    for i in range(n+1):
        S += (2*i+1)/(2*i+2)
print ("gia tri cua S la: ", S)
#Bai 9:
n = int(input("hay nhap gia tri cua n: "))
S = 0
if n <=0 :
    print("hay nhap gia tri n lon hon 0")
else:
    for i in range (n, 0, -1):
        S *= i
print("Gia tri cua S la: ", S)
#Bai 10:
x = int(input("Hay nhap gia tri x: "))
n = int(input("Hay nhap gia tri cua so mu n: "))
S = 0
if x <= 0:
    print("Hau nhap gia tri cua x khac 0")
elif n <= 0:
    print("Hay nhap gia tri n lon hon 0")
else :
    S = x**n
print("Gia tri cua S la: ", S)
#Bai 11:
n = int(input("hay nhap gia tri cua n: "))
S = 1
A = 0
if n <=0 :
    print("hay nhap gia tri n lon hon 0")
else:
    for i in range (1, n+1):
        S *= i
        A += S
print("Gia tri cua S la: ", A)
#Bai 12:
x = int(input("Hay nhap gia tri x: "))
n = int(input("Hay nhap gia tri cua so mu n: "))
S = 0
if x <= 0:
    print("Hau nhap gia tri cua x khac 0") 
elif n <= 0:
    print("Hay nhap gia tri n lon hon 0")
else :
    for i in range(1,n):
        S += x**i
print("Gia tri cua x la: ", S)
#Bai 13:
x = int(input("nhap so x: "))
n = int(input("nhap so mu n: "))
S = 0
if x <= 0:
    print("Hay nhap gia tri cua x lon hon 0")
elif n <= 0:
    print("Hay nhap gia tri n lon hon 0")
else:
    for i in range(1, n + 1):
        S += x**(2*i)
print("Gia tri cua x la: ", S)
#Bai 14:
x = int(input("nhap so x: "))
n = int(input("nhap so mu n: "))
S = 0
if x <= 0:
    print("Hay nhap gia tri cua x lon hon 0") 
elif n <= 0:
    print("Hay nhap gia tri n lon hon 0")
else:
    for i in range(1,n + 1):
        S += x**(2*i+1)
print("Gia tri cua x la: ", S)
#Bai 15:
n = int(input("hay nhap gia tri cua n: "))
S = 0
A = float(0)
if n <= 0:
    print("Hay nhap gia tri cua x lon hon 0") 
elif n <= 0:
    print("Hay nhap gia tri n lon hon 0")
else:
    for i in range(n, 0, -1):
        S += i
        A = 1 / S
print("Gia tri cua S la: ", A)
#Bai 16: 
x = int(input("Hay nhap gia tri x: "))
n = int(input("hay nhap gia tri cua n: "))
S = 0
B = 1
A = float(0)
if n <= 0:
    print("Hay nhap gia tri cua x lon hon 0") 
elif n <= 0:
    print("Hay nhap gia tri n lon hon 0")
else:
    for i in range(1, n+1):
        B = x ** i
        S += i
        A += B / S
print("Gia tri cua S la: ", A)
#Bai17:
x = int(input("Hay nhap gia tri x: "))
n = int(input("hay nhap gia tri cua n: "))
S = 1
B = 1
A = float(0)
if n <= 0:
    print("Hay nhap gia tri cua x lon hon 0") 
elif n <= 0:
    print("Hay nhap gia tri n lon hon 0")
else:
    for i in range(1, n+1):
        B = x ** i
        S *= i
        A += B / S
print("Gia tri cua S la: ", A)
#Bai 18:
x = int(input("Hay nhap gia tri x: "))
n = int(input("hay nhap gia tri cua n: "))
S = 1
B = 1
A = float(0)
if n <= 0:
    print("Hay nhap gia tri cua x lon hon 0") 
elif n <= 0:
    print("Hay nhap gia tri n lon hon 0")
else:
    for i in range(1, n+1):
        B = x ** (2*i)
        S *= 2*i
        A += B / S
print("Gia tri cua S la: ", A)
#Bai 19:
x = int(input("Hay nhap gia tri x: "))
n = int(input("hay nhap gia tri cua n: "))
S = 1
B = 1
A = float(0)
if n <= 0:
    print("Hay nhap gia tri cua x lon hon 0") 
elif n <= 0:
    print("Hay nhap gia tri n lon hon 0")
else:
    for i in range(1, n+1):
        B = x ** (2 *i +1)
        S *= 2* i +1
        A += B / S
print("Gia tri cua S la: ", A)
#Bai 20:
n = int(input("hay nhap gia tri cua n: "))
list_ketqua = []
for i in range (n-1, 0, -1):
    if n%i ==0:
        list_ketqua.append(i)
print(list_ketqua)
#Bai 21:
n = int(input("hay nhap gia tri cua n: "))
list_ketqua = []
for i in range (n, 0, -1):
    if n%i == 0:
        list_ketqua.append(i)
print(" Tong cua cac uoc so la: ", sum(list_ketqua))  
#Bai 22:
n = int(input("hay nhap gia tri cua n: "))
S = 0
list_ketqua = []
for i in range (1, n+1):
    if n%i == 0:
        list_ketqua.append(i)
for i in list_ketqua:
    S *= i
print(" Tong cua cac uoc so la: ", S)  
#Bai 23:
n = int(input("hay nhap gia tri cua n: "))
list_ketqua = []
for i in range (1, n+1):
    if n%i == 0:
        list_ketqua.append(i)
print("So luong uoc so cua so n la: ", len(list_ketqua))
#Bai 24:
n = int(input("hay nhap gia tri cua n: "))
list_ketqua = []
for i in range (1, n+1):
    if n % i == 0: 
        if i % 2  == 1:
            list_ketqua.append(i)
print(" Cac uoc so le cua so n la: ",list_ketqua)
#bai 25:
n = int(input("hay nhap gia tri cua n: "))
list_ketqua = []
for i in range (1, n+1):
    if n % i == 0: 
        if i % 2  == 0:
            list_ketqua.append(i)
print("Tong cac uoc so chan cua so n la:", sum(list_ketqua))
#Bai 26:
n = int(input("hay nhap gia tri cua n: "))
S = 1
list_ketqua = []
for i in range (n, 0, -1):
    if n % i == 0: 
        if i % 2  == 1:
            list_ketqua.append(i)
for i in list_ketqua:
    S *= i
print("Tich cac uoc so le cua so n la:", S)
#Bai 27: 
n = int(input("hay nhap gia tri cua n: "))
list_ketqua = []
for i in range (1, n+1):
    if n % i == 0: 
        if i % 2  == 0:
            list_ketqua.append(i)
print("So luong cac uoc so chan cua so n la:", len(list_ketqua))
#Bai 28:
n = int(input("hay nhap gia tri cua n: "))
list_ketqua = []
for i in range (n-1, 0, -1):
    if n%i == 0:
        list_ketqua.append(i)
print(" Tong cua cac uoc so la: ", sum(list_ketqua)) 
#Bai 29:
n = int(input("hay nhap gia tri cua n: "))
list_ketqua = []
for i in range (1, n+1):
    if n % i == 0: 
        if i % 2  == 1:
            list_ketqua.append(i)
print(" Uoc so le lon nhat la: ",max(list_ketqua))
#Bai 30:
n = int(input("hay nhap gia tri cua n: "))
list_ketqua = []
for i in range (1, n+1):
    if n % i == 0: 
        list_ketqua.append(i)
        if sum(list_ketqua)% n == 0:
            print("so n la so hoan thien")
        elif sum(list_ketqua)% n == 1:
            print("so n khong phai la so hoan thien")
#Bai 31:
n = int(input("hay nhap gia tri cua n: "))
if n == 2:
    print("So n khong phai la so nguyen to")
elif n <= 1:
    print("So n khong phai la so nguyen to")
elif n % 2 ==0:
    print("So n khong phai la so nguyen to") 
else:
    for i in range (1, n+1):
        if n % i == 0:
            print("So n la so nguyen to")
        break

#Bai 32: bai nay lam hoai ma khong co ra a :<<



