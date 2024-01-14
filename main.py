import os, random
from map import Map

run = True
menu = True
play = False
key = False
fight = False
standing = True
structures = False

RESET = "\033[0m"
YELLOW = "\033[33m"
GREEN = "\033[32m"
BLUE = "\033[34m"
RED = "\033[31m"
WHITE = "\033[97m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"

stone_count = 0
wood_count = 0

stone_pickaxe = 0

HP = 50
HPMAX = HP
ATK = 3
gold = 10
pot = 1
elixr = 0
x = 0
y = 0
key = False

os.system("")

if __name__ == "__main__":
    map_w, map_h = 30, 15
    game_map = Map(map_w, map_h)

e_list = ["dronk"]

mobs = {
    "dronk": {
        "hp": 35,
        "at": 3,
        "go": 10
    }
}

def clear():
    os.system("cls")
    
def draw():
    print(RED + "Xx-----------------------------------xX")

def save():
    list = [
        name,
        str(HP),
        str(ATK),
        str(gold),
        str(pot),
        str(elixr),
        str(x),
        str(y),
        str(key),
        str(stone_count),
        str(stone_pickaxe),
        str(wood_count)
    ]

    file = open("load.txt", "w")
    for item in list:
        file.write(item + "\n")
    file.close()

def heal(amount):
    global HP
    if HP + amount < HPMAX:
        HP += amount
    else:
        HP = HPMAX
    print(RESET + name + "'s HP refilled to " + MAGENTA + str(HP) + RESET + "!")

def structures():
    global play, structures, pot, wood_count, stone_count
    randomint = random.randint(0,50)
    if randomint >= 20:
        print(GREEN + "CONGRATULATIONS YOU STUMBLED UPON A VILLAGE!")
        print(BLUE + "would you like to explore or not?")
        choice = input(MAGENTA + "(y/n)" + RESET)
        if choice == 'n':
            play = True
            structures = False
            print(RED)
        if choice == 'y':
            print(BLUE + "okay")
            e = input("would you take the offerings of these people? (y/n) ")
            if e == "y":
                pot += 2
                wood_count += 5
                stone_count += 4
            if e == "n":
                structures = False
                play = True

def battle():
    global fight, play, run, HP, pot, elixr, gold, hpmax, hp, HPMAX

    enemy = random.choice(e_list)
    hp = mobs[enemy]["hp"]
    hpmax = hp
    atk = mobs[enemy]["at"]
    g = mobs[enemy]["go"]

    while fight:
        clear()
        draw()
        print("Defeat the " + enemy + "!")
        draw()
        max_health = HPMAX
        current_health = HP
        max_enemy = hpmax
        current_enemy = hp

        # display
        bars = 20
        remaining_health_symbol = "█"
        lost_health_symbol = "_"

        # colors
        color_green = "\033[92m"
        color_yellow = "\33[33m"
        color_red = "\033[91m"
        color_blue = "\33[34m"
        color_default = "\033[0m"
        health_color = color_green

        remaining_health_bars = round(current_health / max_health * bars)
        lost_health_bars = bars - remaining_health_bars
        remaining_enemy_bars = round(current_enemy / max_enemy * bars)
        lost_enemy_bars = bars - remaining_enemy_bars

        # printing stats
        print(RESET, f"YOUR HP: {current_health} / {max_health}")
        print(f"|{health_color}{remaining_health_bars * remaining_health_symbol}"
            f"{lost_health_bars * lost_health_symbol}{color_default}|")
        print(RESET, f"ENEMY HP: {current_enemy} / {max_enemy}")
        print(f"|{color_blue}{remaining_enemy_bars * remaining_health_symbol}"
            f"{lost_enemy_bars * lost_health_symbol}{color_default}|")

        current_health = max(current_health, 0)
        current_enemy = max(current_enemy, 0)

        # health color update
        if current_health > 0.66 * max_health:
            health_color = color_green
        elif current_health > 0.33 * max_health:
            health_color = color_yellow
        else:
            health_color = color_red

        print(RESET , "POTIONS: " , MAGENTA + str(pot))
        print(RESET , "ELIXIR: " , MAGENTA + str(elixr))
        draw()
        print(RESET + "1 - ATTACK")
        if pot > 0:
            print("2 - USE POTION (30HP)")
        if elixr > 0:
            print("3 - USE ELIXIR (50HP)")
        draw()

        choice = input(MAGENTA + "[#] ")
        if choice == "1":
            current_enemy -= ATK
            hp -= ATK
            print(RESET + name + " dealt " + RED + str(ATK) + RESET + " damage to the " + enemy + ".")
            if hp > 0:
                current_health -= atk
                HP -= atk
                print(RESET + enemy + " dealt " + RED + str(atk) + RESET + " damage to " + name + ".")
            input("> ")

        elif choice == "2":
            if pot > 0:
                pot -= 1
                heal(30)
                HP -= atk
                print(RESET + enemy + " dealt " + RED + str(atk) + RESET + " damage to " + name + ".")
            else:
                print(RED + "No potions!")
            input("> ")

        elif choice == "3":
            if elix > 0:
                elix -= 1
                heal(50)
                HP -= atk
                print(RESET + enemy + " dealt " + RED + str(atk) + RESET + " damage to " + name + ".")
            else:
                print(RED + "No elixirs!")
            input("> ")

        if HP <= 0:
            print(RESET + enemy + RED + " defeated " + name + "...")
            draw()
            fight = False
            play = False
            run = False
            print(RED + "GAME OVER")
            input("> ")

        if hp <= 0:
            draw()
            print(RESET + name + " defeated the " + enemy + "!")
            draw()
            fight = False
            gold += g
            print(RESET + "You've found " + str(g) + " gold!")
            if random.randint(0, 100) < 30:
                pot += 1
                print(RESET + "You've found a potion!")
            input(MAGENTA + "press enter to quit")

