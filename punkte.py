#imports
import random
import time
import msvcrt

#Feste Werte
punkte = 0
level = 1
erfahrung = 0
levelvorraussetzung = 20
idioten_counter = 0
respawn_screen = 0
boss_fight = 0
game_over = 0
skalierungs_faktor = 5
boss_skalierung = 20
timer = 0

#Tasten
gültigeeingaben = ['w', 's', 'quit']
attacken = ["y", "x", "c", "v", "b", "n", "m"]
boss_attacken = ["f", "g", "h", "j", "k", "l", "r", "t", "z", "u", "i", "o", "p", "y", "x", "c", "v", "b", "n", "m"]
dodges = ["q", "e", "a", "d"]

#Farben
RESET = "\033[0m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"

def respawn_menu():
    global erfahrung, level, levelvorraussetzung, punkte, idioten_counter, respawn_screen, game_over
    respawn_screen = 1
    while respawn_screen == 1:
        print("Du hast verloren! Möchtest du noch mal spielen? [J/N]")
        neuer_versuch = input("Eingabe: ").strip().lower()
        if neuer_versuch == "j":
            erfahrung = 0
            level = 1
            levelvorraussetzung = 20
            punkte = 0
            idioten_counter = 0
            respawn_screen = 0
            print("Spiel startet neu!")
            pass
        elif neuer_versuch == "n":
            respawn_screen = 0
            game_over = 1
            exit
            break
        elif neuer_versuch == "nuh uh":
            print(YELLOW + "CHEAT CODE AKTIVIERT" + RESET)
            respawn_screen = 0
            pass
        else:
            print(YELLOW + "Bitte mit [J] für Ja oder [N] für Nein antworten" + RESET)
            time.sleep(1)

def level_up():
    global erfahrung, levelvorraussetzung, level
    if erfahrung >= levelvorraussetzung:
        level += 1
        erfahrung -= levelvorraussetzung
        levelvorraussetzung += 10
        print(YELLOW + f"Du bist auf Level {GREEN}{level}{YELLOW} gestiegen" + RESET)

#Einführung
print(f"Gehe weiter im Dungeon mit {GREEN}[W]{RESET} und geh zurück mit {RED}[S]{RESET}. Du startest auf Ebene {punkte}")

#Spiel-schleife
dungeon_tiefe_ziel = random.randint(5, 10)
dungeon_erfahrungspunkte = random.randint(10, 20)
boss_erfahrungspunkte = random.randint(20, 40)

