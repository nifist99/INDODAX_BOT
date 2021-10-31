from strategi.dump import strategi_dump_buy
from api.web import tanlalana,tanlalana_fungsi
from api.public import indodax 
from strategi.fibo import fungsi_strategi_fibo
from strategi.sell import sell_all
from config import WindowsInhibitor
from api.private import private_api
import time
import os
from config import setting
#aksi looping 
from INDODAXSELL import jual_semua_asset,view_coin_jumlah
from INDODAXUPDATE import update_data,update_strategi_reset,update_dump_reset

def fibonanci_action_beli():
            NewTanlalana=tanlalana
            list=NewTanlalana.list_fibo_active()

            for f in list:
                print("memulai program screening strategi fibonanci buy.....",f['coin'])
                Newanalisis_execute=fungsi_strategi_fibo(f['coin'])
                Newanalisis_execute.fibonanci()
            print("selesai melakukan screening strategi fibonanci buy.......")
            print("Eksekusi Jam :",time.strftime("%H:%M:%S", time.localtime()))

def main():
        #cekk setting app
        #cek btc indodax menghindari dumb
        NewBtc=indodax("btc")
        status_btc=NewBtc.api_detail_btc()
        harga_btc=float(status_btc['ticker']['buy'])

        #cekk setting app
        IndodaxSettingApp=tanlalana
        dum_btc=IndodaxSettingApp.indodax_setting("btc")
        # status_app=IndodaxSettingApp.indodax_setting("status")

        parameter_dum_btc=float(dum_btc['parameter_int'])
        osSleep = None

        status_app= IndodaxSettingApp.control_indodax('trading indodax')

        #in Windows, prevent the OS from sleeping while we run
        if(status_app['status']=='active'):
            print("")
            print("===============================================")          
            print("app indodax on")
            while True:
                auto_sell= IndodaxSettingApp.control_indodax('simple sell')
                control_dumb_buy= IndodaxSettingApp.control_indodax('dump buy')
                sell=IndodaxSettingApp.control_indodax('sell')
                control_fibonanci_buy=IndodaxSettingApp.control_indodax('fibonanci buy')
                nt=IndodaxSettingApp.control_indodax('windows not sleep')
                
                #MELAKUKAN INISIALISASI OS WINDOWS ATAU LINUX
                if(nt['status']=='active'):
                    print("===============================================")
                    print("windows di setting tidak sleep")
                    osSleep = WindowsInhibitor()
                    osSleep.inhibit()
                else:
                    print("===============================================")
                    print("Berjalan di os selain windows")
                
                #MELAKUKAN BATASAN PROGRAM BERHENTI JIKA BTC DI BAWAH HARGA YG KITA SETT
                if(parameter_dum_btc<harga_btc):

                    #FUNGSI MEMBELI COIN DI HARGA DUMB DI BAWAH SUPORT
                    if(control_dumb_buy['status']=='active'):
                        print("")
                        print("===============================================")
                        print("menjalankan program dump atau harga dibawah suport buy")
                        strategi_dump_buy()

                        if(nt['status']=='active'):
                            #clear layar perintah windows
                            os.system("cls")
                        else:
                            #clear layar perintah linux
                            os.system("clear")

                        time.sleep(5)
                    else:
                        print("")
                        print("dumb buy tidak active")

                    #MELAKUKAN FUNGSI BELI FIBONANCI
                    if(control_fibonanci_buy['status']=='active'):
                        print("")
                        print("===============================================")
                        print("menjalankan strategi fibonanci buy")
                        fibonanci_action_beli()
                        if(nt['status']=='active'):
                            #clear layar perintah windows
                            os.system("cls")
                        else:
                            #clear layar perintah linux
                            os.system("clear")
                        time.sleep(5)
                    else:
                        print("")
                        print("fibonanci buy tidak active")

                else:
                    print("")
                    print("===============================================")
                    print("program beli crypto tidak dijalankan harga btc lebih rendah dari parameter yang di setting")

                #MELAKUKAN FUNGSI FIBONANCI SELL
                if(sell['status']=='active'):
                    print("")
                    print("===============================================")
                    print("menjalankan program fibonanci sell")
                    sell_all()
                    if(nt['status']=='active'):
                            #clear layar perintah windows
                            os.system("cls")
                    else:
                            #clear layar perintah linux
                            os.system("clear")
                    time.sleep(5)
                else:
                        print("")
                        print("fibonanci sell tidak active")

                #MELAKUKAN FUNGSI AUTO SELL
                if(auto_sell['status']=='active'):
                    print("")
                    print("===============================================")
                    simple_sell=float(view_coin_jumlah())
                    simple_sell_web=IndodaxSettingApp.indodax_simple_sell()
                    print('Target Jual =',simple_sell_web['auto_sell'])
                    print('Nilai Asset Sekarang =',simple_sell)
                    print("")
                    print("===============================================")
                    if(float(simple_sell)>float(simple_sell_web['auto_sell'])):
                        jual_semua_asset()
                        update_data()
                        update_strategi_reset()
                        update_dump_reset()
                        time.sleep(5)
                        print("Asset Terjual & Semua Data Di Riset")
                    else:
                        print("Asset Belum Terjual, Belum Masuk Target Jual")
                        time.sleep(5)

                    if(nt['status']=='active'):
                            #clear layar perintah windows
                            os.system("cls")
                    else:
                            #clear layar perintah linux
                            os.system("clear")
                else:
                        print("")
                        print("simple sell tidak active")
           
        else:
            print("")
            print("===============================================")          
            print("app indodax off silahkan onkan agar program berjalan")
   
if __name__ == "__main__":
      main()