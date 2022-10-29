import hashlib
import json

def encrypt(input):
    encrypted = str(hashlib.sha512(input.encode()).hexdigest())
    return encrypted


def login(username, password):

    correct = False
    
    file = open("passw", "r")

    filecont = json.loads(file.read().replace("'", "\""))
    
    file.close()
    
    encinput = encrypt(password)
        
    try:
        if filecont[username][0] == encinput:
            correct = True
    except KeyError:
        pass
    return correct

def register(username, password):
    
    file = open("passw", "r")
    
    filecont = file.read()
    
    file.close()
    
    if username in filecont:
        return True
    else:
        if filecont == "":
            filecont = "{}"
        
        filecont = json.loads(filecont.replace("'", "\""))
        
        file = open("passw", "w")
        
        filecont[username] = [encrypt(password), 0]
                
        file.write(str(filecont))
        file.close()

def writevaluetouser(username, password, value):
    correct = login(username, password)
    
    file = open("passw", "r")
    
    filecont = file.read()
    
    file.close()
    
    if correct:
        file = open("passw", "w")
        filecont = json.loads(filecont.replace("'", "\""))
        filecont[username][1] = value
        file.write(str(filecont))
        file.close()
    else:
        return correct
    
def getvaluefromuser(username, password):
    correct = login(username, password)
    
    file = open("passw", "r")
    
    filecont = file.read()
    
    file.close()
    
    if correct:
        filecont = json.loads(filecont.replace("'", "\""))
        if filecont[username][1] == 0:
            filecont[username][1] = [0, 0, 0]
        return filecont[username][1]
    else:
        return correct