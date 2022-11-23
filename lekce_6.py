# with open('mereni.txt', 'r', encoding='utf-8') as file:
#     radky = file.readlines()

# print(radky)

# radky_bez_newline = []
# for radek in radky:
#     radky_bez_newline.append(radek.replace('\n', ''))

# radky_bez_newline = [radek.rstrip() for radek in radky]

# 1 Výplata přesněji (to dáš)
# Zatím jsme výplatu počítali za předpokladu, že každý měsíc odpracujeme stejný počet hodin, což není příliš realistické.
# Vytvořte proto textový soubor vykaz.txt, který bude obsahovat 12 řádků a na každém řádku počet odpracovaných hodin za každý měsíc za poslední rok.

# Otevřete tento soubor ve svém programu a načtěte hodnoty na řádcích do seznamu vykaz.
# Vytiskněte tento seznam na konzoli funkcí print() abyste si ověřili, že jste soubor načetli správně.
# Nechte uživatele zadat na příkazovém řádku hodinovou mzdu.
# Spočítejte a na výstup vytiskněte celkovou výplatu za celý rok a průměrnou výplatu na jeden měsíc.

with open('vykaz.txt') as vstup:
    vykaz = vstup.readlines()

# preved na int
vykaz = [int(hodiny) for hodiny in vykaz]

print(vykaz)

mzda = float(input('Zadejte hodinovou mzdu:'))
vyplata_rok = sum(vykaz)*mzda
print(vyplata_rok)

# TODO

# 2 Počet slov (zapni hlavu)
# Stáhněte si odevzdanou slohovou práci.
# Zadání bylo sepsat text o nejméně 150ti slovech pojednávající o našem hlavním městě.
# Napište program, který spočítá počet slov v tomto textu, abychom věděli, zda bylo zadání formálně splněno.

# Nechte se vést následujícím návodem.

# Nechte váš program otevřít soubor a načíst jednotlivé řádky do seznamu.
# Každý řádek převeďte na seznam slov. Slovem se rozumí vše, co je odděleno mezerou nebo novým řádkem.
# Vypište na výstup seznam hodnot udávající počty slov na každém řádku.
# Vypište na výstup celkový počet všech slov v souboru.

# TODO

# Bonus

# 3 Půjčovna (zavařovačka)

# Půjčovna aut má v každém kraji ČR jedno auto s danou SPZ.
# Ke konci roku chce zjistit, kolik všechna auta najezdila dohromady kilometrů.
# V souboru auta.txt je pro každou SPZ zaznamenáno kolik dané auto ujelo kilometrů za daný rok.
# Hodnoty jsou v tisících kilometrů. Bohužel se v jednotlivých krajích blbě zkoordinovali a někdo používal desetinnou čárku, někdo zase tečku.

# V souboru s daty je ještě jeden problém, který není na první pohled vidět.
# Dá se vyřešit pomocí list comprehension s podmínkou uvedeném v předchozím čtení na doma.

# Napište program, který na výstup vypíše součet všech ujetých kilometrů. Jistě se vám bude hodit metoda řetězců jménem replace().

# NEDELALI JSME - https://kodim.cz/kurzy/python-data/zaklady-programovani/prvni-programy/moduly
# Upravte váš program tak, aby jméno souboru k otevření dostal na příkazové řádce,
# abychom mohli takto zpracovávat výkazy z různých souborů, aniž bychom museli upravovat samotný kód programu.

with open('data/auta.txt', encoding='utf-8') as soubor:
    radky = soubor.readlines()

modifikovane_radky = []
for radek in radky:
    if radek.strip() != '': # pokud radek obsahuje alespon jeden 'nebily' znak
        hodnoty = radek.split(' ')
        # spz, km = radek.split(' )
        spz = hodnoty[0]
        km = float(hodnoty[1].replace(',', '.'))
        modifikovane_radky.append([spz,km])

jen_km = [radek[1] for radek in modifikovane_radky]

km_celkem = sum(jen_km)
print(km_celkem)


# osklivy one liner pomoci list comprehension
print(f"{sum([float(radek.split()[1].replace(',','.')) for radek in radky if radek.strip() != ''])} tisic kilometru")



# tvoreni filu, zapis do filu

jmena = ['Roman', 'Jana', 'Radek', 'Petra', 'Vlasta']
# jmena_radky = [jmeno + '\n' for jmeno in jmena]

with open('uzivatele.txt', 'w', encoding='utf-8') as file:

    # jmena_radky = []
    # for jmeno in jmena:
    #     jmena_radky.append(jmeno + '\n')

    for jmeno in jmena:
        file.write(jmeno = ' :)')

# 1 Rozepsaná výplata (to dáš)
# Modifikujte program pro počítání výplaty z předchozí sekce tak,
# aby nevypisoval průměrnou výplatu za rok, nýbrž aby vypsal konkrétní vyplacenou částku pro každý měsíc zvlášť.

# Nejprve tyto informace vypište na výstup pomocí funkce print().
# Poté program upravte tak, aby vypsal tyto výsledky do souboru.

with open('vykaz.txt') as vstup:
    vykaz = vstup.readlines()

# preved na int
vykaz = [int(hodiny) for hodiny in vykaz]

print(vykaz)

mzda = float(input('Zadejte hodinovou mzdu:'))
vyplata_rok = sum(vykaz)*mzda
print(vyplata_rok)

with open('vyplata.txt', 'w', encoding='uft-8') as textfile:
    for hodiny in vykaz:
        print(f'vyplata je')
        textfile.write(str(hodiny*mzda) + '/n')
# TODO

# 2 Hody kostkou (zapni hlavu)
# Napište program, který vytvoří seznam deseti náhodných hodů dvanáctistěnnou kostkou.

# Nejdříve tento seznam vytiskněte na konzoli pomocí funkce print().
# Upravte váš program tak, aby náhodné hody kostkou vypsal do souboru s názvem hody.txt na jeden řádek oddělené čárkou a mezerou.
# Upravte váš program tak, aby počet hodů dostal jako parametr na příkazové řádce. Zkuste použitím vašeho programu vyrobit 100, 1000 a 10 000 hodů.

# TODO

# Bonus

# 3 Dny v měsíci (zavařovačka)
# Napište program, který bude mít přímo v kódu zapsaný počet dní v jednotlivých měsících takto:

pocty_dni = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# Nechte váš program vypsat tento seznam do souboru s názvem kalendar.txt, každé číslo na jeden řádek.
# Upravte váš program tak, aby zároveň s počtem dnů vypisoval i název měsíce. Oddělte v souboru název měsíce a počet dnů pomocí tabulátoru.
# Upravte váš program tak, aby jako první řádek výsledného souboru obsahoval nadpisy pro jednotlivé sloupce, tedy měsíc a počet dní.

# TODO
