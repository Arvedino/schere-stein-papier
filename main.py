from module import *
import login


punkte = [0, 0, 0]

#Login-Abschnitt

username = None
password = None

register = False
loginn = False

while True:
    username = input("Gebe deinen Nutzernamen hier ein (oder tippe R wenn du noch keinen Account hast): ")
    if username == "R":
        register = True
        break
    password = input("Gebe dein Passwort hier ein: ")
    erfolg = login.login(username, password)
    if erfolg:
        loginn = True
        break
    if not erfolg:
        print("Das Passwort ist leider falsch. Versuch es nochmal.")

if register:
    while True:
        username = input("Gebe deinen Nutzernamen hier ein: ")
        password = input("Gebe dein Passwort hier ein: ")
        exists = login.register(username, password)
        if exists:
            print("Dieser Nutzername existiert bereits. Versuch es nochmal.")
        else:
            loginn = True
            break

if loginn:
    global punktestand
    punktestand = login.getvaluefromuser(username, password)
    if punktestand == False:
        print("Ein Fehler ist aufgetreten. Das Programm wird sich jetzt herunterfahren.")
        quit()
    try:
        gewinnerquote = punktestand[1]/punktestand[2]
    except ZeroDivisionError:
        gewinnerquote = 1
    
    

    print("""Dein Punktestand ist:

Gewonnen: """+str(punktestand[1])+"""
Verloren: """+str(punktestand[0])+"""
Rundenzahl: """+str(punktestand[2])+"""
Gewinnerquote: """+str(round(gewinnerquote*100, 1))+"""%
""")
    
    # Hauptprogramm
    
    while punkte[2] <= 20:
        punkte[2] += 1
        print("Runde: ", punkte[2])
        while True:
            ssp_eingabe = input("Spieler1: Schere (s), Stein (r) oder Papier (p)?: ")
            ausgabe = eingabe(ssp_eingabe)
            if ausgabe != None:
                break
        
        ergebnis = Computer(ausgabe)
        
        if ergebnis[1] == 1:
            ergebnis[1] = "Schere"
        elif ergebnis[1] == 2:
            ergebnis[1] = "Stein"
        elif ergebnis[1] == 3:
            ergebnis[1] = "Papier"
        
        if ergebnis[0] == 1:
            print("Unentschieden!")
        if ergebnis[0] == 2:
            punkte[0] += 1
            print("Der Computer gewinnt!")
            print("Computer:"+ ergebnis[1])
        if ergebnis[0] == 3:
            punkte[1] += 1
            print("Du gewinnst!")
            print("Computer:"+ ergebnis[1])
            
        
        weiterspielen = input("Möchtest du weiterspielen? (j für Ja und n für Nein)")
        weiterspielenl = weiterspielen.lower()
        if weiterspielenl == "j" or weiterspielenl == "ja":
            continue
        elif weiterspielenl == "n" or weiterspielenl == "nein":
            break
        else:
            print("Die Eingabe von "+ weiterspielen +" ist nicht korrekt.")
            continue
    
        
else:
    print("Ein Fehler ist aufgetreten. Das Programm wird sich jetzt herunterfahren.")

generellePunkte = [punktestand[0]+punkte[0], punktestand[1]+punkte[1], punktestand[2]+punkte[2]]

s = login.writevaluetouser(username, password, generellePunkte)
if s == False:
    print("Ein Fehler ist aufgetreten. Das Programm wird sich jetzt herunterfahren.")
    quit()