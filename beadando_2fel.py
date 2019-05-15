try:
    x = int(input("Adja meg az egész osztót: "))
    for i in range(100000):
        szam = str(i)
        rszam = szam[::-1]
        if szam == rszam and i % x == 0:
            print(szam)


except ValueError:
    print("Nem egész számot adott meg!")
