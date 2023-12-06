# 1
# Foydalanuvchidan son olish
son = float(input("Iltimos, son kiriting: "))

# Shart operatori orqali tekshirish
if son > 0:
    # Agar son musbat bo'lsa, 1 ga oshiramiz
    son += 1
    print(f"Natija: {son}")
else:
    # Agar son manfiy yoki 0 bo'lsa, o'zgartirmaslik
    print("Natija: Son manfiy yoki 0, o'zgartirilmadi.")
# 2
# Foydalanuvchidan butun son olish
son = int(input("Iltimos, butun son kiriting: "))

# Shart operatori orqali tekshirish
if son > 0:
    # Agar son musbat bo'lsa, 1 ga oshiramiz
    son += 1
else:
    #  Agar son manfiy yoki 0 bo'lsa, 2 ga kamaytiramiz
    son -= 2
# hnNatijani ekranga chiqaramiziy    
print(f"Natija: {son}")
# 3
# Foydalanuvchidan butun son olish
son = int(input("Iltimos, butun son kiriting: "))
# Shart operatori orqali tekshirish
if son > 0:
    # Agar son musbat bo'lsa, 1 ga oshiramiz
    son += 1
elif son < 0:
    # Agar son manfiy bo'lsa, 2 ga kamaytiramiz
    son -= 2
else:
    # Agar son 0 bo'lsa, 10 ni o'zlashtiramiz
    son = 10

# Natijani ekranga chiqaramiz

print(f"Natija: {son}")

#  4

# Foydalanuvchidan uchta butun son olish
son1 = int(input("Birinchi butun sonni kiriting: "))
son2 = int(input("Ikkinchi butun sonni kiriting: "))
son3 = int(input("Uchinchi butun sonni kiriting: "))
# Musbat sonlar sonini sanash uchun o'zgaruvchilar
musbat_sonlar = 0
# Shart operatorlari orqali tekshirish
if son1 > 0:
    musbat_sonlar += 1
if son2 > 0:
    musbat_sonlar += 1
if son3 > 0:
    musbat_sonlar += 1
# Natijani ekranga chiqaramiz
print(f"Musbat sonlar soni: {musbat_sonlar}")
# 5
# Foydalanuvchidan uchta butun son olish
son1 = int(input("Birinchi butun sonni kiriting: "))
son2 = int(input("Ikkinchi butun sonni kiriting: "))
son3 = int(input("Uchinchi butun sonni kiriting: "))
# Musbat va manfiy sonlar sonini sanash uchun o'zgaruvchilar
musbat_sonlar = 0
manfiy_sonlar = 0
# Shart operatorlari orqali tekshirish
if son1 > 0:
    musbat_sonlar += 1
elif son1 < 0:
    manfiy_sonlar += 1
if son2 > 0:
    musbat_sonlar += 1
elif son2 < 0:
    manfiy_sonlar += 1
if son3 > 0:
    musbat_sonlar += 1
elif son3 < 0:
    manfiy_sonlar += 1
# Natijani ekranga chiqaramiz
print(f"Musbat sonlar soni: {musbat_sonlar}")
print(f"Manfiy sonlar soni: {manfiy_sonlar}")
# 6
# Foydalanuvchidan ikkita butun son olish
son1 = int(input("Birinchi butun sonni kiriting: "))
son2 = int(input("Ikkinchi butun sonni kiriting: "))
# Kattasi sonini aniqlash uchun o'zgaruvchi
katta_son = 0
# Shart operatori orqali tekshirish
if son1 > son2:
    katta_son = son1
else:
    katta_son = son2
# Natijani ekranga chiqaramiz
print(f"Kattasi son: {katta_son}")
# 7
# Foydalanuvchidan ikkita butun son olish
son1 = int(input("Birinchi butun sonni kiriting: "))
son2 = int(input("Ikkinchi butun sonni kiriting: "))
# Kichigi sonini aniqlash uchun o'zgaruvchi
kichik_son = 0
# Shart operatori orqali tekshirish
if son1 < son2:
    kichik_son = son1
else:
    kichik_son = son2
