__author__ = "rizkyhaksono"
__copyright__ = "Copyright 2023, Malang"

allheroes = [{"Hero": "Kagura", "Role": "Mage", "DMG": 350, "Gold": 1000},
             {"Hero": "Yve", "Role": "Mage", "DMG": 250, "Gold": 1000},
             {"Hero": "Lancelot", "Role": "Assassin", "DMG": 200, "Gold": 1000},
             {"Hero": "Hayabusa", "Role": "Assassin", "DMG": 300, "Gold": 1000},
             {"Hero": "Natalia", "Role": "Assassin", "DMG": 150, "Gold": 1000},
             {"Hero": "Cecilion", "Role": "Mage", "DMG": 200, "Gold": 1000}]


def chooseHero():
    print("Select 1 Hero you want to play: ")
    selectedhero = {}
    for i in range(len(allheroes)):
        print("Id : {}".format(i))
        print("Detail : {}".format(allheroes[i]))
    inputs = input("silahkan masukkan pilihan Id: ")
    try:
        selectedhero.update(allheroes[int(inputs)])
        return selectedhero
    except:
        return "Wrong Input!"


def start():
    print("Welcome to mini Mobile Legends Game\n\n")
    hero = chooseHero()
    print("\nYour hero is ", hero)
    # skenario game berhenti disini lanjutannya belum dibuat


# mari jalankan gamenya
start()
