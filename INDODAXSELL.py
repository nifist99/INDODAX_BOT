from api.private import private_api
from config import setting
from api.web import tanlalana
from api.public import indodax
import time
from view.table import view_table

def jual_semua_asset(id_users): 
            Setting=setting(id_users)
            data=private_api(Setting.apikey(),Setting.screetkey())
            NewTanlalana=tanlalana
            list=NewTanlalana.list_data_server_active(id_users)
            list_coin=data.get_info()  
            for f in list:
                jumlah_coin=float(list_coin['return']['balance'][f['trade_parameter']])
                if(jumlah_coin != 0):
                    NewIndodax=indodax(f['coin'])

                    #ambil data dari server indodax
                    result=NewIndodax.api_ticker_detail()
                    coin=float(list_coin['return']['balance'][f['trade_parameter']])

                    #strategi fibonanci harga sell server indodax
                    harga_sell=float(result['ticker']['buy'])

                    print(f['trade_parameter'])
                    print(list_coin['return']['balance'][f['trade_parameter']])

                    cek_sell=data.trade_sell(f['trade_parameter'],harga_sell,list_coin['return']['balance'][f['trade_parameter']])
                    sold='sold_'+f['trade_parameter']
                    receive='receive_rp'
                    remain='remain_'+f['trade_parameter']
                    if(cek_sell['success']==1):
                        NewTanlalana.history_trade_add(f['coin'],f['id_users'],"sell",harga_sell,f['id'],receive,1,cek_sell['return'][sold],cek_sell['return'][receive],cek_sell['return']['fee'],cek_sell['return'][receive],cek_sell['return']['order_id'])                                                                       
                        print("coin =",f['coin'])
                        print("terjual di harga =",harga_sell)
                        print("Eksekusi Jam :",time.strftime("%H:%M:%S", time.localtime()))
                        print("")

            NewTanlalana.update_all_trade_run()
            print("")
            print("coin sudah terjual semua")

def view_coin_jumlah(id_users):
            
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

def single_coin(id_users,order_id):
            
                Setting=setting(id_users)
                data=private_api(Setting.apikey(),Setting.screetkey())
                NewTanlalana=tanlalana
                list_coin=data.get_info()
                hasil=NewTanlalana.trade_run_detail(id_users,order_id)
                f=hasil['data']
                jumlah_coin=float(list_coin['return']['balance'][f['trade_parameter']])
                if(jumlah_coin != 0):
                    NewIndodax=indodax(f['coin'])

                    #ambil data dari server indodax
                    result=NewIndodax.api_ticker_detail()
                    coin=float(list_coin['return']['balance'][f['trade_parameter']])

                    #strategi fibonanci harga sell server indodax
                    harga_sell=float(result['ticker']['buy'])

                    total_idr=coin*harga_sell
                    print(f['trade_parameter'])
                    print(list_coin['return']['balance'][f['trade_parameter']])

                    cek_sell=data.trade_sell(f['trade_parameter'],harga_sell,list_coin['return']['balance'][f['trade_parameter']])
                                    #add history trade
                    sold='sold_'+f['trade_parameter']
                    receive='receive_rp'
                    remain='remain_'+f['trade_parameter']
                    NewTanlalana.history_trade_add(f['coin'],f['id_users'],"sell",harga_sell,f['id_coin'],receive,1,cek_sell['return'][sold],cek_sell['return'][receive],cek_sell['return']['fee'],cek_sell['return'][receive],cek_sell['return']['order_id'])                                                                           
                    print("coin =",f['coin'])
                    print("terjual di harga =",harga_sell)
                    print("Eksekusi Jam :",time.strftime("%H:%M:%S", time.localtime()))
                    print("")
  
                    print("Terjual dengan harga total =",total_idr)
                    print("")

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
                    print("")

            print(round(tambah,2))

def trade_run(id_users):
            NewTanlalana=tanlalana
            Setting=setting(id_users)
            data=private_api(Setting.apikey(),Setting.screetkey())
            list=NewTanlalana.list_trade_run_sell(id_users)
            get_spesific=data.get_info()

            balance_idr=float(get_spesific['return']['balance']['idr'])
            print("[NAMA] :",get_spesific['return']['name'])
            print("[MONEY BALANCE] :",get_spesific['return']['balance']['idr'])
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
                        keuntungan=float(f['keuntungan']*f['harga_buy']/100)
                        harga_target_jual=float(f['harga_buy']+keuntungan)
                        
                        jam=time.strftime("%H:%M:%S", time.localtime())
                        view_table(jam,f['coin'],"SUCCESS",harga_target_jual,f['harga'],harga_sell)
                


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
        jual_semua_asset(id_users)
   elif(nama==2):
     trade_run(id_users)
     crypto=str(input("ketikan coin yang akan dijual contoh [zilidr] = "))
     single_coin(crypto,id_users)   
   else:
       quit()

