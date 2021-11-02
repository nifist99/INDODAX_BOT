
from api.user import user_indodax
from view.table import welcome,sayonara
import os
from INDODAXBOT import bot
from INDODAXSELL import INDODAXSELL
from INDODAXUPDATE import INDODAXUPDATE

def login(email,password):
    user=user_indodax.indodax_login(email,password)
    if(user['api_status']==1):
        print(user['api_message'])

        print("[1] MENU PROGRAM UTAMA BOT TRADING :")
        print("[2] MENU UPDATE STRATEGI DAN PARAMETER WEB :")
        print("[3] MENU SELL COIN CRYPTO :")
        print("")
        confrim = int(input("[MASUKAN ANGKA MENU] : "))
        if(confrim==1):
            bot()
        elif(confrim==2):
            INDODAXUPDATE()
        elif(confrim==2):
            INDODAXSELL()
        else:
            print("[MASUKAN ANGKA SESUI MENU]")

    else:
        print("")
        print(user['api_message'])
        print("")
        confirmasi = str(input("[APAKAH ANDA INGIN MENCOBA LAGI KETIK Y/y] : "))
        if(confirmasi=="y" or confirmasi=="Y"):
            os.system('cls')
            main()
        else:
            os.system('cls')
            sayonara()
            exit()

def main():
    welcome()
    email = str(input("[MASUKAN EMAIL] : "))
    password = str(input("[MASUKAN PASSWORD] : "))
    login(email,password)

if __name__ == "__main__":
      main()