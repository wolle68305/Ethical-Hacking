import hashlib

def startMain():
    #function1()
    #function2()
    #function3()
    #function4()
    function5()

    print("Finish")    

def function1():    
    #encode() Funktion wandelt den String in Byte um
    #o ist ein MD5 Hash Objekt
    o = hashlib.md5("Hallo Welt".encode())
    
    #Ausgabe den Objektes in Byte Schreibweise
    print(o.digest())
    
    #Ausgabe den Objektes in Hex Schreibweise
    print(o.hexdigest())

def function2():
    with open("/home/daniel/Downloads/Kursmaterialien/data/dictionary.txt", "r") as file:
        for line in file:
            #.strip Function entfernt Leerzeichen bzw. Zeilenumbrüche von dem String
            print(line.strip())
            break

def function3():
    with open("/home/daniel/Downloads/Kursmaterialien/data/dictionary.txt", "r") as file:
        for line in file:
            #.strip Function entfernt Leerzeichen bzw. Zeilenumbrüche von dem String
            o = hashlib.md5(line.strip().encode()).hexdigest()
            print(o)
            break

def function4():
    with open("/home/daniel/Downloads/Kursmaterialien/data/dictionary.txt", "r") as file:
        for line in file:
            #.strip Function entfernt Leerzeichen bzw. Zeilenumbrüche von dem String
            o = hashlib.md5(line.strip().encode()).hexdigest()

            if o == "9e083ec666c9f3db044bb7c381640227":
                print("Found")
                print(line.strip())

def function5():
    extra_chars ="!$%&/()=?"
    with open("/home/daniel/Downloads/Kursmaterialien/data/dictionary.txt", "r") as file:
        for line in file:
            #.strip Function entfernt Leerzeichen bzw. Zeilenumbrüche von dem String
            word = line.strip()
            
            for char in extra_chars:
                combi = word + char
                #print(combi)        
                o = hashlib.md5(combi.encode()).hexdigest()
                if o == "1e3bf495a62012e7caf5fdd25624605f":
                    print("Found")
                    print(combi)                
            #break
startMain()