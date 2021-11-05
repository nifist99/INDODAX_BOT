from strategi.dump import strategi_dump_buy
from api.web import tanlalana,tanlalana_fungsi
from api.public import indodax 
from strategi.fibo import fibonanci
from strategi.sell import sell_all
from strategi.manual import strategi_manual
from config import WindowsInhibitor
from api.private import private_api
import time
import os
from config import setting
from countdown import countdown
from fungsi.fungsiSell import sell_all_manual,total_asset



def bot(id_users):
        #cekk setting app
        #cek btc indodax menghindari dumb
        NewBtc=indodax("btc")
        status_btc=NewBtc.api_detail_btc()
        harga_btc=float(status_btc['ticker']['buy'])

        #cekk setting app
        IndodaxSettingApp=tanlalana
        dum_btc=IndodaxSettingApp.indodax_setting("btc",id_users)
        # status_app=IndodaxSettingApp.indodax_setting("status")

        parameter_dum_btc=float(dum_btc['parameter_int'])
        osSleep = None

        status_app= IndodaxSettingApp.control_indodax('trading indodax',id_users)

        #in Windows, prevent the OS from sleeping while we run
        if(status_app['status']=='active'):
            print("")
            print("===============================================")          
            print("[APP BOT INDODAX ON]")
            while True:
                delay_program=dum_btc=IndodaxSettingApp.indodax_setting('delay',id_users)
                auto_sell= IndodaxSettingApp.control_indodax('simple sell',id_users)
                control_dumb_buy= IndodaxSettingApp.control_indodax('dump buy',id_users)
                manual_buy= IndodaxSettingApp.control_indodax('manual buy',id_users)
                sell=IndodaxSettingApp.control_indodax('sell',id_users)
                control_fibonanci_buy=IndodaxSettingApp.control_indodax('fibonanci buy',id_users)
                nt=IndodaxSettingApp.control_indodax('windows not sleep',id_users)
                
                #MELAKUKAN INISIALISASI OS WINDOWS ATAU LINUX
                if(nt['status']=='active'):
                    print("===============================================")
                    print("[WINDOWS NOT SLEEP]")
                    osSleep = WindowsInhibitor()
                    osSleep.inhibit()
                else:
                    print("===============================================")
                    print("[RUN IN ANOTHER OS]")
                
                #MELAKUKAN BATASAN PROGRAM BERHENTI JIKA BTC DI BAWAH HARGA YG KITA SETT
                if(parameter_dum_btc<harga_btc):

                    #FUNGSI MEMBELI COIN DI HARGA DUMB DI BAWAH SUPORT
                    if(control_dumb_buy['status']=='active'):
                        strategi_dump_buy(id_users)

                        if(nt['status']=='active'):
                            #clear layar perintah windows
                            os.system("cls")
                        else:
                            #clear layar perintah linux
                            os.system("clear")

                        time.sleep(5)
                    else:
                        print("")
                        print("[CONTROL INDODAX DUMB BUY NOT ACTIVE]")

                    #MELAKUKAN FUNGSI BELI FIBONANCI
                    if(control_fibonanci_buy['status']=='active'):
                        fibonanci(id_users)
                        if(nt['status']=='active'):
                            #clear layar perintah windows
                            os.system("cls")
                        else:
                            #clear layar perintah linux
                            os.system("clear")
                        time.sleep(5)
                    else:
                        print("")
                        print("[CONTROL INDODAX FIBONANCI BUY NOT ACTIVE]")

                    if(manual_buy['status']=='active'):
                        strategi_manual(id_users)
                        if(nt['status']=='active'):
                            #clear layar perintah windows
                            os.system("cls")
                        else:
                            #clear layar perintah linux
                            os.system("clear")
                        time.sleep(5)
                    else:
                        print("")
                        print("[CONTROL INDODAX MANUAL BUY NOT ACTIVE]")

                else:
                    print("")
                    print("[BTC DUMP PROGRAM NOT RUN]")

                #MELAKUKAN FUNGSI FIBONANCI SELL
                if(sell['status']=='active'):
                    sell_all(id_users)
                    if(nt['status']=='active'):
                            #clear layar perintah windows
                            os.system("cls")
                    else:
                            #clear layar perintah linux
                            os.system("clear")
                    time.sleep(5)
                else:
                        print("")
                        print("[CONTROL INDODAX SELL COIN NOT ACTIVE]")

                #MELAKUKAN FUNGSI AUTO SELL
                if(auto_sell['status']=='active'):
                    print("")
                    print("===============================================")
                    simple_sell=float(total_asset())
                    simple_sell_web=IndodaxSettingApp.indodax_simple_sell()
                    print('[TARGET SELL] :',simple_sell_web['auto_sell'])
                    print('[PRICE INDODAX NOW] :',simple_sell)
                    print("")
                    print("===============================================")
                    if(float(simple_sell)>float(simple_sell_web['auto_sell'])):
                        sell_all_manual()
                        time.sleep(5)
                        print("[FINISH TO SELL ALL COIN PARAMETER ALL UPDATE]")
                    else:
                        print("[PRICE NOT PASS STRATEGI]")
                        time.sleep(5)

                    if(nt['status']=='active'):
                            #clear layar perintah windows
                            os.system("cls")
                    else:
                            #clear layar perintah linux
                            os.system("clear")
                else:
                        print("")
                        print("[CONTROL INDODAX SIMPLE SELL NOT ACTIVE]")

                if(delay_program['parameter_int']!=0):
                    menit=int(delay_program['parameter_int']*60)
                    print("Eksekusi Jam :",time.strftime("%H:%M:%S", time.localtime()))
                    print("DELAY PROGRAM :",delay_program['parameter_int']," MENIT............")
                    countdown(menit)
                    # time.sleep(menit)
                else:
                        print("")
                        print("[DELAY PROGRAM NOT ACTIVE]")
           
        else:
            print("")
            print("===============================================")          
            print("[APP INDODAX OFF]")
   