# Natijani ekranga chiqaramiz
print(f"Kichigi son: {kichik_son}")
# 8
# Foydalanuvchidan ikkita butun son olish
son1 = int(input("Birinchi butun sonni kiriting: "))
son2 = int(input("Ikkinchi butun sonni kiriting: "))
# Avval katta, keyin kichigini aniqlash uchun o'zgaruvchilar
katta_son = 0
kichik_son = 0
# Shart operatorlari orqali tekshirish
if son1 > son2:
    katta_son = son1
    kichik_son = son2
else:
    katta_son = son2
    kichik_son = son1
# Natijani ekranga chiqaramiz
print(f"Avval katta, keyin kichik sonlar: {katta_son}, {kichik_son}")
# 9
# Foydalanuvchidan haqiqiy sonlarni olish
A = float(input("A sonni kiriting: "))
B = float(input("B sonni kiriting: "))
# Shart operatori orqali tekshirish va almashtirish
if A < B:
    A, B = B, A
# Natijani ekranga chiqaramiz
print(f"A son: {A}")
print(f"B son: {B}")
# 10
# Foydalanuvchidan butun sonlarni olish
A = int(input("A sonni kiriting: "))
B = int(input("B sonni kiriting: "))
# Shart operatori orqali tekshirish
if A != B:
    A = A + B
    B = A
else:
    A = 0
    B = 0
# Natijani ekranga chiqaramiz  
print(f"A son: {A}")
print(f"B son: {B}")

#  11


a = int(input("a ni kiriting: "))
b = int(input("b ni kiriting: "))

if a != b:
    if a > b:
        a, b = b, a
else:
    a = b = 0

print(f"a = {a}, b = {b}")


# 12


# Uchta son kiritiladi
son1 = float(input("Birinchi sonni kiriting: "))
son2 = float(input("Ikkinchi sonni kiriting: "))
son3 = float(input("Uchinchi sonni kiriting: "))

# Eng kichik sonni aniqlash
kichik_son = son1

if son2 < kichik_son:
    kichik_son = son2

if son3 < kichik_son:
    kichik_son = son3

# Natijani ekranga chiqarish
print(f"Uchta sonning eng kichigi: {kichik_son}")


# 13


# Uchta son kiritiladi
son1 = float(input("Birinchi sonni kiriting: "))
son2 = float(input("Ikkinchi sonni kiriting: "))
son3 = float(input("Uchinchi sonni kiriting: "))

# O'rtacha sonni aniqlash
if son1 <= son2 <= son3 or son3 <= son2 <= son1:
    ortacha_son = son2
elif son2 <= son1 <= son3 or son3 <= son1 <= son2:
    ortacha_son = son1
else:
    ortacha_son = son3

# Natijani ekranga chiqarish
print(f"Uchta sonning o'rtachasi: {ortacha_son}")


# 14


# Uchta son kiritiladi
son1 = float(input("Birinchi sonni kiriting: "))
son2 = float(input("Ikkinchi sonni kiriting: "))
son3 = float(input("Uchinchi sonni kiriting: "))

# Kichigini aniqlash
kichik_son = son1

if son2 < kichik_son:
    kichik_son = son2

if son3 < kichik_son:
    kichik_son = son3

# Kattasini aniqlash
katta_son = son1

if son2 > katta_son:
    katta_son = son2

if son3 > katta_son:
    katta_son = son3

# Natijani ekranga chiqarish
print(f"Kichik son: {kichik_son}")
print(f"Katta son: {katta_son}")


# 15


# Uchta son kiritiladi
son1 = float(input("Birinchi sonni kiriting: "))
son2 = float(input("Ikkinchi sonni kiriting: "))
son3 = float(input("Uchinchi sonni kiriting: "))

# Yig'indini aniqlash
yigindi1 = son1 + son2
yigindi2 = son2 + son3
yigindi3 = son1 + son3

# Eng katta yig'indini aniqlash
eng_katta_yigindi = max(yigindi1, yigindi2, yigindi3)

# Natijani ekranga chiqarish
print(f"Ikkita sonning eng katta yig'indisi: {eng_katta_yigindi}")

# 16


# Haqiqiy sonlarni kiritish
a = float(input("a ni kiriting: "))
b = float(input("b ni kiriting: "))
c = float(input("c ni kiriting: "))

# O'sish tartibini tekshirish
if a <= b <= c:
    a *= 2
    b *= 2
    c *= 2
else:
    a = -a
    b = -b
    c = -c

