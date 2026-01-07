''''
1. Feladat
A mellékelt fájl néhány ismert programozási nyelv adatát tartalmazza. Olvasd be a fájl tartalmát és tárold el
a, egy listában, melynek elemei szótárak,
b, egy kétdimenziós listában!
mind a két esetben az évszám int típusként kerüljön rögzítésre!
(Fájl letöltése: kattints a "Forrásfájl" feliratú gombra az egér jobb gombjával, és a felugró menüből válaszd a "Link mentése másként..." opciót!)
'''

nyelvek = []
with open('adatok/nyelvek.csv' , 'r', encoding='utf-8') as forrasfajl:
    next(forrasfajl)
    next (forrasfajl)
    for sor in forrasfajl:
        nyelvek_adatai = sor.strip().split(';')
        nyelv = {'year': int(nyelvek_adatai[0]), 'programming language': nyelvek_adatai[1], 'first name': nyelvek_adatai[2], 'last name': nyelvek_adatai[3]}
        nyelvek.append(nyelv)

for nyelv in nyelvek:
    print(nyelv)

legfi_kor = nyelvek[0]['year']
legfi_nyelv = nyelvek[0]
for nyelv in nyelvek:
    if nyelv['year'] > legfi_kor:
        legfi_kor = nyelv['year']
        legfi_nyelv = nyelv

print(f'A legfiatalabb nyelv adatai:\n kiadási év: {legfi_nyelv['year']}\n nyelv neve: {legfi_nyelv['programming language']}\n szerző keresztneve: {legfi_nyelv['first name']}\n szerző családneve: {legfi_nyelv['last name']}')

legid_kor = nyelvek[0]['year']
legid_nyelv = nyelvek[0]
for nyelv in nyelvek:
    if nyelv['year'] < legid_kor:
        legid_kor = nyelv['year']
        legid_nyelv = nyelv

print(f'A legidősebb nyelv adatai:\n kiadási év: {legid_nyelv['year']}\n nyelv neve: {legid_nyelv['programming language']}\n szerző keresztneve: {legid_nyelv['first name']}\n szerző családneve: {legid_nyelv['last name']}')