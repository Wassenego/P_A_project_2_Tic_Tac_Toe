"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie - Tic Tac Toe
author: Marek Sýkora
email: MarekSykora78@marks.cz
discord: Wassenego#1875
"""

import random

separator = "=" * 67

# seznam pozic v mřížce k zapisování volených vstupů podle hráčů 
positions = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

# seznam použitý k očíslování polí mřížky - nápověda pro hráče 
grid_marking = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# seznam indexů výherních kombinací
winning_combinations = [[0, 1, 2], [0, 3, 6], [0, 4, 8], [3, 4, 5], [6, 7, 8], [1, 4, 7], [2, 4, 6], [2, 5, 8]]

def print_grid(positions: list) -> str:
    """
    Popis:
    - vykreslí mřížku včetně hodnot podle zadaného seznamu.
    Parametry:
    - positions (list): seznam pozic v mřížce. 
    Návratová hodnota:
    - string : proměnná, jehož hodnota je řetězec, který vytiskne mřížku 
    """
    line = "+---+---+---+"
    grid = f"""\
{line} 
| {positions[0]} | {positions[1]} | {positions[2]} |
{line}
| {positions[3]} | {positions[4]} | {positions[5]} |
{line}
| {positions[6]} | {positions[7]} | {positions[8]} |
{line}\
"""
    return grid

def computers_entry() -> list:
    """
    Popis:
    - zahraje kolo za počítač, pokud je na řadě. Buď zabrání umístění výherního kamene protihráči,
      nebo umístí výherní kámen pro sebe a pokud tato možnost neexistuje, vybere náhodnou pozici kamene
    Parametry:
    - nezadávám
    Návratová hodnota:
    - list : aktualizuje seznam positions podle zvoleného umístění kamene
             zároveň vytiskne aktualizovanou mřížku 
    """
    print("Computer's turn.")
    condition = True
    while condition == True:
        for com in winning_combinations:
            if len(set([positions[com[0]], positions[com[1]], positions[com[2]]])) == 2 and [positions[com[0]], positions[com[1]], positions[com[2]]].count(" ") == 1:
                for i in range(len(com)):
                    if positions[com[i]] == " ":
                        index = com[i]
                        if actual_player == player_one_name:
                            positions[index] = "O"
                        else:
                            positions[index] = "X"
                        condition = False    
                        break    
                    else:
                        continue
                break    
            else:
                continue
                
        else:
            while True:
                entry = random.randrange(1, 10)
                if positions[int(entry)-1] != " ":
                    continue
                else:
                    if actual_player == player_one_name:
                        positions[int(entry) - 1] = "O"
                    else:
                        positions[int(entry) - 1] = "X"
                    break
            break
    print(separator)
    print(print_grid(positions))

def players_entry(player: str) -> str:
    """
    Popis:
    - požádá hráče, když je na řadě o umístění jeho značky. Ověří, že má vstup správnou hodnotu
      a je v rámci všech pravidel.
    Parametry:
    - player(str): jako vstup dávám jméno hráče
    Návratová hodnota:
    - list : aktualizuje seznam positions podle zvoleného umístění kamene
             zároveň vytiskne aktualizovanou mřížku 
    """
    while True:
        entry = input(f"{player} | Please enter your move number (digit 1-9):")
        if not entry.isdigit() or int(entry) not in range(1,10):
            print("You didn't enter proper value, try again.", separator, sep="\n")
            continue
        elif positions[int(entry)-1] != " ":
            print("This cell is already taken, try again.", separator, sep="\n")
            continue
        else:
            if actual_player == player_one_name:
                positions[int(entry) - 1] = "O"
            else:
                positions[int(entry) - 1] = "X"
            print(separator)
            print(print_grid(positions))
            break

# definování funkce, která ověří, že ve hře už je výherní kombinace - 3 znaky v jedné řadě 
def find_three(marks: list) -> bool:
    """
    Popis:
    - funkce, která ověří po každém zadání kamene, zda není v mřížce už výherní kombinaci 
      tří stejných značek v řadě
    Parametry:
    - marks(list): vstupním parametrem je aktualizovaný seznam pozic kamenů
    Návratová hodnota:
    - boolean : v případě návratové hodnoty True se vypíše gratulace vítězi
                v případě návratové hodnoty False hra pokračuje 
    """
    victory = f"Congratulations, '{actual_player}' WON! \n{separator}"
    for combination in winning_combinations:
        if marks[combination[0]] == marks[combination[1]] == marks[combination[2]] and marks[combination[0]] != " ":
            print(victory)
            return True
        else:
            continue
    return False
    
# vypsání uvítací fráze a pravidel hry
print(f"""
Welcome to Tic Tac Toe
{separator}
GAME RULES:
Each player can place one mark (or stone)
per turn on the 3x3 grid. The WINNER is
who succeeds in placing three of their
marks in a:
* horizontal,
* vertical or
* diagonal row
{separator}
Enter your names please.\nIf you press 'Enter' without input, it's computer's time to shine.
{separator}""")

# zadání kombinace hráčů - můžou hrát proti sobě dva hráči, hráč proti počítači nebo nechat hrát dva počítače proti sobě
player_one_name = input("Player one, input your name please: ")
if player_one_name == "":
    player_one_name = "Computer O"
                      
player_two_name = input("Player two, input your name please: ")
if player_two_name == "":
    player_two_name = "Computer X"                                                

print(f"""
{separator}      
Let's start the game. {player_one_name} x {player_two_name} \
"""
)

# vykreslení mřížky před první volbou včetně očíslování políček pro lepší orientaci na začátku hry
print(separator, print_grid(grid_marking), separator, sep="\n")

# průběh hry se zadáváním vstupů jednotlivých hráčů, ověřováním jejich platnosti, kontroly výherní kombinace a gratulace výherci
while True:
    actual_player = player_one_name
    if actual_player == "Computer O":
       computers_entry()
    else:
        players_entry(player_one_name)
    print(separator)

    if find_three(positions) == True:
        break
    
    if not " " in positions:
        print("Nobody was able to place three marks in the row. It's a draw!", separator, sep="\n") 
        break

    actual_player = player_two_name
    if actual_player == "Computer X":
       computers_entry()
    else:   
        players_entry(player_two_name)
    print(separator)
    if find_three(positions) == True:
        break

