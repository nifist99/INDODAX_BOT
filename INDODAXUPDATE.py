from api.web import tanlalana,tanlalana_fungsi
from api.public import indodax 
from api.user import user_indodax 
import time
import os
from config import setting
#aksi looping 

def update_sr_to_server(crypto):
        print("ini adalah update data to server")
        NewTanlalana=tanlalana
        NewIndodax=indodax(crypto)
        #ambil info status coin sekarang dari server
        result=NewIndodax.api_ticker_detail()
        #update suport resisten ke server tanlalna
        status=NewTanlalana.update_suport_resisten_to_server(crypto,result['ticker']['low'],result['ticker']['high'],result['ticker']['sell'],result['ticker']['buy'])
        NewTanlalana.update_btc()
        print(status)

def update_user():
            NewTanlalana=tanlalana
            list=NewTanlalana.list_data_server()
            
            for f in list:
                print("update data to server ", f['coin'])
                cek=user_indodax.update_user(f['coin'],3)
                
            
            print("selesai update data to server")

def update_data():
            NewTanlalana=tanlalana
            list=NewTanlalana.list_data_server_active()
            
            for f in list:
                print("update data to server ....")
                update_sr_to_server(f['coin'])

            
            print("selesai update data to server")

def update_strategi_reset():
            NewTanlalana=tanlalana
            list=NewTanlalana.list_data_server_active()
            
            for f in list:
                print("melakukan reset strategi coin = ",f['coin'])
                tanlalana.strategi_reset(f['id'])
            
            print("selesai reset strategi silahkan cek perubahan di website")

def update_dump_reset():
            NewTanlalana=tanlalana
            list=NewTanlalana.list_data_server_active()
            
            for f in list:
                print("melakukan reset dump coin = ",f['coin'])
                cek=tanlalana.dump_reset(f['id'])
                print(cek)
            
            print("selesai reset dump silahkan cek perubahan di website")

def desesion():
    print("wait.......")
    time.sleep(2)
    print("")
    print("PILIH [1] UNTUK UPDATE SUPORT RESISTEN ALL")
    print("PILIH [2] UNTUK UPDATE 1 KOIN")
    print("PILIH [3] UNTUK RESET STRATEGI")
    print("PILIH [4] UNTUK RESET DUMP")

    print("============================================")
    print("")
    
    nama = int(input("SILAHKAN PILIH MENGGUNAKAN ANGKA ="))
    if(nama==1):
        print("")
        print("melakukan perintah update semua koin aktif")
        time.sleep(2)
        loop()
        masukan=input("masukan Y / y untuk melanjutkan program =")
        if(masukan=='y' or masukan=='Y'):
            os.system('cls')
            INDODAXUPDATE()
        else:
            print("")
            print("selesai melakukan update keluar aplikasi ..........")
            os.system('cls')
            os.close()
    elif(nama==2):
        print("")
        print("memilih 1 koin :")
        crypto=input('silahkan masukan uang crypto contoh [zilidr] =')
        single(crypto)
        masukan=input("masukan Y / y untuk melanjutkan program =")
        if(masukan=='y' or masukan=='Y'):
            os.system('cls')
            INDODAXUPDATE()
        else:
            print("")
            print("selesai melakukan update keluar aplikasi ..........")
            os.system('cls')
            os.close()
    elif(nama==3):
        print("melakukan reset strategi all")
        update_strategi_reset()
        masukan=input("masukan Y / y untuk melanjutkan program =")
        if(masukan=='y' or masukan=='Y'):
            os.system('cls')
            INDODAXUPDATE()
        else:
            print("")
            print("selesai melakukan update keluar aplikasi ..........")
            os.system('cls')
            os.close()
    elif(nama==4):
        print("melakukan reset dump all")
        update_dump_reset()
        masukan=input("masukan Y / y untuk melanjutkan program =")
        if(masukan=='y' or masukan=='Y'):
            os.system('cls')
            INDODAXUPDATE()
        else:
            print("")
            print("selesai melakukan update keluar aplikasi ..........")
            os.system('cls')
            os.close()
    else:
        os.system('cls')
        print("pilih yang benar ngab angkanya !!!!!!!")
        INDODAXUPDATE()

def single(crypto):
        print("")
        print("ini adalah update data to server")
        NewTanlalana=tanlalana
        NewIndodax=indodax(crypto)
        #ambil info status coin sekarang dari server
        result=NewIndodax.api_ticker_detail()
        #update suport resisten ke server tanlalna
        status=NewTanlalana.update_suport_resisten_to_server(crypto,result['ticker']['low'],result['ticker']['high'],result['ticker']['sell'],result['ticker']['buy'])
        NewTanlalana.update_btc()
        time.sleep(2)
        print("")
        print("selesai melaukan update koin =",crypto)
        r=input("apakah anda akan melakukan update lagi ? jika iya Tekan Y jika tidak tekan N =")
        if(r=='Y' or r=='y'):
            return desesion()
        elif(r=='N' or r=='n'):
            exit()
        

def loop():
        #cekk setting app
        IndodaxSettingApp=tanlalana
        status_app= IndodaxSettingApp.control_indodax('trading indodax')
        osSleep = None

        #in Windows, prevent the OS from sleeping while we run
        if(status_app['status']=='active'):
            print("")
            print("===========================================")           
            print("app indodax on")
            print("menjalakan api update coin active")
            update_data()
        else:
            print("")
            print("===============================================")           
            print("app indodax off silahkan onkan agar program berjalan")
        print("")
        print("selesai melakukan update semua coin.....")

def INDODAXUPDATE():
    desesion()
    # update_user()
   
# if __name__ == "__main__":
#       main()