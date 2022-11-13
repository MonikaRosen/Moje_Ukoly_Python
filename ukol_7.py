# Vytvoř program na prodej vstupenek do letního kina. Ceny vstupenek jsou v tabulce níže.

# Datum	Cena
# 1. 7. 2021 - 10. 8. 2021	250 Kč
# 11. 8. 2021 - 31. 8. 2021	180 Kč
# Mimo tato data je středisko zavřené.

# Tvůj program se nejprve zeptá uživatele na datum a počet osob, pro které uživatel chce vstupenky koupit. Uživatel zadá datum ve středoevropském formátu. 
# Převeď řetězec zadaný uživatelem na datum pomocí funkce datetime.strptime().

# Pokud by uživatel zadal příjezd mimo otevírací dobu, vypiš, že letní kino je v té době uzavřené. Pokud je letní kino otevřené, spočítej a vypiš cenu za vstupenky.

# Data lze porovnávat pomocí známých operátorů <, >, <=, >=, ==, !=. Tyto operátory můžeš použít v podmínce if. Níže vidíš příklad porovnání dvou dat.
# Program vypíše text "Druhá událost se stala po první události".

from datetime import datetime
date = input('Please specify the date of your visit: ')
number_people = input('Please confirm number of visitors: ')

date_visit = datetime.strptime(date, '%d.%m.%Y')
start_date = datetime(2021, 7, 1)
second_date = datetime(2021, 8, 10)
end_date = datetime(2021, 8, 31)

if date_visit < start_date or date_visit > end_date:
    print('The cinema is closed.')
if date_visit >= start_date and date_visit <= second_date:
    price_1 = int(number_people) * 250
    print(f'Price of the tickets is: {price_1} Kc. ')
if date_visit >= second_date and date_visit <= end_date:
    price_2 = int(number_people) * 180
    print(f'Price of the tickets is: {price_2} Kc. ')