while run:
    while menu:
        clear()
        print(BLUE + '''
    ____     __                __
   /  _/____/ /___ _____  ____/ /
   / // ___/ / __ `/ __ \/ __  / 
 _/ /(__  ) / /_/ / / / / /_/ /  
/___/____/_/\__,_/_/ /_/\__,_/''')

        print(RESET + '''
           OPTIONS

1 - new game
2 - load game
3 - save & quit
        
tips: if your game crashes as 
      soon as u enter option 2, you probably
      deleted your save file''')
        draw()
              
        choice = input(MAGENTA + "$- " + RESET)
    
        if choice == '1':
            name = input(MAGENTA + "What will be your name? " + RESET)
            menu = False
            play = True

        if choice == '2':
            f = open("load.txt", "r")
            load_list = f.readlines()
            if len(load_list) == 12:
                name = load_list[0][:-1]
                HP = int(load_list[1][:-1])
                ATK = int(load_list[2][:-1])
                gold = int(load_list[3][:-1])
                pot = int(load_list[4][:-1])
                elixr = int(load_list[5][:-1])
                x = int(load_list[6][:-1])
                y = int(load_list[7][:-1])
                key = bool(load_list[8][:-1])
                stone_pickaxe = int(load_list[9][:-1])
                stone_count = int(load_list[10][:-1])
                wood_count = int(load_list[11][:-1])
                clear()
                print(BLUE + "Welcome back, " + name + "!")
                input(MAGENTA + "> " + RESET)
                menu = False
                play = True
            else:
                print(RED + "Sorry, the save file may have been corrupted or moved")
                input(MAGENTA + "> ")

        if choice == '3':
            save()
            quit()

    while play:
        save()
        clear()
        if not standing:
            randomnum = random.randint(0, 100)
            if randomnum <= 30:
                fight = True
                battle()
            if randomnum <= 40:
                structures()
        print(RESET + "0 - quit to menu")
        draw(), RESET
        game_map.display_map()
        draw()
        print(RESET + "LOCATION (y,x): ", y, x)
        print(RESET + "NAME: ", name)
        # stats
        max_health = HPMAX
        current_health = HP

        # display
        bars = 20
        remaining_health_symbol = "█"
        lost_health_symbol = "_"

        # colors
        color_green = "\033[92m"
        color_yellow = "\33[33m"
        color_red = "\033[91m"
        color_blue = "\33[34m"
        color_default = "\033[0m"

        health_color = color_green


        # bar update
        remaining_health_bars = round(current_health / max_health * bars)
        lost_health_bars = bars - remaining_health_bars

        # printing stats
        print(f"HP: {current_health} / {max_health}")
        print(f"|{health_color}{remaining_health_bars * remaining_health_symbol}"
            f"{lost_health_bars * lost_health_symbol}{color_default}|")
        
        current_health = max(current_health, 0)

        # health color update
        if current_health > 0.66 * max_health:
            health_color = color_green
        elif current_health > 0.33 * max_health:
            health_color = color_yellow
        else:
            health_color = color_red

        print(RESET, "ATK:",RED, str(ATK))
        print(RESET, "GOLD:", YELLOW, str(gold))
        print(RESET, "POTIONS:", MAGENTA, str(pot))
        print(RESET, "ELIXIRS:", MAGENTA, str(elixr))
        draw()
        print(RESET + '''1 - north
2 - east
3 - south
4 - west            
m - go mining
w - get wood
e - see inventory
c - go to tools expert to craft tools''')
        draw()
        if pot > 0:
            print(RESET + "5 - USE POTION (30HP)")
        if elixr > 0:
            print(RESET + "6 - USE ELIXIR (50HP)")
        draw()

        dest = input(MAGENTA + "-> " + RESET)

        if dest == '0':
            clear()
            play = False
            menu = True

        elif dest == "1":
            if y > 0:
                y -= 1
                standing = False
            else:
                y = 0
        elif dest == "2":
            if x < map_w:
                x += 1
                standing = False
            else:
                x = 0
        elif dest == "3":
            if y < map_h:
                y += 1
                standing = False
            else:
                y = 0
        elif dest == "4":
            if x > 0:
                x -= 1
                standing = False
            else:
                x = 0
        elif dest == "5":
            if pot > 0:
                pot -= 1
                heal(30)
            else:
                print("No potions!")
            input(MAGENTA + "> ")
            standing = True
        elif dest == "6":
            if elixr > 0:
                elixr -= 1
                heal(50)
            else:
                print("No elixirs!")
            input(MAGENTA + "> ")
            standing = True
        elif dest == "m":
            clear()
            rock = random.randint(0,1)
            if rock == 1:
                print(BLUE + "u found stone!")
                stone_count += 1
                input()
        elif dest == "w":
            clear()
            print(BLUE + "u found a tree!")
            wood_count += 1
            input()
        elif dest == "c":
            clear()
            draw()
            print(RESET + '''
What do you want to craft?
                  
1 - stone pickaxe
            ''')
            draw()
            craft = input(MAGENTA + "(1) ")
            if ((wood_count >= 2) and (stone_count >= 3)):
                print(BLUE + "congratulatiosn you now have a stone pickaxe")
                stone_pickaxe += 1
                wood_count -= 2
                stone_count -= 3
                input()
        elif dest == "e":
            clear()
            draw()
            if stone_count > 0:
                print(RESET + "stone x" , stone_count)
            if wood_count > 0:
                print(RESET + "wood x" , wood_count)
            if stone_pickaxe > 0:
                print(RESET + "stone pickaxe x" , stone_pickaxe)
            draw()
            input()