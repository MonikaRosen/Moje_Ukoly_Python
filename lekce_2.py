# sales = {
#     "A": 4165,
#     "B": 5681,
#     "C": 2565,
# }

# print(sales['C'])

##prochazim klice:
# for book in sales:
#     print(book)

##prochazim hodnoty i klice
# for book in sales.items():
#     print(book)

## format tuple - neda se modifikovat oproti slovniku, je to nemenitelny seznam
# for key, value in sales.items():
#     print(f'Klic {key} -- {value}')

##dvojrozmerny slovniky - seznam slovniku

# from multiprocessing.sharedctypes import Value


# books = [
#     {"title": "Zkus mě chytit", "sold": 4165, "price": 347, "year": 2018},
#     {"title": "Vrah zavolá v deset", "sold": 5681, "price": 299, "year": 2019},
#     {"title": "Zločinný steh", "sold": 2565, "price": 369, "year": 2019},
# ]
# for book in books:
#     print(book)

##jen prodane knihy
# for book in books:
#     print(book['sold'])

## za kolik prodany
# for book in books:
#     profit = book['sold'] * book['price']
#     print(profit)


# for book in books:
#     print(book["year"] == 2019)

##funkce strip odebere znaky typu mezery, taby.. 

# 1 Vysvědčení (to dáš)
# Uvažujme vysvědčení, které máme zapsané jako slovník.

# Napiš program, který spočte průměrnou známku ze všech předmětů.
# Uprav program, aby vypsal všechny předměty, ve kterých získal student známku 1.

# school_report = {
#     "Český jazyk": 1,
#     "Anglický jazyk": 1,
#     "Matematika": 1,
#     "Přírodopis": 2,
#     "Dějepis": 1,
#     "Fyzika": 2,
#     "Hudební výchova": 4,
#     "Výtvarná výchova": 2,
#     "Tělesná výchova": 3,
#     "Chemie": 4,
# }
#dam soucet 0 jako default a ta fce soucet += pricita vzdy radek po radku znamky
# soucet = 0
# for znamka in school_report.values():
#     soucet += znamka
# prum_znamka = soucet/len(school_report)
# print(prum_znamka)

# Uprav program, aby vypsal všechny předměty, ve kterých získal student známku 1.
# for key, value in school_report.items():
#     if value == 1:
#         print(key)


# 2 Čtenářský deník (to dáš)
# Gustav je vášnivým čtenářem detektivek z našeho nakladatelství a navíc si zapisuje knihy, které přečetl.
# Níže ve slovníku vidíme, jaké informace si eviduje - název knihy, počet stran a hodnocení od 0 do 10.

# Napiš program, který spočte celkový počet stran, které Gustav přečetl.
# Připiš do programu výpočet počtu knih, kterým dal Gustav hodnocení alespoň 8.
#books = [
#     {"title": "Vražda s příliš mnoha notami", "pages": 450, "rating": 5},
    # {"title": "Vražda podle knihy", "pages": 524, "rating": 9},
    # {"title": "Past", "pages": 390, "rating": 4},
    # {"title": "Popel popelu", "pages": 411, "rating": 10},
    # {"title": "Noc, která mě zabila", "pages": 159, "rating": 7},
    # {"title": "Vražda, kouř a stíny", "pages": 258, "rating": 6},
    # {"title": "Zločinný steh", "pages": 542, "rating": 8},
#     {"title": "Zkus mě chytit", "pages": 247, "rating": 7},
#     {"title": "Vrah zavolá v deset", "pages": 396, "rating": 6},
# ]
# Napiš program, který spočte celkový počet stran, které Gustav přečetl.
# strany_celkem = 0
# for item in books:
#     strany_celkem += item['pages']
# print(strany_celkem)

# Připiš do programu výpočet počtu knih, kterým dal Gustav hodnocení alespoň 8.
# pocet = 0
# for item in books:
#     if item['rating'] >= 8:
#         pocet +=1
# print(pocet)


# # Bonusy
# # 3 Poznávací značky (zapni hlavu)
# # V následujícím slovníků je evidence automobilů.
# # Klíčem jsou státní poznávací značky (SPZ) a hodnotou je jméno majitele vozu.
# # Napiš program, který vypíše všechny majitele, jejichž vozidlo je registrováno v Plzeňském kraji,
# # tj. na druhém místě (index 1!) řetězce v klíči je písmeno P.

plates = {"4A2 3000": "František Novák",
    "6P5 4747": "Jana Pilná",
    "3B7 3652": "Jaroslav Sečkár",
    "1P5 5269": "Marta Nováková",
    "37E 1252": "Martina Matušková",
    "2A5 2241": "Jan Král"}

for key, value in plates.items():
    if key[1] == 'P':
        print(value)