from time import sleep
import os

os.system('cls')
def Intro():
  x = "░"
  i = 0
  j = "."
  k = 1
  while True:
    os.system('cls')
    print(f"Loading{j}\t {i*2} %")
    print("__________________________________________________")
    print(x * i)
    print("\u203e"*50)   
    i += 1
    sleep(0.05)
    if j == ".":
      j = ".."
    elif j == ".." and i % 2 == 0:
      j = "..."
    elif j == ".." and i % 2 != 0:
      j = "."
    elif j == "...":
      j = ".."
    if i == 49:
      for k in range(99,74,-1):
        os.system('cls')
        print(f"Loading{j}\t {k} %")
        print("__________________________________________________")
        print(x * round(k/2))
        print("\u203e"*50) 
        if k == 99:
          sleep(4)  
        sleep(0.05)

      for k in range(75,125):
        os.system('cls')
        print(f"Loading{j}\t {k} %")
        print("__________________________________________________")
        print(x * round(k/2))
        print("\u203e"*50)
        sleep(0.05) 
        if k == 100:
          print("""
      ░░░░░▄▄▄▄▀▀▀▀▀▀▀▀▄▄▄▄▄▄░░░░░░░
      ░░░░░█░░░░▒▒▒▒▒▒▒▒▒▒▒▒░░▀▀▄░░░░
      ░░░░█░░░▒▒▒▒▒▒░░░░░░░░▒▒▒░░█░░░
      ░░░█░░░░░░▄██▀▄▄░░░░░▄▄▄░░░░█░░
      ░▄▀▒▄▄▄▒░█▀▀▀▀▄▄█░░░██▄▄█░░░░█░
      █░▒█▒▄░▀▄▄▄▀░░░░░░░░█░░░▒▒▒▒▒░█
      █░▒█░█▀▄▄░░░░░█▀░░░░▀▄░░▄▀▀▀▄▒█
      ░█░▀▄░█▄░█▀▄▄░▀░▀▀░▄▄▀░░░░█░░█░
      ░░█░░░▀▄▀█▄▄░█▀▀▀▄▄▄▄▀▀█▀██░█░░
      ░░░█░░░░██░░▀█▄▄▄█▄▄█▄████░█░░░
      ░░░░█░░░░▀▀▄░█░░░█░█▀██████░█░░
      ░░░░░▀▄░░░░░▀▀▄▄▄█▄█▄█▄█▄▀░░█░░
      ░░░░░░░▀▄▄░▒▒▒▒░░░░░░░░░░▒░░░█░
      ░░░░░░░░░░▀▀▄▄░▒▒▒▒▒▒▒▒▒▒░░░░█░
      ░░░░░░░░░░░░░░▀▄▄▄▄▄░░░░░░░░█░░
                """)
          sleep(1.5)
          os.system('cls')
          break
      os.system('cls')
      break


  #### need function to "stop" the Loading Animation with Key Input!



print('''
*    ___       _______ *____    ____  _______ .__ * __. .___________. __    __  .______*      _______ 
    /   \  *  |       \ \   \ */   / |   ____||  \ |  | |           ||  | *|  | |   _  \     |   ____|
   /  ^  \    |  .--.  | \   \/   /  |  |_*   |   \|  | `---|  |----`|  |  |  | |  |_)  |    |  |_*   
  /  /_\  \   |  | *|  |  \      /   |   __|  |  . `  |   * |  |    *|  |  |  | |      /   * |   __|  
 /  _____  \ *|  '--'  |   \    / *  |  |____*|  |\   |     |  |     |  `--'  | |  |\  \----.|  |____*
/__/     \__\ |_______/    *\__/     |_______||__| \__|*    |__|      \______/  | _|*`._____||_______|
                                                                                            
                                                                                                       by Nils and Samo''')