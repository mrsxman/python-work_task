# 1
son = 5 # Masalan, musbat son


if son > 0:
 print("A musbat")
else:
 print("A soni musbat emas")

# 2


a = 10 # Masalan, a butun son
if a % 2 == 0:
 print("A soni juft son")
else:
 print("A soni toq son")


# 3

a = 15 # Masalan, a butun son
if a % 2 == 0:
 print(f"{a} soni juft son")
else:
 print(f"{a} soni toq son")


# 4
A = 5 # Masalan, A butun son
B = 3 # Masalan, B butun son
if A > 2 and B == 3:
 print("A>2 va B=3")
else:
 print("A>2 va B=3 rost emas")

# 5

# 6
A = int(input('1-son kriting: '))
B = int(input('2-son kriting: '))
C = int(input('3-son kriting: '))
if A <= B and B <= C:
 print(True)
else:
 print(False)

# 7
A = int(input('1-son kriting: '))
B = int(input('2-son kriting: '))
C = int(input('3-son kriting: '))

if B < A and B > C or B > A and B < C:
 print(True)
else:
 print(False)

# 8
A = int(input('1-son kriting: '))
B = int(input('2-son kriting: '))
if A % 2 == 1 and B % 2 == 1:
 print(True)
else:
 print(False)

# 9
A = int(input('1-son kriting: '))
B = int(input('2-son kriting: '))
if A % 2 == 1 and B % 2 == 1 or A % 2 == 1 or B % 2 == 1:
 print(True)
else:
 print(False)

# 10
A = int(input('1-son kriting: '))
B = int(input('2-son kriting: '))
if A % 2 == 1 and B % 2 == 0 or B % 2 == 1 and A % 2 == 0:
 print(True)
else:
 print(False)

# 11
A = int(input('1-son kriting: '))
B = int(input('2-son kriting: '))
if A % 2 == 1 and B % 2 == 1 or A % 2 == 0 and B % 2 == 0:
 print(True)
else:
 print(False)

# 12
A = int(input('1-son kriting:'))
B = int(input('2-son kriting:'))
C = int(input('3-son kriting:'))
if A > 0 and B > 0 and C > 0:
 print(True)
else:
 print(False)

# 13
A = int(input('1-son kriting: '))
B = int(input('2-son kriting: '))
C = int(input('3-son kriting: '))
if A > 0 or B > 0 or C > 0:
 print(True)
else:
 print(False) 

# 14
A = int(input('1-son kriting: '))
B = int(input('2-son kriting: '))
C = int(input('3-son kriting: '))
if A > 0 and B < 0 and C < 0 or A < 0 and B > 0 and C < 0 or A < 0 and B < 0 and C > 0:
 print(True)
else:
 print(False)

# 15
A = int(input('1-son kriting: '))
B = int(input('2-son kriting: '))
C = int(input('3-son kriting: '))
if A > 0 and B > 0 and C < 0 or A > 0 and B < 0 and C > 0 or A < 0 and B > 0 and C > 0:
 print(True)
else:
 print(False)

# 16
A = int(input('son kriting: '))
if A > 9 and A < 100 and A % 2 == 0:
 print(True)
else:
 print(False)

# 17
A = int(input('son kriting: '))
if A > 99 and A < 1000 and A % 2 == 1:
 print(True)
else:
 print(False)

# 18
A = int(input('1-son kriting: '))
B = int(input('2-son kriting: '))
C = int(input('3-son kriting: '))
if A == B or A == C or B == C:                                                                       
 print(True)
else: 
 print(False)


#  19
A = int(input('число 1: '))
B = int(input('число 2: '))
C = int(input('число 3: '))

if A == -B or A == -C or B == -C:
    print(True)
else:
    print(False)

#  20
A = int(input('трехзначное число: '))
ones = A % 10
teens = A // 10 % 10
huns = A // 100
if ones != teens and ones != huns and teens != huns: 
    print(True) 
else:
    print(False)

# 21
A = int(input('трехзначное число: '))
ones = A % 10
teens = A // 10 % 10
huns = A // 100
if huns < teens and huns < ones and teens < ones:
    print(True)
