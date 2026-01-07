autok = []
with open('adatok/autok_listaja.csv', 'r', encoding='utf-8') as forrasfajl:
    for sor in forrasfajl:
        adatok = sor.strip().split(',')
        auto = {'rendszam': adatok[0], 'tipus': adatok[1], 'kor': int(adatok[2])}
        autok.append(auto)

for auto in autok:
    print (f'{auto['rendszam']} - {auto['tipus']} - {auto['kor']}')

legid_kor = autok[0]['kor']
legid_auto = autok[0]
for auto in autok:
    if legid_kor < auto['kor']:
        legid_kor = auto['kor']
        legid_auto = auto

print(f'A legfiatalabb autó életkora: {legid_kor}')
print(f'A legfiatalabb autó adatai:\n {legid_auto['rendszam']} - {legid_auto['tipus']} - {legid_auto['kor']}')

legif_kor = autok[0]['kor']
legif_auto = autok[0]
for auto in autok:
    if legif_kor > auto['kor']:
        legif_kor = auto['kor']
        legif_auto = auto

print(f'A legfiatalabb autó életkora: {legif_kor}')
print(f'A legfiatalabb autó adatai:\n {legif_auto['rendszam']} - {legif_auto['tipus']} - {legif_auto['kor']}')