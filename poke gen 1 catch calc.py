import aiopoke
import asyncio
from math import ceil





async def main() -> None:
    async with aiopoke.AiopokeClient() as client:
        species = await client.get_pokemon_species(catchRate.lower())
        if species.generation.name == "generation-i":
            return species.capture_rate
        else:
            raise ValueError
        await client.close()

while True:


    catchRate = -1
    version = ""
    statusAilment = ""
    ballMod = 0
    Ball = 0
    hpRatio = -1
    loop = 0
    a = 0
    pb = 0
    gb = 0
    ub = 0
    reset = 0


    print("""This is a catch rate calculator for Generation I Pokémon games.
It falls short of 100% accuracy by simulating pure randomness rather than the original games' psudorandom number generator. Its calculations of HP uses decimal ratios and doesn't round, as well.
For additional details and a more accurate Generation I catch rate calculator, please visit this website:
https://www.dragonflycave.com/mechanics/gen-i-capturing\n""")
    while catchRate not in range(3, 256):
        version = ""
        if loop > 0:
            print("Try again.")
        catchRate = input("Type the wild Pokémon's name you wish to catch or enter a catch rate (0-255) you wish to calculate:\n")
        try:
            catchRate = int(catchRate)
        except ValueError:
            if catchRate.lower() == "dragonair" or catchRate.lower() == "dragonite":
                version = input("If you are playing on Pokémon Yellow Version, press \"Y\". If you wish to reset, type \"RESET\". Otherwise, continue.\n")
                if "reset" in version.lower():
                    reset = 1
                elif 'y' in version.lower() and catchRate.lower() == "dragonair":
                    catchRate = 27
                elif 'y' in version.lower() and catchRate.lower() == "dragonite":
                    catchRate = 9
            if 'y' not in  version.lower() and catchRate.lower() != "raticate":
                try:
                    catchRate = asyncio.run(main())
                except:
                    pass
            try:
                if catchRate.lower() == "raticate":
                    catchRate = 90
            except:
                pass
        finally:
            loop = 1
            pass

    loop = 0


    if reset != 1:
        statusAilment = input("If the wild Pokémon is asleep or frozen, press \"S\". If the wild Pokémon is paralyzed, poisoned, or burned, press \"P\". If you wish to reset, type \"RESET\". Otherwise, continue.\n")
    while "reset" not in statusAilment.lower() and ('s' in statusAilment.lower() or 'f' in statusAilment.lower()) and ('p' in statusAilment.lower() or 'b' in statusAilment.lower()):
        statusAilment = input("Try again.\nIf the wild Pokémon is asleep or frozen, press \"S\" or \"F\". If the wild Pokémon is paralyzed, poisoned, or burned, press \"P\" or \"B\". Otherwise, continue.\n")
    if "reset" in statusAilment.lower():
        reset = 1
    if 's' in statusAilment or 'f' in statusAilment.lower():
        statusAilment = 25
    elif 'p' in statusAilment or 'b' in statusAilment.lower():
        statusAilment = 12
    else:
        statusAilment = 0


    while (ceil(hpRatio) not in range(0, 101) or float(hpRatio) == 0) and reset != 1:
        if loop == 1:
            print("Try again.")
        loop = 0
        hpRatio = input("What's the approximate ratio of the opposing wild Pokémon's remaining HP to their maxixmum HP in percentage points? For instance, 100% or 50%. If you wish to reset, type \"RESET\".\n")
        if "reset" not in hpRatio.lower():
            for i in list(hpRatio):
                if loop == 0:
                    hpRatio = ""
                try:
                    hpRatio += str(int(i))
                except ValueError:
                    pass
                finally:
                    if i == '.' and '.' not in hpRatio:
                        hpRatio += i
                    elif i == '.' or i == '-':
                        hpRatio = 0
                        break
                    loop = 1
        else:
            reset = 1
        try:
            hpRatio = float(hpRatio)
        except:
            hpRatio = 0
        loop = 1
    
    if reset != 1:
        hpRatio = hpRatio / 100


    if reset != 1:
        try:
            if catchRate + statusAilment + 1 > 256:
                if hpRatio > 1 / 3:
                    print(f"\nCatch chance with a Poké Ball: {100 * ((statusAilment / 256) + (((85 / (256 * hpRatio)) + (1 / 256)) * ((256 - statusAilment) / 256)))}%")
                else:
                    print(f"\nCatch chance with a Poké Ball: 100% (guaranteed)")
            else:
                if hpRatio > 1 / 3:
                    print(f"\nCatch chance with a Poké Ball: {100 * ((statusAilment / 256) + (((85 / (256 * hpRatio)) + (1 / 256)) * ((catchRate + 1) / 256)))}%")
                else:
                    print(f"\nCatch chance with a Poké Ball: {100 * ((statusAilment + catchRate + 1) / 256)}%")
            if catchRate + statusAilment + 1 > 201:
                if hpRatio > 1 / 2:
                    print(f"Catch chance with a Great Ball: {100 * ((statusAilment / 201) + (((255 / (512 * hpRatio)) + (1 / 256)) * ((201 - statusAilment) / 201)))}%")
                else:
                    print(f"Catch chance with a Great Ball: 100% (guaranteed)")
            else:
                if hpRatio > 1 / 2:
                    print(f"Catch chance with a Great Ball: {100 * ((statusAilment / 201) + (((255 / (512 * hpRatio)) + (1 / 256)) * ((catchRate + 1) / 201)))}%")
                else:
                    print(f"Catch chance with a Great Ball: {100 * ((statusAilment + catchRate + 1) / 201)}%")
            if catchRate + statusAilment + 1 > 151:
                if hpRatio > 1 / 3:
                    print(f"Catch chance with an Ultra Ball or Safari Ball: {100 * ((statusAilment / 151) + (((85 / (256 * hpRatio)) + (1 / 256)) * ((151 - statusAilment) / 151)))}%")
                else:
                    print(f"Catch chance with an Ultra Ball or Safari Ball: 100% (guaranteed)")
            else:
                if hpRatio > 1 / 3:
                    print(f"Catch chance with an Ultra Ball or Safari Ball: {100 * ((statusAilment / 151) + (((85 / (256 * hpRatio)) + (1 / 256)) * ((catchRate + 1) / 151)))}%")
                else:
                    print(f"Catch chance with an Ultra Ball or Safari Ball: {100 * ((statusAilment + catchRate + 1) / 151)}%")
            print("Catch chance with a Master Ball: 100% (guaranteed)")
        except:
            input("Oops, there was an error. Please try again or contact the developer.")
            pass
        finally:
            input("Continue to run the program again from the beginning.\n")

    #print(f"status ailment: {statusAilment}\ncatch rate: {catchRate}\nhp ratio: {hpRatio}")
