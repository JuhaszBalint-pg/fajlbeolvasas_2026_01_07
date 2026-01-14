with open ('gyumolcsok.txt', 'r', encoding='UTF-8') as forrasfajl, \
     open ('./adatok/gyumolcsok_masolat.txt', 'w', encoding='UTF-8') as celfajl:
        celfajl.write(forrasfajl.read())