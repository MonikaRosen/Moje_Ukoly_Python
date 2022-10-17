# Uvažuj, že píšeš jednoduchou aplikaci pro zasílání SMS zpráv. Napiš program, který provede následující činnosti:

# Zeptá se uživatele na číslo, kam chce zprávu zaslat a ověří, že číslo má správný formát.
# Zeptá se uživatele na zprávu, kterou chce zaslat. Následně vypíše, kolik zpráva bude stát.
# Tvůj program bude obsahovat dvě funkce:

# První funkce ověří délku telefonního čísla. Uvažuj, že telefonní číslo může být devítimístné 
# nebo třináctimístné (pokud je na začátku předvolba "+420"). Nemusíte kontrolovat, zda uživatel 
# zadal skutečně číslo, či zda jsou tam i jiné znaky. To jsme v kurzu zatím neřešili. Pokud je číslo platné,
# funkce vrátí hodnotu True, jinak vrátí hodnotu False.
# Druhá funkce spočte cenu zprávy. Uživatel platí 3 Kč za každých započatých 180 znaků.
# Tvůj program nejprve ověří pomocí první funkce správnost telefonního čísla. Pokud není platné,
# vypíše chybu, v opačném případě se zeptá na text zprávy a pomocí druhé funkce určí její cenu, kterou vypíše uživateli.

# Nápověda
# Pokud chcete zkontrolovat předvolbu, stačí využít podmínku+420 in cislo, alternativně můžete využít indexy:
# Python umožňuje kromě jednoho znaku z řetězce získat i více znaků, a to pomocí dvojtečky. Pokud budete chtít získat 
# první čtyři znaky, napište cislo[0:4]. Pak můžete vytvořit podmínku cislo[0:4] == "+420".

from itertools import count
from operator import truediv


def check_number(phone_number):
    number = str(phone_number)
    lenght = len(number)
    if lenght == 9 or lenght == 13:
        return True
    else: 
        return False

# print(check_number(607544203))

def price_message(message):
    lenght_message = len(message)
    number_messages = (int(lenght_message) // 180)
    if ((int(lenght_message)) % 180) > 0:
        count = number_messages + 1
    else:
        count = number_messages
    price = count * 3
    return (price)

phone_number = input("Input your phone number: ")
ret_value = check_number(phone_number)
print(ret_value) 
if ret_value:
    message = input('Write your message: ')
    cena = price_message(message)
    print(f'Price of your message is {cena} Kc.')
else:
    print('Wrong number.')





