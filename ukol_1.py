baliky = {
    "B541X": True,
    "B547X": False,
    "B251X": False,
    "B501X": True,
    "B947X": False,
}
kod_baliku = input('Zadej cislo baliku: ')
cislo = baliky[kod_baliku]
if cislo == True:
    print('Balík byl předán kurýrovi.')
else:
    print('Balík ještě nebyl předán kurýrovi.')


# kod_baliku = input('Zadej cislo baliku: ')
# if kod_baliku in baliky:
# cislo = baliky[kod_baliku]
#   if cislo == True:
#      print('Balík byl předán kurýrovi.')
#   else:
#       print('Balík ještě nebyl předán kurýrovi.')
# else:
#      print('Cislo neexistuje')