else:
    print(False)

#  22
A = int(input('трехзначное число: '))
ones = A % 10
teens = A // 10 % 10
huns = A // 100
if huns < teens and huns < ones and teens < ones or huns > teens and huns > ones and teens > ones:
    print(True)
else:
    print(False)

# 23
A = int(input('трехзначное число: '))
ones = A % 10
teens = A // 10 % 10
huns = A // 100
if huns == ones:
    print(True)
else:
    print(False)

# 24


# A, B, C sonlarni olib olamiz
A = float(input("A ni kiriting: "))
B = float(input("B ni kiriting: "))
C = float(input("C ni kiriting: "))

# Diskerminantni hisoblaymiz
D = B**2 - 4*A*C

# Tenglamani haqiqi ildizga ega bo'lishini tekshiramiz
if D > 0:
    print("Kvadrat tenglama haqiqi ildizga ega")
elif D == 0:
    print("Kvadrat tenglama bir haqiqi ildizga ega")
else:
    print("Kvadrat tenglama haqiqi ildizga ega emas")


# 25

# x va y sonlarini olib olamiz
x = float(input("x ni kiriting: "))
y = float(input("y ni kiriting: "))

# Koordinatalari (x, y) bo'lgan nuqta koordinata choragining to'rtinchisida yotadiganligini tekshiramiz
if 1 <= x <= 4 and -2 <= y <= 5:
    print(f"({x}, {y}) nuqta koordinata choragining to'rtinchisida yotadi")
else:
    print(f"({x}, {y}) nuqta koordinata choragining to'rtinchisida yotmaydi")

# 26


# x va y sonlarini olib olamiz
x = float(input("x ni kiriting: "))
y = float(input("y ni kiriting: "))

# Koordinatalari (x, y) bo'lgan nuqta koordinata choragining ikkinchisida yotadiganligini tekshiramiz
if -1 <= x <= 3 and -3 <= y <= 4:
    print(f"({x}, {y}) nuqta koordinata choragining ikkinchisida yotadi")
else:
    print(f"({x}, {y}) nuqta koordinata choragining ikkinchisida yotmaydi")


# 27


# x va y sonlarini olib olamiz
x = float(input("x ni kiriting: "))
y = float(input("y ni kiriting: "))

# Koordinatalari (x, y) bo'lgan nuqta koordinata choragining birinchi yoki uchinchisida yotadiganligini tekshiramiz
if (0 <= x <= 2 and 0 <= y <= 4) or (4 <= x <= 6 and 0 <= y <= 4):
    print(f"({x}, {y}) nuqta koordinata choragining birinchi yoki uchinchisida yotadi")
else:
    print(f"({x}, {y}) nuqta koordinata choragining birinchi yoki uchinchisida yotmaydi")


# 28

# x va y sonlarini olib olamiz
x = float(input("x ni kiriting: "))
y = float(input("y ni kiriting: "))

# Koordinatalari (x, y) bo'lgan nuqta koordinata choragining ikkinchi yoki uchinchisida yotadiganligini tekshiramiz
if (1 <= x <= 3 and -2 <= y <= 5) or (4 <= x <= 6 and -2 <= y <= 5):
    print(f"({x}, {y}) nuqta koordinata choragining ikkinchi yoki uchinchisida yotadi")
else:
    print(f"({x}, {y}) nuqta koordinata choragining ikkinchi yoki uchinchisida yotmaydi")


# 29


# x, y, x1, y1, x2, y2 sonlarini olib olamiz
x = float(input("x ni kiriting: "))
y = float(input("y ni kiriting: "))
x1 = float(input("x1 ni kiriting: "))
y1 = float(input("y1 ni kiriting: "))
x2 = float(input("x2 ni kiriting: "))
y2 = float(input("y2 ni kiriting: "))

# To'rtburchakning tomonlarini o'lchamiz
a = ((x1 - x) ** 2 + (y1 - y) ** 2) ** 0.5  # Chap yuqori chorakdan pastiga bo'lgan masofa
b = ((x2 - x) ** 2 + (y2 - y) ** 2) ** 0.5  # Chap pastikidan pastiga bo'lgan masofa
c = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5  # Chap yuqori chorakdan pastigacha bo'lgan masofa

