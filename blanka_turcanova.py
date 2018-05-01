from random import randint


herni_pole = '.' * 10
herni_pole = list(herni_pole)
delka_pole = len(herni_pole)
def tah_hrace():
    vstup = int(input('zadejte pozici 0 - 9: '))
    if herni_pole[vstup] == '.':
        herni_pole[vstup] = 'x'
    else:
        print('hahaha! mas to blbe;)')
        tah_hrace()

def tah_pocitace():
    stav = True
    while stav:
        pozice = randint(0, delka_pole)
        if herni_pole[pozice] == '.':
            herni_pole[pozice]= 'o'
            stav = False


def vyhodnot_stav():
    str_herni_pole = ''.join(herni_pole)
    if 'xxx' in str_herni_pole:
        print('huraaaa you landlubber!!!!')
        return False
    if 'ooo' in str_herni_pole:
        print('you suck you idontknowwhat!!!')
        return False
    if '.' not in str_herni_pole:
        print('remizka')
        return False
    else:
        return True

stav_hry = True
while stav_hry:
    print(herni_pole)
    tah_hrace()
    stav_hry = vyhodnot_stav()
    tah_pocitace()
    stav_hry = vyhodnot_stav()
