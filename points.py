import random
import time
import sys
import os
import tty
import termios

# Platform-independent single-character input
def get_input():
    if os.name == 'nt':
        import msvcrt
        return msvcrt.getch().decode('utf-8').lower()
    else:
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch.lower()

# Constants
score = 0
level = 1
experience = 0
level_requirement = 20
invalid_input_count = 0
respawn_active = False
boss_battle_active = False
game_over = False
scaling_factor = 5
boss_scaling = 20

# Keys
valid_inputs = ['w', 's', 'quit']
attack_keys = list("yxcvbnm")
boss_attack_keys = list("fghjklrtzuiopyxcvbnm")
dodge_keys = list("qead")

# Colors
RESET = "\033[0m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"

def show_respawn_menu():
    global experience, level, level_requirement, score
    global invalid_input_count, respawn_active, game_over
    respawn_active = True
    while respawn_active:
        print("You died! Would you like to play again? [Y/N]")
        retry = input("Choice: ").strip().lower()
        if retry == "y":
            experience = 0
            level = 1
            level_requirement = 20
            score = 0
            invalid_input_count = 0
            respawn_active = False
            print("Restarting the game...")
        elif retry == "n":
            respawn_active = False
            game_over = True
            break
        elif retry == "nuh uh":
            print(YELLOW + "CHEAT CODE ENABLED" + RESET)
            respawn_active = False
        else:
            print(YELLOW + "Please respond with [Y] for yes or [N] for no." + RESET)
            time.sleep(1)

def level_up():
    global experience, level_requirement, level
    while experience >= level_requirement:
        level += 1
        experience -= level_requirement
        level_requirement += 10
        print(YELLOW + f"You leveled up to {GREEN}{level}{YELLOW}!" + RESET)

# Introduction
print(f"Move forward in the dungeon with {GREEN}[W]{RESET} and go back with {RED}[S]{RESET}. You start at floor {score}")

# Main Game Loop
dungeon_target_depth = random.randint(5, 10)
dungeon_exp_reward = random.randint(10, 20)
boss_exp_reward = random.randint(20, 40)

while not game_over:

    encounter_chance = random.randint(1, 10)
    hit_chance = random.randint(1, 10)
    base_boss_health = random.randint(50, 100)
    boss_health = base_boss_health + scaling_factor * level
    boss_event_chance = random.randint(1, 3)

    print("Input: ", end="", flush=True)
    user_input = get_input()
    print(user_input)

    if user_input == "quit":
        print("Game exited.")
        time.sleep(2)
        break

    if user_input == "w":
        score += 1
        print(f"You move deeper into the dungeon. Now at floor {GREEN}{score}{RESET}")

    if score != dungeon_target_depth and user_input in ["w", "s"]:
        if encounter_chance == 7:
            enemy_key = random.choice(attack_keys)
            print(YELLOW + f"An {RED}enemy{YELLOW} appeared!" + RESET)
            gained_exp = random.randint(5, 15)
            print(f"Attack using {RED}{enemy_key.upper()}{RESET}: ", end="", flush=True)
            attack_input = get_input()
            print(attack_input)

            if attack_input == enemy_key:
                print("You defeated the enemy!")
                experience += gained_exp
                print(YELLOW + f"Gained {GREEN}{gained_exp} EXP {YELLOW}[{experience}/{level_requirement}]" + RESET)
                level_up()
            else:
                show_respawn_menu()

    if score == dungeon_target_depth and boss_event_chance == 3:
        print(RED + "A Boss has appeared!" + RESET)
        boss_battle_active = True
        while boss_battle_active:
            base_damage = random.randint(10, 20)
            damage = base_damage + scaling_factor * level
            crit_damage = int((base_damage * 1.5) + (scaling_factor * level))
            critical_hit = random.randint(1, 5)

            print(YELLOW + f"Boss HP: {boss_health}" + RESET)
            boss_attack_key = random.choice(boss_attack_keys)
            print(f"Attack the boss with {RED}{boss_attack_key.upper()}{RESET}")
            print("Input: ", end="", flush=True)
            boss_input = get_input()
            print(boss_input)

            if boss_input == boss_attack_key:
                if critical_hit == 3:
                    print(YELLOW + f"Critical hit! {RED}-{crit_damage} HP{YELLOW}" + RESET)
                    boss_health -= crit_damage
                else:
                    print(f"Hit! {RED}-{damage} HP{RESET}")
                    boss_health -= damage

            if boss_health > 0:
                dodge_sequence = [random.choice(dodge_keys) for _ in range(4)]
                print("Boss is attacking! Dodge in order:")
                print(" ".join(f"[{RED}{k.upper()}{RESET}]" for k in dodge_sequence))

                dodge_index = 0
                dodged = False
                while True:
                    dodge_input = get_input()
                    print(dodge_input, end="", flush=True)
                    if dodge_input == dodge_sequence[dodge_index]:
                        if dodge_index == 3:
                            dodged = True
                            break
                        dodge_index += 1
                        continue
                    break
                print()
                if dodged:
                    print(GREEN + "You dodged successfully!" + RESET)
                else:
                    print(RED + "You were hit!" + RESET)
                    boss_battle_active = False
                    show_respawn_menu()

            if boss_health <= 0:
                experience += boss_exp_reward
                print(YELLOW + f"Boss defeated! Gained {boss_exp_reward} EXP [{experience}/{level_requirement}]" + RESET)
                level_up()
                boss_battle_active = False

    if user_input == "s":
        if score < 1:
            score = 0
            print(YELLOW + "You can't leave the dungeon!" + RESET)
        else:
            score -= 1
            print(f"You move back to floor {RED}{score}{RESET}")

    if user_input not in valid_inputs and user_input != "":
        invalid_input_count += 1
        if invalid_input_count >= 5:
            print(YELLOW + "Are you even trying?" + RESET)
    else:
        invalid_input_count = 0

    if score >= dungeon_target_depth:
        score = 0
        experience += dungeon_exp_reward
        print(YELLOW + f"Congratulations! You cleared the dungeon and gained {GREEN}{dungeon_exp_reward} EXP {YELLOW}[{experience}/{level_requirement}]" + RESET)
        level_up()
        dungeon_target_depth = random.randint(5, 10)
        dungeon_exp_reward = random.randint(10, 20)
        boss_exp_reward = random.randint(20, 40)
