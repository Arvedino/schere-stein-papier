from random import randint


def eingabe(eingabe):
    global ausgabe
    if eingabe == "s" or eingabe == "Schere" or eingabe == "schere":
        ausgabe= 1
    elif eingabe == "r" or eingabe == "Stein" or eingabe == "stein":
        ausgabe= 2
    elif eingabe == "p" or eingabe == "Papier" or eingabe == "papier":
        ausgabe= 3
    else:
        print("Die Eingabe von \'" + eingabe + "\' ist ein üngültiges Wort/Zeichen.")
        ausgabe = None
    return ausgabe

def Computer(ausgabespieler):
    ergebnis = 0
    computer = randint(1,3)
    if ausgabespieler == computer:
        ergebnis = 1
    elif ausgabespieler == 1 and computer == 2:
        ergebnis = 2
    elif ausgabespieler == 1 and computer == 3:
        ergebnis = 3
    elif ausgabespieler == 2 and computer == 1:
        ergebnis = 3
    elif ausgabespieler == 2 and computer == 3:
        ergebnis = 2
    elif ausgabespieler == 3 and computer == 1:
        ergebnis = 2
    elif ausgabespieler == 3 and computer == 2:
        ergebnis = 3
    return [ergebnis, computer]


        
        
        
        
        
