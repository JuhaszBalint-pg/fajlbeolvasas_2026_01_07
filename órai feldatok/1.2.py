''''
1. Feladat
A mellékelt fájl néhány ismert programozási nyelv adatát tartalmazza. Olvasd be a fájl tartalmát és tárold el
a, egy listában, melynek elemei szótárak,
b, egy kétdimenziós listában!
mind a két esetben az évszám int típusként kerüljön rögzítésre!
(Fájl letöltése: kattints a "Forrásfájl" feliratú gombra az egér jobb gombjával, és a felugró menüből válaszd a "Link mentése másként..." opciót!)
'''

nyelvek = []
years = []
with open('adatok/nyelvek.csv' , 'r', encoding='utf-8') as forrasfajl:
    next(forrasfajl)
    next (forrasfajl)
    for sor in forrasfajl:
        nyelvek_adatai = sor.strip().split(';')
        year = int(nyelvek_adatai[0])
        language = nyelvek_adatai[1]
        first_name = nyelvek_adatai[2]
        last_name = nyelvek_adatai[3]
        nyelvek.append([year, language, first_name, last_name])
        print (f'{year} {language} {first_name} {last_name}')
        years.append(year)

print (min(years))
print (max(years))