# Chap yuqori chorak, pastik va pastikni o'z ichiga olgan to'rtburchakning qirqonasi
s = (a + b + c) / 2
area = (s * (s - a) * (s - b) * (s - c)) ** 0.5

# Chap yuqori chorak, pastik va pastikni o'z ichiga olgan to'rtburchak ichida yotganlikni tekshiramiz
if area > 0:
    print(f"({x}, {y}) nuqta, ({x1}, {y1}) va ({x2}, {y2}) tomonlari o'qlariga parallel bo'lgan to'rtburchak ichida yotadi")
else:
    print(f"({x}, {y}) nuqta, ({x1}, {y1}) va ({x2}, {y2}) tomonlari o'qlariga parallel bo'lmagan to'rtburchak ichida yotmaydi")


# 30


def teng_tomonli_uchburchak(a, b, c):
    return a == b == c

# Test qilish
a = int(input("a ni kiriting: "))
b = int(input("b ni kiriting: "))
c = int(input("c ni kiriting: "))

if teng_tomonli_uchburchak(a, b, c):
    print("Uchburchak barcha tomonlari teng tomonli")
else:
    print("Uchburchak barcha tomonlari teng emas")

# 31

def teng_yonli_uchburchak(a, b, c):
    # a, b, c butun sonlar bo'lishi shart
    if type(a) == int and type(b) == int and type(c) == int:
        # Har bir tomon uzunligi qanday o'zgaruvchiga olinishi
        # Sizning maqsadingizga qarab o'zgartirishingiz mumkin
        x = a**2 + b**2 - c**2
        y = b**2 + c**2 - a**2
        z = c**2 + a**2 - b**2

        # Teng yonli uchburchak shartlari
        if x == 0 or y == 0 or z == 0:
            return True

    return False

# Test qilish
a = int(input("a ni kiriting: "))
b = int(input("b ni kiriting: "))
c = int(input("c ni kiriting: "))

if teng_yonli_uchburchak(a, b, c):
    print("Uchburchak teng yonli bo'ladi")
else:
    print("Uchburchak teng yonli emas")


# 32

from math import acos, degrees, radians

def teng_burchakli_uchburchak(a, b, alpha):
    # burchakni radianlarda olib chiqamiz
    alpha_rad = alpha

    # Uchburchakning burchaklarini topish
    beta = acos((a**2 + b**2 - 2 * a * b * acos(alpha_rad)) / (2 * a * b))
    gamma = acos((a**2 + b**2 - 2 * a * b * acos(alpha_rad)) / (2 * a * b))

    # Barcha burchaklar teng bo'lishi shartlari
    if alpha_rad == beta == gamma:
        return True

    return False

# Test qilish
a = float(input("a ni kiriting: "))
b = float(input("b ni kiriting: "))
alpha_degrees = float(input("alpha burchakni darajada kiriting: "))

# Burchakni radianlarga o'tkazamiz
alpha_radians = radians (alpha_degrees)

if teng_burchakli_uchburchak(a, b, alpha_radians):
    print("Uchburchak barcha burchaklari teng bo'ladi")
else:
    print("Uchburchak barcha burchaklari teng emas")


# 33


def is_square_light(x, y):
    # Berilgan (x, y) maydonning oq qoraligi bo'lishini tekshirish
    # Oq qoraligida x + y juft son bo'lishi kerak
    if (x + y) % 2 == 0:
        return True
    else:
        return False

# Test qilish
x = 3
y = 4
result = is_square_light(x, y)

if result:
    print(f"({x}, {y}) maydoni oq (oq/odd) qoraligiga tegishli.")
else:
    print(f"({x}, {y}) maydoni oq (oq/odd) qoraligiga tegishli emas.")



# 34

