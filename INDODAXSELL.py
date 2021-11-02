from api.private import private_api
from config import setting
from api.web import tanlalana
from api.public import indodax
import time

def jual_semua_asset(): 
            data=private_api(setting.apikey(),setting.screetkey())
            NewTanlalana=tanlalana
            list=NewTanlalana.list_data_server_active()
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
                        NewTanlalana.history_trade_add(f['coin'],f['id_users'],"sell",harga_sell,f['id_coin'],receive,1,cek_sell['return'][sold],cek_sell['return'][receive],cek_sell['return']['fee'],cek_sell['return'][receive],cek_sell['return']['order_id'])                                                                       
                        print("coin =",f['coin'])
                        print("terjual di harga =",harga_sell)
                        print("Eksekusi Jam :",time.strftime("%H:%M:%S", time.localtime()))
                        print("")
                    else:
                        print("gagal melakukan pembelian")
                        data.cancel_order_sell(f['trade_parameter'],cek_sell['return']['order_id'])

            NewTanlalana.update_all_trade_run()
            print("")
            print("coin sudah terjual semua")

def view_coin_jumlah():
            
            data=private_api(setting.apikey(),setting.screetkey())
            NewTanlalana=tanlalana
            list=NewTanlalana.list_data_server_active()
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

def single_coin(crypto):
            
                data=private_api(setting.apikey(),setting.screetkey())
                NewTanlalana=tanlalana
                list_coin=data.get_info()
                hasil=NewTanlalana.get_data_from_server(crypto)
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
                    if(cek_sell['success']==1):
                        NewTanlalana.history_trade_add(f['coin'],f['id_users'],"sell",harga_sell,f['id_coin'],receive,1,cek_sell['return'][sold],cek_sell['return'][receive],cek_sell['return']['fee'],cek_sell['return'][receive],cek_sell['return']['order_id'])                                                                           
                        print("coin =",f['coin'])
                        print("terjual di harga =",harga_sell)
                        print("Eksekusi Jam :",time.strftime("%H:%M:%S", time.localtime()))
                        print("")
                    else:
                            print("gagal melakukan pembelian")
                            data.cancel_order_sell(f['trade_parameter'],cek_sell['return']['order_id'])
                    print("Terjual dengan harga total =",total_idr)
                    print("")

def view_coin():
            
            data=private_api(setting.apikey(),setting.screetkey())
            NewTanlalana=tanlalana
            list=NewTanlalana.list_data_server_active()
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

def INDODAXSELL():
   print("==============================================")
   print("ini adalah app penjualan semua coin")
   print("")
   view_coin()
   print("ketik [1] untuk menjual semua coin di indodax")
   print("ketik [2] untuk menjual 1 coin di indodax")
   print("")
   nama=int(input("silahkan pilih perintah yang akan di jalankan = "))
   if(nama==1):
        jual_semua_asset()
   elif(nama==2):
     crypto=str(input("ketikan coin yang akan dijual contoh [zilidr] = "))
     single_coin(crypto)   
   else:
       quit()


# if __name__ == "__main__":
#       main()