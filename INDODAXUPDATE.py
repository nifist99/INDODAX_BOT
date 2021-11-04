from api.web import tanlalana,tanlalana_fungsi
from api.public import indodax 
from api.user import user_indodax 
import time
import os
from config import setting
from view.table import txt
#aksi looping 

def update_sr_to_server(id_users,crypto):
        txt("INI ADALAH PROGRAM UPDATE DATA TO SERVER")
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
                update_sr_to_server(id_users,f['coin'])
            
            txt("SELESAI UPDATE DATA TO SERVER")

def update_strategi_reset(id_users):
            NewTanlalana=tanlalana
            list=NewTanlalana.list_data_server_active(id_users)
            for f in list:
                txt("MELAKUKAN RESET FIBONANCI = "+f['coin'])
                tanlalana.strategi_reset(f['id'],id_users)
            
            txt("SELESAI MELAKUKAN PERUBAHAN RESET FIBONANCI ALL COIN ACTIVE")

def update_dump_reset(id_users):
            NewTanlalana=tanlalana
            list=NewTanlalana.list_data_server_active(id_users)
            
            for f in list:
                txt("MELAKUKAN RESET DUMP = "+f['coin'])
                cek=tanlalana.dump_reset(f['id'],id_users)
                print(cek)
            
            txt("SELESAI MELAKUKAN RESET DUMP ALL COIN ACTIVE")

def desesion(id_users):
    print("WAIT.......")
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
        txt("MELAKUKAN UPDATE ALL COIN")
        time.sleep(2)
        loop(id_users)
        masukan=input("MASUKAN Y / y UNTUK MELANJUTKAN PROGRAM =")
        if(masukan=='y' or masukan=='Y'):
            os.system('cls')
            INDODAXUPDATE(id_users)
        else:
            os.system('cls')
    elif(nama==2):
        print("")
        txt("MEMILIH 1 COIN :")
        crypto=input('SILAHKAN MASUKAN COIN CRYPTO CONTOH [zilidr] =')
        single(crypto,id_users)
        masukan=input("MASUKAN Y / y UNTUK MELANJUTKAN PROGRAM =")
        if(masukan=='y' or masukan=='Y'):
            os.system('cls')
            INDODAXUPDATE(id_users)
        else:
            os.system('cls')
    elif(nama==3):
        update_strategi_reset(id_users)
        masukan=input("MASUKAN Y / y UNTUK MELANJUTKAN PROGRAM =")
        if(masukan=='y' or masukan=='Y'):
            os.system('cls')
            INDODAXUPDATE(id_users)
        else:
            os.system('cls')
    elif(nama==4):
        update_dump_reset(id_users)
        masukan=input("MASUKAN Y / y UNTUK MELANJUTKAN PROGRAM =")
        if(masukan=='y' or masukan=='Y'):
            os.system('cls')
            INDODAXUPDATE(id_users)
        else:
            os.system('cls')
    else:
        os.system('cls')
        txt("PILIH YANG BENAR ANGKANYA NGAB !!!!!!!")
        INDODAXUPDATE(id_users)

def single(crypto,id_users):
        NewTanlalana=tanlalana
        NewIndodax=indodax(crypto)
        #ambil info status coin sekarang dari server
        result=NewIndodax.api_ticker_detail()
        #update suport resisten ke server tanlalna
        status=NewTanlalana.update_suport_resisten_to_server(id_users,crypto,result['ticker']['low'],result['ticker']['high'],result['ticker']['sell'],result['ticker']['buy'])
        time.sleep(2)
        print("")
        txt("SELESAI MELAKUKAN UPDATE COIN ="+crypto)


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
   