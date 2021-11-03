from api.web import tanlalana,tanlalana_fungsi
from api.public import indodax 
from api.user import user_indodax 
import time
import os
from config import setting
#aksi looping 

def update_sr_to_server(id_users,crypto):
        print("ini adalah update data to server")
        NewTanlalana=tanlalana
        NewIndodax=indodax(crypto)
        #ambil info status coin sekarang dari server
        result=NewIndodax.api_ticker_detail()
        #update suport resisten ke server tanlalna
        status=NewTanlalana.update_suport_resisten_to_server(id_users,crypto,result['ticker']['low'],result['ticker']['high'],result['ticker']['sell'],result['ticker']['buy'])
        print(status)

def update_data(id_users):
            NewTanlalana=tanlalana
            list=NewTanlalana.list_data_server_active(id_users)
            
            for f in list:
                print("update data to server ....")
                update_sr_to_server(id_users,f['coin'])
            
            print("selesai update data to server")

def update_strategi_reset(id_users):
            NewTanlalana=tanlalana
            list=NewTanlalana.list_data_server_active(id_users)
            for f in list:
                print("melakukan reset strategi coin = ",f['coin'])
                tanlalana.strategi_reset(f['id'],id_users)
            
            print("selesai reset strategi silahkan cek perubahan di website")

def update_dump_reset(id_users):
            NewTanlalana=tanlalana
            list=NewTanlalana.list_data_server_active(id_users)
            
            for f in list:
                print("melakukan reset dump coin = ",f['coin'])
                cek=tanlalana.dump_reset(f['id'],id_users)
                print(cek)
            
            print("selesai reset dump silahkan cek perubahan di website")

def desesion(id_users):
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
        loop(id_users)
        masukan=input("masukan Y / y untuk melanjutkan program =")
        if(masukan=='y' or masukan=='Y'):
            os.system('cls')
            INDODAXUPDATE(id_users)
        else:
            print("")
            print("selesai melakukan update keluar aplikasi ..........")
            os.system('cls')
            os.close()
    elif(nama==2):
        print("")
        print("memilih 1 koin :")
        crypto=input('silahkan masukan uang crypto contoh [zilidr] =')
        single(crypto,id_users)
        masukan=input("masukan Y / y untuk melanjutkan program =")
        if(masukan=='y' or masukan=='Y'):
            os.system('cls')
            INDODAXUPDATE(id_users)
        else:
            print("")
            print("selesai melakukan update keluar aplikasi ..........")
            os.system('cls')
            os.close()
    elif(nama==3):
        print("melakukan reset strategi all")
        update_strategi_reset(id_users)
        masukan=input("masukan Y / y untuk melanjutkan program =")
        if(masukan=='y' or masukan=='Y'):
            os.system('cls')
            INDODAXUPDATE(id_users)
        else:
            print("")
            print("selesai melakukan update keluar aplikasi ..........")
            os.system('cls')
            os.close()
    elif(nama==4):
        print("melakukan reset dump all")
        update_dump_reset(id_users)
        masukan=input("masukan Y / y untuk melanjutkan program =")
        if(masukan=='y' or masukan=='Y'):
            os.system('cls')
            INDODAXUPDATE(id_users)
        else:
            print("")
            print("selesai melakukan update keluar aplikasi ..........")
            os.system('cls')
            os.close()
    else:
        os.system('cls')
        print("pilih yang benar ngab angkanya !!!!!!!")
        INDODAXUPDATE(id_users)

def single(crypto,id_users):
        print("")
        print("ini adalah update data to server")
        NewTanlalana=tanlalana
        NewIndodax=indodax(crypto)
        #ambil info status coin sekarang dari server
        result=NewIndodax.api_ticker_detail()
        #update suport resisten ke server tanlalna
        status=NewTanlalana.update_suport_resisten_to_server(id_users,crypto,result['ticker']['low'],result['ticker']['high'],result['ticker']['sell'],result['ticker']['buy'])
        time.sleep(2)
        print("")
        print("selesai melaukan update koin =",crypto)
        r=input("apakah anda akan melakukan update lagi ? jika iya Tekan Y jika tidak tekan N =")
        if(r=='Y' or r=='y'):
            return desesion(id_users)
        elif(r=='N' or r=='n'):
            exit()
        

def loop(id_users):
        #cekk setting app
        IndodaxSettingApp=tanlalana
        status_app= IndodaxSettingApp.control_indodax('trading indodax',id_users)

        #in Windows, prevent the OS from sleeping while we run
        if(status_app['status']=='active'):
            print("")
            print("===========================================")           
            print("app indodax on")
            print("menjalakan api update coin active")
            update_data(id_users)
        else:
            print("")
            print("===============================================")           
            print("app indodax off silahkan onkan agar program berjalan")
        print("")
        print("selesai melakukan update semua coin.....")

def INDODAXUPDATE(id_users):
    desesion(id_users)
   