def is_triangle_possible(a, b, c):
    # Uchburchakning tomonlarining sonlari butun son bo'lishini tekshirish
    if isinstance(a, int) and isinstance(b, int) and isinstance(c, int):
        # Uchburchakning shartlarini tekshirish
        if a + b > c and a + c > b and b + c > a:
            return True
        else:
            return False
    else:
        return False

# Test qilish
a = 3
b = 4
c = 5
result = is_triangle_possible(a, b, c)

if result:
    print(f"{a}, {b}, va {c} tomonli uchburchak yasash mumkin.")
else:
    print(f"{a}, {b}, va {c} tomonli uchburchak yasash mumkin emas.")


# 35

def are_squares_same_color(x1, y1, x2, y2):
    # Maydonlarning rangini aniqlash
    color1 = (x1 + y1) % 2
    color2 = (x2 + y2) % 2

    # Maydonlarning ranglarini solishtirish
    if color1 == color2:
        return True
    else:
        return False

# Test qilish
x1, y1 = 1, 2
x2, y2 = 3, 4
result = are_squares_same_color(x1, y1, x2, y2)

if result:
    print(f"({x1}, {y1}) va ({x2}, {y2}) maydonlar bir xil rangda.")
else:
    print(f"({x1}, {y1}) va ({x2}, {y2}) maydonlar bir xil rangda emas.")


# 36



def are_squares_same_color(x1, y1, x2, y2):
    # Maydonlarning rangini aniqlash
    color1 = (x1 + y1) % 2
    color2 = (x2 + y2) % 2

    # Maydonlarning ranglarini solishtirish
    if color1 == color2:
        return True
    else:
        return False

# Test qilish
x1, y1 = 1, 2
x2, y2 = 3, 4
result = are_squares_same_color(x1, y1, x2, y2)

if result:
    print(f"({x1}, {y1}) va ({x2}, {y2}) maydonlar bir xil rangda.")
else:
    print(f"({x1}, {y1}) va ({x2}, {y2}) maydonlar bir xil rangda emas.")


# 37



def can_king_move(x1, y1, x2, y2):
    # Shohning yurishida bir maydondan ikkinchisiga o'tish tekshiriladi
    if abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1:
        return True
    else:
        return False

# Test qilish
x1, y1 = 4, 5
x2, y2 = 5, 6
result = can_king_move(x1, y1, x2, y2)

if result:
    print(f"Shoh bir yurishda ({x1}, {y1}) dan ({x2}, {y2}) ga o'ta oladi.")
else:
    print(f"Shoh bir yurishda ({x1}, {y1}) dan ({x2}, {y2}) ga o'ta olmaydi.")


# 38

def rostlikka_tekshir(x1, y1, x2, y2):
    if (x1 + y1) % 2 == (x2 + y2) % 2:
        return "Fil bir maydondan ikkinchisiga o'ta oladi"
    else:
        return "Fil bir maydondan ikkinchisiga o'tmaydi"

# Test qilish uchun misol
x1, y1 = 1, 1
x2, y2 = 3, 3

natija = rostlikka_tekshir(x1, y1, x2, y2)
print(natija)


# 39


def rostlikka_tekshir(x1, y1, x2, y2):
    if (abs(x1 - x2) == 1 and abs(y1 - y2) == 2) or (abs(x1 - x2) == 2 and abs(y1 - y2) == 1):
        return "Farzin bir yurishda bir maydondan ikkichisiga o'ta oladi"
    else:
        return "Farzin bir yurishda bir maydondan ikkichisiga o'tmaydi"

# Test qilish uchun misol
x1, y1 = 1, 1
x2, y2 = 2, 3

natija = rostlikka_tekshir(x1, y1, x2, y2)
print(natija)


# 40


def rostlikka_tekshir(x1, y1, x2, y2):
    if abs(x1 - x2) == 1 and abs(y1 - y2) == 1:
        return "Ot bir maydondan ikkinchisiga o'ta oladi"
    else:
        return "Ot bir maydondan ikkinchisiga o'tmaydi"

# Test qilish uchun misol
x1, y1 = 1, 2
x2, y2 = 2, 3

natija = rostlikka_tekshir(x1, y1, x2, y2)
print(natija)


