#komentarz
licznik = 0
while True:
    print licznik,
    licznik += 1
    if licznik >= 5:
        break


for x in xrange(10):
    # Sprawdz, czy x jest parzyste
    if x % 2 == 0:
        continue
    print x,
