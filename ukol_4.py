# Vymyšlené zadání
# Uvažuj že vytváříš kuchařku a potřebuješ uložit několik receptů. Vytvoř dvě třídy Recept a Kucharka (idealne v tomto poradi).

# 1. Recept
# Bude mít 3 atributy:

# nazev - string, jmeno kucharky
# narocnost - necham na vas jak ji budete reprezentovat (muze byt cislo, muze byt slovni vyjadreni)
# url_adresa - string, odkaz na recept
# vyzkouseno - bool, metoda __init__ ji vzdy nastavi na False
# nazev,narocnost, url_adresa budou atributy metody __init__, tedy uzivatel si je muze zvolit pri vytvareni objektu.

# A bude mít také 3 metody:

# __str___(self)
# vraci hezky vypis receptu (necham na vas ktere atributy chcete do vypisu dat)
# zmen_narocnost(self, nova_hodnota)
# zmeni narocnost, tedy zmeni atribut narocnost na nova_hodnota
# zkusit(self)
# zmeni atribut vyzkouseno na True

class Recipe:
    def __init__(self, name_recipe, difficulty, url_address):
        self.name_recipe = name_recipe
        self.difficulty = difficulty
        self.url_address = url_address
        self.tried = False
    
    def __str__(self):
        return(f'The recipe for {self.name_recipe} has difficulty {self.difficulty} and you can access it at {self.url_address}. The recipe was tried: {self.tried}.')
        
    def tried_change(self):
        self.tried = True
        return (f'The recipe for {self.name_recipe} has difficulty {self.difficulty} and you can access it at {self.url_address}. The recipe was tried: {self.tried}.')

    def change_difficulty(self, new_difficulty):
        self.difficulty = new_difficulty
        return(new_difficulty)


pancakes = Recipe('pancakes', 2, 'https://www.pankes.com')
muffin = Recipe('muffin', 3, 'https://www.muffin.com')
cake = Recipe('cake', 4, 'https://www.cake.com')

print(cake)
cake.change_difficulty(5)
print(cake)
print(str(pancakes.tried_change()))


# 2. Kucharka
# Bude mít 3 atributy:

# nazev - string, jmeno kucharky
# autor - string, jmeno autora kucharky
# recepty - list objektu tridy Recept, metoda __init__ ji nastavuje vzdy na prazdny seznam []
# nazev a autor budou atributy metody __init__, tedy uzivatel si je muze zvolit pri vytvareni objektu.

# A bude mít také 3 metody:

# __str___(self)
# vraci hezky vypis kucharky (necham na vas ktere atributy chcete do vypisu dat)
# pocet_receptu(self)
# vraci cislo reprezentujici pocet receptu v atributu recepty
# pridej_recept(self, recept)
# prida do atributu recepty objekt recepty ktery je v argumentu recept

class Cookbook:
    def __init__(self, name_cookbook, author):
        self.name_cookbook = name_cookbook
        self.author = author
        self.recipe = []
        self.list = []

    def __str__(self):
        return(f'Name of the cookbook is {self.name_cookbook} written by {self.author}.')
    
    def number_recipes(self):
        number_recipes = len(self.recipe)
        return(f'Number of recipes in the cookbook is {number_recipes}.')

    def add_recipe(self, new_recipe):
        self.recipe.append(new_recipe)
        return(f'New recipe {new_recipe} was added.')

# Bonus:
    def tried_recipes(self, list):
        self.list.append(list)
        if self.tried == True:
            return({self_list})

#-----

desserts = Cookbook('Desserts', 'Kate Newman')
sweets = Cookbook('Sweets', 'Linda Bush')

print(desserts)
desserts.add_recipe('tiramisu')
print(desserts.number_recipes())
print(desserts.recipe)


# Bonus:
# Pridej tride Kucharka metodu vyzkousene_recepty(self), ktera vrati seznam receptu ktere maji atribut vyzkouseno True.
# Priklady vypisu jsou ilustracni, muzete si je udelat jak chcete, pokud byste meli problem s tim ze se vam u printu celeho listu nevypisuji ve forme __str__ metody, 
# muzete pridat metou __repr__ (bude uplne totozna jako __str__ jen zmenite nazev),
# pripadne muzete zkusit list comprehension ktere vam vrati list retezcu (pro kazdy recept zavolate uvnitr list comprehension __str__ metodu).
