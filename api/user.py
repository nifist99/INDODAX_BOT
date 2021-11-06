
from logging import exception
import time
from countdown.countdown import countdown
import requests
from requests_toolbelt import sessions
from requests.adapters import HTTPAdapter
from urllib3.util import Retry
import os


retries = Retry(total=3, backoff_factor=0.3, status_forcelist=[500, 502, 504])
adapter = HTTPAdapter(max_retries=retries)

http = sessions.BaseUrlSession(base_url="https://tanlalana.com/api/")
http.mount("https://", adapter)
http.mount("http://", adapter)


class user_indodax:
    def update_user(coin,id_users):
        try:
            param={'coin':coin,'id_users':id_users}
            url="update_user_indodax"
            http.post(url,data=param)
        except requests.exceptions.RequestException as e:  # This is the correct syntax
            raise SystemExit(e)

    def indodax_login(email,password):
        this_email=email
        this_password=password
        try:
            url="indodax_login"
            param={'email':email,'password':password}
            r=http.post(url,data=param)
            respon=r.json()
            return respon

        except Exception:
                # sleep for a bit in case that helps
                time.sleep(2)
                return user_indodax.indodax_login(this_email,this_password)
def process():
    print("MENU ADMIN ADD NEW USER")
    email = str(input("[MASUKAN EMAIL] : "))
    password = str(input("[MASUKAN PASSWORD] : "))
    user=user_indodax.indodax_login(email,password)
    if(user['api_status']==1):
        print(user['api_message'])
        global id_users
        id_users=user['data']['id']

        print("[1] MENU PROGRAM MENAMBAHKAN KOIN NEW USER :")
        print("[2] MENU PROGRAM ADD SETTING NEW USER :")
        print("[3] MENU PROGRAM ADD COMTROL NEW USER :")
        print("[4] MENU PROGRAM ADD FIBO NEW USER :")
        print("[5] MENU PROGRAM ADD DUMP NEW USER :")
        print("[6] DELETE BERKAITAN DENGAN USER :")
        print("")
        confrim = int(input("[MASUKAN ANGKA MENU] : "))
        if(confrim==1):
            user_indodax.update_user("add_coin",id_users)
            lanjut=str(input("Apakah anda akan mencoba lagi Y/y ? :"))
            if(lanjut=="y" or lanjut=="Y"):
                os.system("cls")
                main()
        elif(confrim==2):
            user_indodax.update_user("add_setting",id_users)
            lanjut=str(input("Apakah anda akan mencoba lagi Y/y ? :"))
            if(lanjut=="y" or lanjut=="Y"):
                os.system("cls")
                main()
        elif(confrim==3):
            user_indodax.update_user("add_control",id_users)
            lanjut=str(input("Apakah anda akan mencoba lagi Y/y ? :"))
            if(lanjut=="y" or lanjut=="Y"):
                os.system("cls")
                main()
        elif(confrim==4):
            user_indodax.update_user("add_fibo",id_users)
            lanjut=str(input("Apakah anda akan mencoba lagi Y/y ? :"))
            if(lanjut=="y" or lanjut=="Y"):
                os.system("cls")
                main()
        elif(confrim==5):
            user_indodax.update_user("add_dump",id_users)
            lanjut=str(input("Apakah anda akan mencoba lagi Y/y ? :"))
            if(lanjut=="y" or lanjut=="Y"):
                os.system("cls")
                main()
        elif(confrim==6):
            user_indodax.update_user("delete_coin",id_users)
            lanjut=str(input("Apakah anda akan mencoba lagi Y/y ? :"))
            if(lanjut=="y" or lanjut=="Y"):
                os.system("cls")
                main()
    else:
        print(user['api_message'])
        lanjut=str(input("Apakah anda akan mencoba lagi Y/y ? :"))
        if(lanjut=="y" or lanjut=="Y"):
            os.system("cls")
            main()


    
def main():
        process()

if __name__ == "__main__":
      main()