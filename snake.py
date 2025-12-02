while(True):
    print("> Big boss")
    print("> Wybierz opcje")
    print("1) Start")
    print("2) Opcje")
    print("q) Wyjdź")
    Snake = input("Opcja nr : ")
    if Snake == "q":
        break
    if Snake == '1':
        print("Start")
        break
    if Snake == '2':
        print("1) Alt + F4")
        print("2) Ustawienia Jamnika")
        break





import random

def numguesser():
    PLAYING = 1

    zakres = int(input('Wprowadz do jakiej liczby chcesz zgadywac: '))
    
    losowa = random.randint(1,zakres)

    liczba_prob = 0 # Jesli 3 to przegrywa    
    while(PLAYING == 1):
        if liczba_prob < 3 :
            if liczba_prob < 2:
                print("Liczba")
            wybor = int(input("Zgandij liczbe: "))

            if wybor == random:
                print(f"Zgadłeś ukrytą liczbe! to liczba {losowa}")
                PLAYING = 0
            else:
                liczba_prob += 1
                print(f"Pozostało Ci prób {3-liczba_prob}")
        else:
            print("Nie udało Ci się zgadnąć")
            PLAYING = 0

numguesser()

Papież kamien NOŻYCE

import random

def PKN():

    SCORE = 0

    while(True):

        xd = random.randint(0,2)

        opcje = ['kamień','papier','nożyce']
    
        komputer = opcje[xd]
    
        wybor = input('Co wyrzucasz? [kamień,papier,nożyce]: ')
    
        wybor_lower = wybor.lower()
    
        if wybor_lower == komputer:
            SCORE -= 1
            print('Remis! -1')
        elif wybor == 'kamień' and komputer == 'papier':
            SCORE = 0
            print(f'Przegrałeś! Tracisz wszystkie {SCORE} punkty')
        elif wybor =='papier' and komputer == 'nożyce':
            SCORE = 0
            print(f'Przegrałeś! Tracisz wszystkie {SCORE} punkty')
        elif wybor == 'nożyce' and komputer == 'kamień':
            SCORE = 0
            print(f'Przegrałeś! Tracisz wszystkie {SCORE} punkty')
        else:
            SCORE += 1
            print(f'Wygrałeś! Zyskujesz 1 punkt do puli {SCORE}')

import os
import random
import time


def color_text(text, color = "RED"):
    """
    Takes text as string,  and color as string, returns colored text, can be used in terminal.
    """
    # BLUE = '\033[94m'
    # CYAN = '\033[96m'
    # GREEN = '\033[92m'
    # ORANGE = '\033[93m'
    # RED = '\033[91m'
    if color == "RED":
        return '\033[91m'+text+'\033[0m'

    elif color == 'ORANGE':
        return '\033[93m'+text+'\033[0m'

    elif color == 'GREEN':
        return '\033[92m'+text+'\033[0m'

    elif color == 'CYAN':
        return '\033[96m'+text+'\033[0m'

    elif color == 'BLUE':
        return '\033[94m'+text+'\033[0m'

print(color_text('xd', 'GREEN'))

WIDTH = 20
HEIGHT = 10

snake = [(5, 5), (5, 4), (5, 3)] # długość początkowa
direction = 'd' # start: w prawo

food = (random.randint(0, HEIGHT-1), random.randint(0, WIDTH-1))
super_food = (random.randint(0, round((HEIGHT-1)/2)), random.randint(0, round((WIDTH-1)/2)))

# render_board() lub render_board(100, 50)

def render_board(HEIGHT = HEIGHT, WIDTH = WIDTH):
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if(y,x) == food:
                print(color_text("@"), end="")
            elif (x,y) in snake:
                print(color_text("#", "BLUE"))
            else:
                print(" ", end="")
        print()



def draw():
    os.system('cls' if os.name == 'nt' else 'clear')

    render_board

draw()

    for y in range(HEIGHT):
        for x in range(WIDTH):
            if
