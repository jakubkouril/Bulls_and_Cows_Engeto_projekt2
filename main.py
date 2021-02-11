import random

oddelovac = '=' * 100

def uvitani():
    print(oddelovac)
    print('Vítáme Vás u hry Bulls and Cows. Cílem je uhodnout počítačem náhodně\n'
            'vygenerované čtyřmístné číslo, kde každá číslice je jiná. Pokud správně\n'
            'uhodnete číslo i jeho umístění, získáváte "Bull". Jestliže správně \n'
            'uhodnete číslo, nikoliv jeho umístění, získáváte "Cow". Hra končí, pokud\n'
            'trefíte všechny čtyři čísla, včetně jejich umístění, to je získání 4x"Bull".\n'
            'Pojďme do toho!')
    print()
    print(oddelovac)
    return()


nahodne_cislo = []

def pocitac_cislo():
    # Necháme počítač vygenerovat náhodné číslo
    while len(nahodne_cislo) != 4:
        nahodne_cislo.append(random.randrange(0, 10))
        if len(nahodne_cislo) == 4 and len(set(nahodne_cislo)) < 4:
            nahodne_cislo.clear()

    return()


pokusy = 0
zbyvajici_pokusy = 20
bulls = 0
cows = 0


def hra():
    global pokusy, zbyvajici_pokusy, bulls, cows

    # Pravidlo pokračování/ukončení hry
    while bulls != 4 and zbyvajici_pokusy > 0:

        # Necháme uživatele zadat jeho tip
        zadano_uzivatelem = input('Zadejte Váš tip (čtyřmístné číslo): ')
        tip_uzivatele = [int(num) for num in str(zadano_uzivatelem)]
        pokusy += 1
        zbyvajici_pokusy -= 1


        if len(tip_uzivatele) != 4:
            print('Je třeba zadat čtyřmístné číslo! Zbytečně jsi vyčerpal/a jeden pokus. ')
            print(oddelovac)
            continue


        for index, value in enumerate(tip_uzivatele):
            for pozice, hodnota in enumerate(nahodne_cislo):
                if index == pozice and value == hodnota:
                    bulls += 1

                elif index != pozice and value == hodnota:
                    cows += 1

        print(f'Bulls: {bulls}')
        print(f'Cows: {cows}')
        print(f'Zbývající pokusy: {zbyvajici_pokusy}')
        print(oddelovac)


        if zbyvajici_pokusy == 0:
            print('Konec hry! Bohužel, nevyšlo to. Zkus to znovu!')

        elif bulls != 4:
            bulls = 0
            cows = 0

        else:
            bulls = 4
            cows = 0

            if pokusy < 11:
                print(f'Vyhrál jsi! Skvělá práce! Celkový počet pokusů: {pokusy}')
            elif pokusy >= 11 and pokusy < 20:
                print(f'Vyhrál jsi, ale mohlo to být lepší. Celkový počet pokusů: {pokusy}')


uvitani()
pocitac_cislo()
hra()

