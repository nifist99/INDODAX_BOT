
from api.user import user_indodax
from view.table import welcome,sayonara
import os
from INDODAXBOT import bot
from INDODAXSELL import INDODAXSELL
from INDODAXUPDATE import INDODAXUPDATE
from api.web import tanlalana

def login(email,password):
    user=user_indodax.indodax_login(email,password)
    IndodaxSettingApp=tanlalana
    if(user['api_status']==1):
        print(user['api_message'])
        global id_users
        id_users=user['data']['id']

        print("[1] MENU PROGRAM UTAMA BOT TRADING :")
        print("[2] MENU UPDATE STRATEGI DAN PARAMETER WEB :")
        print("[3] MENU SELL COIN CRYPTO :")
        print("")
        confrim = int(input("[MASUKAN ANGKA MENU] : "))
        if(confrim==1):
            bot(id_users)
        elif(confrim==2):
            INDODAXUPDATE(id_users)
        elif(confrim==3):
            INDODAXSELL(id_users)
        else:
            print("[MASUKAN ANGKA SESUI MENU]")

    else:
        print("")
        print(user['api_message'])
        print("")
        confirmasi = str(input("[APAKAH ANDA INGIN MENCOBA LAGI KETIK Y/y] : "))
        if(confirmasi=="y" or confirmasi=="Y"):
            nt=IndodaxSettingApp.control_indodax('windows not sleep',user['data']['id'])
            if(nt['status']=='active'):
                os.system('cls')
            else:
                os.system('clear')
            main()
        else:
            os.system('cls')
            sayonara()
            exit()

def process():
    welcome()
    email = str(input("[MASUKAN EMAIL] : "))
    password = str(input("[MASUKAN PASSWORD] : "))
    login(email,password)

def main():
    process()

if __name__ == "__main__":
      main()