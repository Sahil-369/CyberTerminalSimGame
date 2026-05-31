print("Welcome to the Cyber Terminal.")
print("----------Terminal----------")

#----------commands----------#
cmnd = ""
class ls:

    def zwiggato():
        print("""
storyline.txt
server
objectives
orderlist.txt
""")
    def objectives():
        missions = """
mission1.txt
mission2.txt
mission3.txt
mission4.txt
mission5.txt
mission6.txt
"""
        print(missions)
    
    def root():
        print("""
logs
zwiggato
""")

class cd:

    
    def back():
        global path
        if path == "/root/zwiggato>>":
            path = "/root>>"      
        elif path == "/root>>":
            pass
        elif path == "/root/zwiggato/objectives>>" :
            path = "/root/zwiggato>>"
        
    def zwiggato():
        global path
        path = "/root/zwiggato>>"

    def objectives():
        global path
        path = "/root/zwiggato/objectives>>"
        


def help():
    print("""
ls                      list files and directories
cd                      change directory
cd ..                   go to one directory back
cd <directoryname>      go to the directory
cat <file name>         print content of a file
help                    show help
apache start /server    start server
nmap <target ip>        scan target machine
msfconsole              start metasploit framework
edit <file name>        edit file
stats                   see your progress in the game
""")

class cat:

    def missions(mn):
        
        if path == "/root/zwiggato/objectives>>":
            
            with open(f"CyberGame/objectives/mission{mn}.txt") as file:
                content = file.read()
                print(content)
        else:
            print("No such file exists")
        
    def story():
        if path == "/root/zwiggato>>":
            with open("storyline.txt") as file:
                content = file.read()
                print(content)
        else:
            print("No such file exists.")

    def logs():
        if path == "/root>>" :
            with open("CyberGame/logs") as file:
                content = file.read()
                print(content)
            save("15%", "Curious")
        else:
            print("No such file exists.")
    
    def order():
        if path == "/root/zwiggato>>":
            with open("CyberGame/orderlist.txt") as file:
                content = file.read()
                print(content)
                if "customerid:order:price" in content:
                    print("System warning!")  
                    save("10%", "Beginner")

        else:
            print("No such file exists.")


class edit:

    def missions(mn):
        
        if path == "/root/zwiggato/objectives>>":
            
            with open(f"CyberGame/objectives/mission{mn}.txt", "a") as file:
                print("press enter to append")
                add = input("")
                file.write(add)
                
        else:
            print("No such file exists")
        
    def story():
        if path == "/root/zwiggato>>":
            with open("storyline.txt", "a") as file:
                print("press enter to append")
                add = input("")
                file.write(add)
                
        else:
            print("No such file exists.")

    def logs():
        if path == "/root>>" :
            with open("CyberGame/logs", "a") as file:
                print("press enter to append")
                add = input("")
                file.write(add)
                       
        else:
            print("No such file exists.")

    def order():
        if path == "/root/zwiggato>>":
            with open("CyberGame/orderlist.txt", "a") as file:
                print("press enter to append")
                add = input("")
                file.write(add)
        else:
            print("No such file exists.")


def nmap():
    ip = cmnd[5:16]
    if ip == "192.168.1.5" :
        print("""open ports found
80/tcp
445/SMBv1
21/ftp""")
        save("30%", "Script kiddie")
    else:
        print("IP is not reachable.")

