# Otevřete si dokument s jedním výkazem známek.
# Zkopírujte si tuto tabulku do textového souboru - ulozte si ho to stejne slozky jako skript s resenim domaciho ukolu.
# Je jedno jak si ho pojmenujete, ten nazev pak budete pouzivat ve vasem programu
# Napište program, který tuto tabulku načte ze souboru (z toho ktery jste si vytvorily) a změní všechny známky tak, že 1 bude A, 2 bude B, 3 bude C, 4 bude D a 5 bude F.
# Existuje vic zpusobu reseni, zamyslete se jestli se vam treba nehodi nejaka datova struktura o ktere jsme se ucili, pripadne podminky (pro fajnsmekry se to resit i s Tridami)
# Vypište váš výsledek do nějakého souboru tak, aby se z něj dal zase zkopírovat do tabulky Google.
# Uz umite funkce - nezapominejte na to, pokud potrebujete neco udelat vickrat dejte ten kod do funkce kterou pak muzete znovu volat.

# Zaroven se nebojte si problem rozkouskovat na vic mensich, muzete mit kus kodu (funkci) ktery zapisuje do souboru, kus ktery meni znamky a kus ktery cte ze souboru.

with open('znamky.txt', 'r', encoding = 'utf-8') as vstup:
    znamky = vstup.readlines()

prvni_radek = znamky[0]
modifikovane_radky = [prvni_radek]

for radek in znamky[1:]:
    new_line = radek.replace('1','A').replace('2','B').replace('3','C').replace('4','D').replace('5','E')
    modifikovane_radky.append(new_line)

# print(modifikovane_radky)

for radek in modifikovane_radky:
    print(radek)

with open('grades.txt', 'w', encoding='utf-8') as file:
    for radek in modifikovane_radky:
        file.write(radek)

# BONUS
import csv

with open('list_grades.csv', 'r', encoding = 'utf-8') as csvfile:
    spamreader = csv.reader(csvfile)
    for row in spamreader:
        print(row)
    # print(spamreader)

# pokud chci videt nejen ten objekt, ale co je vevnitr, tak musim dat ten for cyklus a vypsat ty radky
