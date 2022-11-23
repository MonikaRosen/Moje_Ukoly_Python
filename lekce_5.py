# opakovani tridy
# class Zamestnanec: 
#     def __init__(self, jmeno: str, pozice: str):
#         self.jmeno = jmeno
#         self.pozice = pozice
#         self.pocet_dni_dovolene = 25

#     def __str__(self):
#         print(self.jmeno)
#         return f'{self.jmeno} pracuje na pozici {self.pozice}'

#     def cerpani_dovolene(self, pocet_dni):
#         if pocet_dni <= self.pocet_dni_dovolene:
#             self.pocet_dni_dovolene -= pocet_dni
#             return f'Zbyva dovolene: {self.pocet_dni_dovolene}'
#         else:
#             return f'Nemas dostatek dovolene: {self.pocet_dni_dovolene}'
#     # bud dam prazdny return nebo vynecham to else (kdyz nechci nic)
# frantisek = Zamestnanec('Frantisek', 'Programator')

# print(frantisek)

# print(frantisek.cerpani_dovolene(5))
# print(frantisek.cerpani_dovolene(15))
# print(frantisek.cerpani_dovolene(10))

# DEDICNOST - trida dedi vlastnosti a metody z jiny tridy, takze manazer bude zamestnanec taky, jen ma neco navic.. takze podrazena a nadrazena trida,
#  takze to ze ktere dedim dam do zavorek viz dole u manazera
# fce super dole odkazuje na tu nadrazenou tridu, ze ktere dedim
class Zamestnanec: 
    def __init__(self, jmeno: str, pozice: str):
        self.jmeno = jmeno
        self.pozice = pozice
        self.pocet_dni_dovolene = 25

    def __str__(self):
        # print(self.jmeno)
        return f'{self.jmeno} pracuje na pozici {self.pozice}'

    def cerpani_dovolene(self, pocet_dni):
        if pocet_dni <= self.pocet_dni_dovolene:
            self.pocet_dni_dovolene -= pocet_dni
            return f'Zbyva dovolene: {self.pocet_dni_dovolene}'
        else:
            return f'Nemas dostatek dovolene: {self.pocet_dni_dovolene}'

class Manazer(Zamestnanec):
    def __init__(self, jmeno, pocet_podrizenych):
        super().__init__(jmeno, 'Manazer')
        self.pocet_dni_dovolene = 30
        self.pocet_podrizenych = pocet_podrizenych
    
    def __str__(self):
        return f'{super().__str__()} a ma {self.pocet_podrizenych} podrizenych'

martin = Manazer('Martin', 10)
print(martin.cerpani_dovolene(10))
print(martin)


# List comprehenshion?
# rychle se vztvari seznam

pisemky = [0, 2, 0, 1, 1, 3]

# klasika for cykle
pisemky_1 = []
for znamka in pisemky:
    pisemky_1.append(znamka+1)

print(pisemky_1)

# pouziti list comprehension

print([znamka+1 for znamka in pisemky])

print([znamka*2 for znamka in pisemky])

pisemky = [0, 2, 0, 1, 1, 3]

# klasika for cykle a ted s podminkou
pisemky_1 = []
for znamka in pisemky:
    nova_znamka = znamka
    if znamka == 0:
        nova_znamka += 1
    pisemky_1.append(znamka+1)

print(pisemky_1)

# pouziti list comprehension a da se tam dat jen if a and, or 

print([znamka+1 if znamka == 0 else znamka for znamka in pisemky])

jmena = ['Roman', 'Jan', 'Miroslav', 'Petr', 'Gabriel']

jmena_velka = [jmena.lower() for jmena in jmena]
print(jmena_velka)

teploty = [
    [2.1, 5.2, 6.1, -0.1],
    [2.2, 4.8, 5.6, -1.0],
    [3.3, 6.5, 5.9, 1.2],
    [2.9, 5.6, 6.0, 0.0],
    [2.0, 4.6, 5.5, -1.2],
    [1.0, 3.2, 2.1, -2.0],
    [0.4, 2.7, 1.3, -2.8]
]

soucty = [sum(teploty) for teploty in teploty]
print(soucty)