class ms:
    mscmd = ""
    excmd = ""
    payload = ""
    Rhosts = ""
    Rport = ""
    viccmd = ""
    victim = ""
    docs = """
important.txt
presentation.ppt
"""
    z = """
notes.txt
mo.txt
"""

    def set():
        if ms.excmd[4:11] == "payload" :
            print(f"Parameter payload set to {ms.excmd[12:]}")
            ms.payload = f"{ms.excmd[12:]}"
        elif ms.excmd[4:10] == "RHOSTS" :
            print(f"Parameter RHOSTS set to {ms.excmd[11:]}")
            ms.Rhosts = f"{ms.excmd[11:]}"
        elif ms.excmd[4:9] == "RPORT" :
            print(f"Parameter RPORT set to {ms.excmd[10:]}")
            ms.Rport = f"{ms.excmd[10:]}"
        elif ms.excmd[4:10] == "LHOSTS" :
            print(f"Parameter LHOSTS set to {ms.excmd[11:]}")

    def vicsys():

        if ms.viccmd == "dir":

            print("""
Documents
zwiggato
""")
        elif ms.viccmd == "cd Documents":
            while ms.viccmd != "cd ..":
                ms.viccmd = input(f"{ms.victim[0:len(ms.victim)-1]}/Documents>>")
                
                if ms.viccmd == "dir":
                    
                    print(ms.docs)
                elif ms.viccmd == "type important.txt":
                        print("""
presentation's deadline is, 2nd march, 2026 
""")
                elif ms.viccmd == "del presentation.ppt":
                    ms.docs = "important.txt"
                    save("100%", "Real CyberPerson")
                elif ms.viccmd == "cd ..":
                    pass
                else:
                    print("""You Bastard, complete the mission or
Go to the real terminal and experience the hell.""")

        elif ms.viccmd == "cd zwiggato":
            while ms.viccmd != "cd ..":
                ms.viccmd = input(f"{ms.victim[0:len(ms.victim)-1]}/zwiggato>>")
                

                if ms.viccmd == "dir":
                    print(ms.z)

                elif ms.viccmd == "type notes.txt":
                
                    print("""hacked zwiggato server and
exported costumers mobile number.
The Red cafe will buy these on 5th march 2026""")
                elif ms.viccmd == "type mo.txt":
                    print("""
Mr. Sahil  235753563
Mrs. Sharma 7453755663
Ms. Unknown 5244624563
""")
                elif ms.viccmd == "del mo.txt":
                    ms.z = "notes.txt"
                    save("80%", "Begginer of real cyber practices.")

        else :
                    print("""Fuck you player!
just focus on the mission, 
otherwise go to the real terminal""")

            



    def use():
        exprmpt = f"msf3 exploit({ms.mscmd[4:15]})>"
        while ms.excmd != "quit":
            ms.excmd = input(exprmpt)
            if ms.excmd[0:3] == "set":
                ms.set()
            elif ms.excmd == "run":
                if ms.Rhosts == "" :
                    print("please set RHOSTS.")
                if ms.Rport == "" :
                    print("please set RPORT.")
                elif ms.Rhosts == "192.168.1.5":
                    print("access granted!")
                    save("60%", "Cyber Nerd")
            
                    ms.victim = "windows/users/neo>>"
                    
                    while ms.viccmd != "exit":
                        ms.viccmd = input(ms.victim)
                        ms.vicsys()
                    ms.victim = ""
                elif ms.Rhosts != "192.168.1.5":
                    print("victim is not alive.")
                else:
                    print("This is a game not the real world!")
            elif ms.excmd == "show options":
                print(f"""
RHOSTS  {ms.Rhosts}
Payload  {ms.payload}
RPORT  {ms.Rport}
LHOST  192.168.1.2
LPORT  8080
""")
                save("50%", "Cyber Student")
            else :
                print("""Are you a dick?
If you want to explore, 
Then go to the real terminal""")



    def msfconsole():
        
        while ms.mscmd != "quit":
            prompt = "msf3>"
            ms.mscmd = input(prompt)
            if ms.mscmd[0:3] == "use":
                ms.use()
                save("40%", "Guide follower")
            
    
#------save stats--------#

def save(comp, rank):
    with open("CyberGame/stats", "w") as file:
        file.write(f"Progress: {comp}\nRank: {rank}")

def stats():
    with open("CyberGame/stats") as file:
        print(file.read())

#----------terminal----------#

path = "/root/zwiggato>>"
while True :
    cmnd = input(path)
    if cmnd == "ls":
        if path == "/root/zwiggato>>":
            ls.zwiggato()
        elif path == "/root/zwiggato/objectives>>":
            ls.objectives()
        elif path == "/root>>":
            ls.root()
        else:
            print("if you wanna explore, turn off the screen and explore the world.")

    elif cmnd == "cd ..":
        cd.back()

    elif cmnd == "cd objectives":
        cd.objectives()
    elif cmnd == "cd zwiggato" :
        cd.zwiggato()

    elif cmnd == "help":
        help()
    elif cmnd[0:3] == "cat":
        if cmnd[4:11] == "mission":
            n = cmnd[11:12]
            cat.missions(n)
        elif cmnd[4:] == "storyline.txt":
            cat.story()
        elif cmnd[4:] == "logs":
            cat.logs()
        elif cmnd[4:] == "orderlist.txt":
            cat.order()
        else:
            print("if you want to explore, go to the real terminal.")
    elif cmnd[0:4] == "nmap":
        nmap()
    elif cmnd == "msfconsole":
        ms.msfconsole()
    elif cmnd == "stats":
        stats()
    elif cmnd == "apache start /server":
        print("Server is started in the background.")
        save("5%", "Starter")
    elif cmnd[0:4] == "edit":
        if cmnd[5:11] == "mission":
            n = cmnd[11:12]
            edit.missions(n)
        elif cmnd[5:] == "storyline.txt":
            edit.story()
        elif cmnd[5:] == "logs":
            edit.logs()
        elif cmnd[5:] == "orderlist.txt":
            edit.order()
        else:
            print("if you want to explore, go to the real terminal.")
    else:
        print("go and explore real world")
