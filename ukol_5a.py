class Nemoc:
    # poradi argumentu v radku nize si klidne preskladejte
    def __init__(self, jmeno, inkubacni_doba, pocet_obeti, sireni):
        self.jmeno = jmeno
        self.inkubacni_doba = inkubacni_doba
        self.pocet_obeti = pocet_obeti
        self.sireni = sireni

    def __str__(self):
        return f'Jmeno: {self.jmeno}'

    def zmen_pocet_obeti(self, pocet_obeti):
        self.pocet_obeti = pocet_obeti

# Vytvor tridu Koronavirus kera dedi ze tridy Nemoc a to nasledujicim zpusobem:

# Ze tridy Nemoc dedi beze zmeny chovani:

# Atribut jmeno
# Metodu zmen_pocet_obeti
# Navic pridava jeste:

# atribut varianty
# prazdny list v __init__ metode tridy Koronavirus
# metodu pridej_variantu(self, varianta)
# do atributu varianty prida novou variantu - varianty muzete specifikovat pomoci retezcu, pripadne i klidne vlastni tridou
# Upravuje metodu tridy Nemoc:

# __str__ uprav tak aby zobrazovala obsah atributu jmeno a varianty
# v retezci budou varianty oddelene carkami tedy napriklad z listu ['omikron', 'delta'] se stane retezec 'omikron, delta' - pouzijte metodu join podle nasledujicicho prikladu:
# Hodnoty atributu inkubacni_doba, pocet_obeti a sireni budou v __init__ metode tridy Koronavirus predane __init__ metode materske tridy (pres super().__init__(...)).

class Coronavirus(Nemoc):
    def __init__(self, jmeno, inkubacni_doba, pocet_obeti, sireni):
        super().__init__(jmeno, inkubacni_doba, pocet_obeti, sireni)
        self.varianty = []
    
    def pridej_variantu(self, nova_varianta):
        self.varianty.append(nova_varianta)
        return (f'Nova varianta coronaviru je {nova_varianta}.')

    def __str__(self):
        return (f'Jmeno: {self.jmeno}, varianty: {", ".join(self.varianty)}.')

covid = Coronavirus('covid', 6, 30000, 'kapenkami')

covid.pridej_variantu('omikron')
covid.pridej_variantu('delta')
covid.pridej_variantu('alpha')
print(covid)