# Natijani ekranga chiqarish
print(f"a = {a}, b = {b}, c = {c}")


# 17


# Haqiqiy sonlarni kiritish
a = float(input("a ni kiriting: "))
b = float(input("b ni kiriting: "))
c = float(input("c ni kiriting: "))

# O'sish yoki kamayish tartibini tekshirish
if a <= b <= c or a >= b >= c:
    a *= 2
    b *= 2
    c *= 2
else:
    a = -a
    b = -b
    c = -c

# Natijani ekranga chiqarish
print(f"a = {a}, b = {b}, c = {c}")



# 18


# Uchta butun sonni olish
son1 = int(input("Birinchi sonni kiriting: "))
son2 = int(input("Ikkinchi sonni kiriting: "))
son3 = int(input("Uchinchi sonni kiriting: "))

# Ikkitasi o'zaro teng va bittasi tartib raqamiga mos kelgan sonni topish
if son1 == son2 == son3:
    print("Uchta son ham bir biriga teng")
elif son1 == son2:
    print("Uchta sonning birinchi va ikkinchi sonlari bir biriga teng")
elif son2 == son3:
    print("Uchta sonning ikkinchi va uchinchi sonlari bir biriga teng")
elif son1 == son3:
    print("Uchta sonning birinchi va uchinchi sonlari bir biriga teng")
else:
    print("Hech bir to'g'ri keluvchi moslik topilmadi")

# 19

# To'rtta butun sonni olish
son1 = int(input("Birinchi sonni kiriting: "))
son2 = int(input("Ikkinchi sonni kiriting: "))
son3 = int(input("Uchinchi sonni kiriting: "))
son4 = int(input("To'rtinchi sonni kiriting: "))

# Uchta o'zaro teng sonlarni aniqlash
if son1 == son2 == son3:
    print("Uchta son bir biriga teng")
elif son1 == son2 == son4:
    print("Uchta son bir biriga teng")
elif son1 == son3 == son4:
    print("Uchta son bir biriga teng")
elif son2 == son3 == son4:
    print("Uchta son bir biriga teng")
else:
    print("Hech bir to'g'ri keluvchi moslik topilmadi")


# 20
# Nuqtalarni olish
xA = float(input("A nuqtasi x koordinatasini kiriting: "))
yA = float(input("A nuqtasi y koordinatasini kiriting: "))

xB = float(input("B nuqtasi x koordinatasini kiriting: "))
yB = float(input("B nuqtasi y koordinatasini kiriting: "))

xC = float(input("C nuqtasi x koordinatasini kiriting: "))
yC = float(input("C nuqtasi y koordinatasini kiriting: "))

# A, B va C nuqtalari orasidagi masofalarni hisoblash
AB_masofa = ((xB - xA)**2 + (yB - yA)**2)**0.5
AC_masofa = ((xC - xA)**2 + (yC - yA)**2)**0.5
BC_masofa = ((xC - xB)**2 + (yC - yB)**2)**0.5

# Eng yaqin nuqtani aniqlash
if AB_masofa < AC_masofa and AB_masofa < BC_masofa:
    print("A nuqtasiga eng yaqin nuqta B nuqtasi va masofasi:", AB_masofa)
elif AC_masofa < AB_masofa and AC_masofa < BC_masofa:
    print("A nuqtasiga eng yaqin nuqta C nuqtasi va masofasi:", AC_masofa)
else:
    print("A nuqtasiga eng yaqin nuqta B nuqtasi va masofasi:", BC_masofa)


# 21

# Nuqta kordinatasini olish
x = float(input("Nuqta x koordinatasini kiriting: "))
y = float(input("Nuqta y koordinatasini kiriting: "))

# Nuqta joylashgan o'qni aniqlash
if x == 0 and y == 0:
    print("Nuqta kordinata boshida joylashgan (0, 0)")
elif x == 0 or y == 0:
    print("Nuqta OX yoki OY o'qlarida joylashgan (1)")
else:
    print("Nuqta koordinata o'qida joylashmagan (2)")


# 22

# Nuqta kordinatasini olish
x = float(input("Nuqta x koordinatasini kiriting: "))
y = float(input("Nuqta y koordinatasini kiriting: "))

