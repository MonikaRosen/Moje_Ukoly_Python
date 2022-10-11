# Jeden lístek do divadla "Pěst na oko" stojí 12 euro. Spočítejte měsíční příjem divadla ze vstupného přichází-li průměrně 174 návštěvníků na jedno představení a divadlo hraje 15 představení měsíčně.

# print(15 * 12 * 174)

# Divadlo se rozhodlo prodávat studentské vstupné ve výši 65% plného vstupného. Jak se změní měsíční příjem divadla pokud víme, že polovina návštěvníků jsou studenti?

# print (12 * 0.65)
# print((15 * (12 * 0.65) * 174 / 2) + (15 * 12 * 174 / 2))


# Vytvořte řetězec obsahující jméno divadla.
# print("Pest na oko.")

# Vytvořte řetězec obsahující jméno divadla tak, že sečtete dohromady jednotlivá slova toho jména.
# print("Pest" + " " + "na" + " " + "oko.")

# Zkuste vynásobit řetězec celým číslem. Jaký jste dostali výsledek?
# print("Pest na oko." * 2)

# Vytvořte řetězec který vypadá takto: '111111000000', ale místo šesti jedniček a šesti nul obsahuje 256 jedniček a 256 nul.
# print("1" * 256 + "0" * 256)

# Fíha banka a.s. nabízí na svých stránkách spořící účet s úrokem 2,4 %. Když si na takový účet uložíte 1 000 000 kč, kolik peněz nastřádáte za 10 let?
# print(1000000 + (1000000 * 0.024 * 10))

# Do malého sálu v divadle, který má tvar čtverce o rozloze 30 m^2 potřebujeme koupit nový koberec. Jakou délku má mít strana koberce? Vejde se nám srolovaný do dodávky s nákladovým prostorem dlouhým 5 m?
# print(30**(1/2))

# Takzvané Shannonovo číslo má hodnotu 10^120 a udává kolik nejméně lze odehrát různých šachových partií. Vytvořte řetězec, který obsahuje toto číslo zapsané běžným způsobem pomocí cifer. Například 10^3 je 1000, 10^6 je 1000000 atd.
shann = (10**120)
# Čísla s mnoha nulami je v Česku zvykem zapisovat tak, že každé tři nuly následuje mezera. Jeden milión se tedy zapíše jako 1 000 000. Vytvořte řetězec, který obsahuje Shannonovo číslo z předchozího cvičení zapsané v tomto formátu.
print(shann)