while True:

    if game_over == 1:
        break

    #Zufallswerte
    encounter = random.randint(1, 10)
    hit = random.randint(1, 10)
    base_boss_health = random.randint(50, 100)
    boss_health = (base_boss_health + skalierungs_faktor * level)
    boss_event = random.randint(1, 3)
    counter = random.randint(1, 2)

    #"Movement"
    print(f"Eingabe: ", end="", flush=True)
    while True:
        if msvcrt.kbhit():
            eingabe = msvcrt.getch()
            if ord(eingabe) == 27:
                eingabe = "quit"
                print()
            else:
                eingabe = eingabe.decode('ASCII')
                eingabe = eingabe.lower()
                print(eingabe)
            break

    #Verlassen
    if eingabe == "quit":
        print("Spiel beendet.")
        time.sleep(2)
        break

    #Vorwärts gehen
    if eingabe == "w":
        punkte += 1
        print(f"Du gehst tiefer in den Dungeon auf Ebene {GREEN}{punkte}{RESET}")

    #Gegner
    if punkte != dungeon_tiefe_ziel:
        if eingabe in ["w", "s"]:  
            if encounter == 7:
                attacke = random.choice(attacken)
                print(YELLOW + f"Ein {RED}Gegner{YELLOW} ist erschienen!" + RESET)
                gegner_erfahrungspunkte = random.randint(5, 15)
                print(f"Greif an mit {RED}{attacke.upper()}{RESET} an: ", end="", flush=True)
                while True:
                    if msvcrt.kbhit():
                        angriff = msvcrt.getch().decode('ASCII')
                        print(angriff)
                        angriff = angriff.lower()
                        break
                if angriff == attacke:
                    print("Du hast den Gegner besiegt")
                    erfahrung += gegner_erfahrungspunkte
                    print(YELLOW + f"Du hast durchs Besiegen des Gegners {GREEN}{gegner_erfahrungspunkte}{YELLOW} EXP bekommen {RESET}[{erfahrung}|{levelvorraussetzung}]" + RESET)
                    level_up()
                else:
                    respawn_menu()

    #Boss
    if punkte == dungeon_tiefe_ziel:
        if boss_event == 3:
            print(RED + "Ein Boss ist erschienen!" + RESET)
            boss_fight = 1
            while boss_fight == 1:
                base_damage = random.randint(10, 20)
                damage = (base_damage + (skalierungs_faktor * level))
                crit_damage = ((base_damage * 1.5) + (skalierungs_faktor * level))
                critical = random.randint(1, 5)
                print(YELLOW + f"Der Boss hat {boss_health} HP" + RESET)
                boss_attacke = random.choice(boss_attacken)
                print(f"Greife denn Boss an mit {RED}{boss_attacke.upper()}{RESET}")
                print(f"Eingabe: ", end="", flush=True)
                while True:
                    if msvcrt.kbhit():
                        boss_input = msvcrt.getch().decode('ASCII')
                        print(boss_input)
                        boss_input = boss_input.lower()
                        break
                if boss_input == boss_attacke:
                    if critical == 3:
                        print(YELLOW + f"Die Attacke war effektiv! [{RED}-{crit_damage} HP{YELLOW}]" + RESET)
                        boss_health -= crit_damage
                    else:
                        print(f"Du hast den Boss getroffen! [{RED}-{damage} HP{RESET}]")
                        boss_health -= damage
                if boss_health > 0:
                    bo_do = []
                    for i in range(4):
                        bo_do.append(random.choice(dodges))

                    print(f"Der Boss greift jetzt an! Weich aus mit: [{RED}{bo_do[0].upper()}{RESET}], [{RED}{bo_do[1].upper()}{RESET}], [{RED}{bo_do[2].upper()}{RESET}], [{RED}{bo_do[3].upper()}{RESET}]")
                    print(f"Eingabe: ", end="", flush=True)
                    dodgeindex = 0
                    dodged = False
                    while True:
                        if msvcrt.kbhit():
                            userinput = msvcrt.getch().decode('ASCII')
                            print(userinput, end="", flush=True)
                            if userinput.lower() == bo_do[dodgeindex]:
                                if dodgeindex == 3:
                                    dodged = True
                                    break
                                dodgeindex += 1
                                continue
                            break
                    print()
                    if dodged:
                        print(GREEN + "Du bist erfolgreich ausgewichen" + RESET)
                        pass
                    else:
                        print(RED + "Du wurdest getroffen!" + RESET)
                        boss_fight = 0
                        respawn_menu()
                if boss_health <= 0:
                    erfahrung += boss_erfahrungspunkte
                    print(YELLOW + f"Du hast den Boss besiegt! Du hast {boss_erfahrungspunkte} EXP bekommen {RESET}[{erfahrung}|{levelvorraussetzung}]")
                    level_up()
                    boss_fight = 0  

    #Rückwärts gehen
    if eingabe == "s":
        if punkte < 1:
            punkte = 0
            print(YELLOW + "Du kannst nicht aus dem Dungeon" + RESET)
        else:
            punkte -= 1
            print(f"Du gehst zurück auf Ebene {RED}{punkte}{RESET}")

    #idioten Meldung
    if eingabe not in gültigeeingaben:
        if eingabe == "":
            pass
        else:
            idioten_counter += 1
            if idioten_counter >= 5:
                print(YELLOW + "Bist du blöd?" + RESET)
    else:
        idioten_counter = 0

    #"Ziel"
    if punkte >= dungeon_tiefe_ziel:
        punkte = 0
        erfahrung += dungeon_erfahrungspunkte
        print(YELLOW + f"Glückwunsch du hast den Dungeon geschafft! Du hast {GREEN}{dungeon_erfahrungspunkte}{YELLOW} EXP bekommen {RESET}[{erfahrung}|{levelvorraussetzung}]")
        level_up()
        dungeon_tiefe_ziel = random.randint(5, 10)
        dungeon_erfahrungspunkte = random.randint(10, 20)
        boss_erfahrungspunkte = random.randint(20, 40)