# Nuqta joylashgan koordinata choragini aniqlash
if x > 0 and y > 0:
    print("Nuqta I choragida joylashgan")
elif x < 0 and y > 0:
    print("Nuqta II choragida joylashgan")
elif x < 0 and y < 0:
    print("Nuqta III choragida joylashgan")
elif x > 0 and y < 0:
    print("Nuqta IV choragida joylashgan")
else:
    print("Nuqta OX va OY o'qlarida yotmaydi")


# 23


# Uchta to'g'ri to'rtburchak uchining koordinatalarini olish
x1 = float(input("1-chi nuqta x koordinatasini kiriting: "))
y1 = float(input("1-chi nuqta y koordinatasini kiriting: "))

x2 = float(input("2-chi nuqta x koordinatasini kiriting: "))
y2 = float(input("2-chi nuqta y koordinatasini kiriting: "))

x3 = float(input("3-chi nuqta x koordinatasini kiriting: "))
y3 = float(input("3-chi nuqta y koordinatasini kiriting: "))

# Koordinata o'qlari parallel ravishda to'g'ri to'rtburchak uchining to'rtinchi uchini aniqlash
if y1 == y2 and y2 == y3:
    x4 = x3
    y4 = y3 + (y2 - y1)
    print(f"To'rtinchi uchining koordinatalari: ({x4}, {y4})")
else:
    print("Koordinata o'qlari parallel ravishda to'g'ri to'rtburchak emas.")

# 24


def calculate_function(X):
    # Funksiya hisoblash
    if X > 0:
        result = 2 * X + 1
    elif X == 0:
        result = 0
    else:
        result = X**2 - 1

    return result

# Funksiya uchun X ni olish
X = float(input("X ni kiriting: "))

# Funksiyani chaqirib natijani chiqarish
result = calculate_function(X)
print(f"Funksiya natijasi: {result}")


# 25


X = 5
natija = X if X > 0 else 0
print(natija)


# 26


def funksiya(x, y, z):
    natija = x + y + z
    return natija

# 3 ta son kiritish
x = float(input("Birinchi sonni kiriting: "))
y = float(input("Ikkinchi sonni kiriting: "))
z = float(input("Uchunchi sonni kiriting: "))

# Natijani hisoblash va ekranga chiqarish
natija = funksiya(x, y, z)
print(f"Natija: {natija}")


# 27

def takrorlash_funksiyasi(x):
    natija = x * 3
    return natija

# Haqiqiy sonni kiritish
x = float(input("Haqiqiy sonni kiriting: "))

# Natijani hisoblash va ekranga chiqarish
natija = takrorlash_funksiyasi(x)
print(f"Takrorlangan natija: {natija}")


# 28

# Yilni kiritish
yil = int(input("Yilni kiriting: "))

# Shart operatori orqali kabisa yilni aniqlash
if (yil % 4 == 0 and yil % 100 != 0) or (yil % 400 == 0):
    print(f"{yil} - Kabisa yil, kunlar soni: 366")
else:
    print(f"{yil} - Kabisa yil emas, kunlar soni: 365")


# 29

# Sonni kiritish
son = int(input("Istalgan sonni kiriting: "))

# Shart operatori orqali sonning xususiyatlarini tekshirish
if son > 0:
    print(f"{son} - Musbat son")
elif son < 0:
    print(f"{son} - Manfiy son")
elif son == 0:
    print(f"{son} - Nol")
else:
    print(f"{son} - Toq son")

# Sonni kvadratini hisoblash
son_kvadrati = son ** 2
print(f"{son} ning kvadrati: {son_kvadrati}")



# 30

# Sonni kiritish
son = int(input("1 dan 999 gacha son kiriting: "))

# Shart operatori orqali sonning xususiyatlarini tekshirish
if son < 1 or son > 999:
    print("Noto'g'ri kirish! Faqat 1 dan 999 gacha son kiriting.")
else:
    ikki_nonali_juft_uch_nolari_toq = (son % 2 == 0) and (son % 3 == 0) and (son % 1000 != 0)
    
    if ikki_nonali_juft_uch_nolari_toq:
        print(f"{son} - Ikki nonali, juft, uch nolari toq, x.k sifatida")
    elif son % 2 == 0:
        print(f"{son} - Juft son")
    else:
        print(f"{son} - Toq son")
