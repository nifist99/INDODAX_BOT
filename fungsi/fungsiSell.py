import os
from api.web import tanlalana,tanlalana_fungsi
from api.public import indodax
from config import setting
from api.private import private_api
import time
from view.table import view_table

def sell_all_manual(id_users):
            NewTanlalana=tanlalana
            Setting=setting(id_users)
            data=private_api(Setting.apikey(),Setting.screetkey())
            list=NewTanlalana.list_trade_run_sell(id_users)
            get_spesific=data.get_info()

            print("[NAMA] :",get_spesific['return']['name'])
            print("[MONEY BALANCE] :",get_spesific['return']['balance']['idr'])
            print("[TOTAL ASSET : ]",total_asset(id_users))
            print("")
            print("===============================================")
            print("[START PROGRAM SELL COIN]")

            for f in list:
                if(f['status']=='sell'):
                        detail=NewTanlalana.get_data_from_server(f['coin'])
                        #mengetahui harga sekarang
                        NewIndodax=indodax(f['coin'])
                        result=NewIndodax.api_ticker_detail()
                        harga_sell=float(result['ticker']['buy'])
                        
                        jam=time.strftime("%H:%M:%S", time.localtime())

                        data.trade_sell(detail['data']['trade_parameter'],harga_sell,f['receive_coin'])
                                    #add history trade
                        receive=harga_sell*f['receive_coin']
      
                        NewTanlalana.history_trade_add(f['coin'],f['id_users'],"sell",harga_sell,f['id_coin'],receive,1,f['receive_coin'],0,f['fee'],0,f['order_id'])                               
                                        #update strategi indodax
                        NewTanlalana.update_tanlalana_auto_buy_sell(f['id'],f['id_coin'],'finish',harga_sell)

                        NewTanlalana.update_trade_run(f['id'],'finish')
                                        
                        view_table(jam,f['coin'],"SUCCESS",harga_sell,f['harga'],harga_sell)
  
                        
                else:
                    view_table(jam,f['coin'],"CEK STATUS WEB",harga_sell,f['harga'],harga_sell)

            print("")
            print("[",jam,"]","[FINISH LOOP SELL]")
            print("")

def single_coin(id_users,order_id):
            
                Setting=setting(id_users)
                data=private_api(Setting.apikey(),Setting.screetkey())
                NewTanlalana=tanlalana
                get_spesific=data.get_info()
                hasil=NewTanlalana.trade_run_detail(id_users,order_id)
                f=hasil['data']

                print("[NAMA] :",get_spesific['return']['name'])
                print("[MONEY BALANCE] :",get_spesific['return']['balance']['idr'])
                print("[TOTAL ASSET : ]",total_asset(id_users))
                print("")
                print("===============================================")
                print("[START PROGRAM SELL COIN]")
                detail=NewTanlalana.get_data_from_server(f['coin'])
                        #mengetahui harga sekarang
                NewIndodax=indodax(f['coin'])
                result=NewIndodax.api_ticker_detail()
                harga_sell=float(result['ticker']['buy'])
                        
                jam=time.strftime("%H:%M:%S", time.localtime())

                if(f['status']=='sell'):

                        data.trade_sell(detail['data']['trade_parameter'],harga_sell,f['receive_coin'])
                                    #add history trade
                        receive=harga_sell*f['receive_coin']
      
                        NewTanlalana.history_trade_add(f['coin'],f['id_users'],"sell",harga_sell,f['id_coin'],receive,1,f['receive_coin'],0,f['fee'],0,f['order_id'])                               
                                        #update strategi indodax
                        NewTanlalana.update_tanlalana_auto_buy_sell(f['id'],f['id_coin'],'finish',harga_sell)

                        NewTanlalana.update_trade_run(f['id'],'finish')
                                        
                        view_table(jam,f['coin'],"SUCCESS",harga_sell,f['harga'],harga_sell)
  
                        
                else:
                    view_table(jam,f['coin'],"CEK STATUS WEB",harga_sell,f['harga'],harga_sell)


def total_asset(id_users):
            
            Setting=setting(id_users)
            data=private_api(Setting.apikey(),Setting.screetkey())
            NewTanlalana=tanlalana
            list=NewTanlalana.list_data_server_active(id_users)
            list_coin=data.get_info()

            print("=====================================")
            print("Menjalankan Simple Sell")
            print("")

            tambah=0
            for f in list:
                jumlah_coin=float(list_coin['return']['balance'][f['trade_parameter']])
                if(jumlah_coin != 0):
                    NewIndodax=indodax(f['coin'])

                    #ambil data dari server indodax
                    result=NewIndodax.api_ticker_detail()
                    coin=float(list_coin['return']['balance'][f['trade_parameter']])

                    #strategi fibonanci harga sell server indodax
                    harga_sell=float(result['ticker']['buy'])

                    total_idr=coin*harga_sell

                    tambah +=total_idr

            return round(tambah,2) 

def view_coin(id_users):
            Setting=setting(id_users)
            data=private_api(Setting.apikey(),Setting.screetkey())
            NewTanlalana=tanlalana
            list=NewTanlalana.list_data_server_active(id_users)
            list_coin=data.get_info()

            print("=====================================")
            print("ASSET COIN YANG DIMILIKI DI INDODAX")
            print("")

            tambah=0
            for f in list:
                jumlah_coin=float(list_coin['return']['balance'][f['trade_parameter']])
                if(jumlah_coin != 0):
                    NewIndodax=indodax(f['coin'])

                    #ambil data dari server indodax
                    result=NewIndodax.api_ticker_detail()
                    coin=float(list_coin['return']['balance'][f['trade_parameter']])

                    #strategi fibonanci harga sell server indodax
                    harga_sell=float(result['ticker']['buy'])

                    total_idr=coin*harga_sell

                    tambah +=total_idr

                    print(f['trade_parameter'],'=',list_coin['return']['balance'][f['trade_parameter']])
                    print('Rp.',round(total_idr,2))
                    print("")


def INDODAXSELL(id_users):
   print("==============================================")
   print("ini adalah app penjualan semua coin")
   print("")
   view_coin(id_users)
   print("ketik [1] untuk menjual semua coin di indodax")
   print("ketik [2] untuk menjual 1 coin di indodax")
   print("")
   nama=int(input("silahkan pilih perintah yang akan di jalankan = "))
   if(nama==1):
        sell_all_manual(id_users)
        lanjut=str(input("masukan Y/y untuk melanjutkan :"))
        if(lanjut=="y" or lanjut=="Y"):
            os.system("cls")
            INDODAXSELL(id_users)
   elif(nama==2):
     order_id=str(input("ketikan order_id cek di menu web [trade run] = "))
     single_coin(id_users,order_id) 
     lanjut=str(input("masukan Y/y untuk melanjutkan :"))
     if(lanjut=="y" or lanjut=="Y"):
            os.system("cls")
            INDODAXSELL(id_users)  
   else:
       quit()
