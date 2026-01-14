'''
A mellékelt fájl néhány ismert programozási nyelv adatát tartalmazza.
Olvasd be a fájl tartalmát, és másold át azt egy fájlba úgy,
hogy abba már csak a nyelv és az évszám kerüljön!
'''

with open ('../adatok/nyelvek.csv', 'r', encoding='Utf-8') as forrasfajl, \
     open ('../adatok/nyelvek_masolat.csv', 'w', encoding='utf-8') as celfajl:
    next(forrasfajl)
    next(forrasfajl)
    for sor in forrasfajl:
        adatok = sor.strip().split(';')
        evszam = adatok[0]
        nyelv = adatok[1]
        celfajl.write(f'{evszam} , {nyelv}\n')

print('A fájl sikeresen kiirva!')

