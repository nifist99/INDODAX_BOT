from api.web import tanlalana,tanlalana_fungsi
from api.public import indodax
from config import setting
from api.private import private_api
import time


def strategi_dump_buy():
            NewTanlalana=tanlalana
            data=private_api(setting.apikey(),setting.screetkey())
            list=NewTanlalana.list_data_server_active()
            get_spesific=data.get_info()

        #membuat info uang jadi int
            balance_idr=float(get_spesific['return']['balance']['idr'])

            print("[NAMA] :",get_spesific['return']['name'])
            print("[MONEY BALANCE] :",balance_idr)
            print("")
            print("===============================================")
            print("[START PROGRAM DUMP BUY]")
            for f in list:
                if(f['status_dump']=='active'):
                #mengetahui harga sekarang
                    jam=time.strftime("%H:%M:%S", time.localtime())
                    NewIndodax=indodax(f['coin'])
                    result=NewIndodax.api_ticker_detail()
                    harga_buy=float(result['ticker']['sell'])
                    
                    autobuy=NewTanlalana.list_tanlalana_auto_buy_sell(f['id'])
                    for auto in autobuy:
                        if(auto['status']=='buy'):
                            if(auto['harga_buy']!=0):
                                if(harga_buy<=auto['harga_buy']):
                                    if(balance_idr>=auto['idr']):
                                        buy=auto['idr']
                                        # data.trade_buy('zil',harga_buy,buy)
                                        cek_buy=data.trade_buy(f['trade_parameter'],harga_buy,buy)

                                        #melakukan cek coin terbeli atau faild
                                        if(cek_buy['success']==1):
                                        #add history trade
                                            re='receive_'
                                            trade_c=f['trade_parameter']

                                            NewTanlalana.trade_run_add('dump',f['id_users'],f['id'],harga_buy,buy,auto['keuntungan'],'sell',cek_buy['return'][re+trade_c],cek_buy['return']['spend_rp'],cek_buy['return']['fee'],cek_buy['return']['remain_rp'],cek_buy['return']['order_id'])

                                            NewTanlalana.history_trade_add(f['coin'],f['id_users'],"buy",harga_buy,auto['id_coin'],buy,0,cek_buy['return'][re+trade_c],cek_buy['return']['spend_rp'],cek_buy['return']['fee'],cek_buy['return']['remain_rp'],cek_buy['return']['order_id'])

                                            #update parameter strategi jadi sell
                                            NewTanlalana.update_tanlalana_auto_buy_sell(auto['id'],auto['id_coin'],'sell',harga_buy)

                                            print("[",jam,"]","[COIN :",f['coin']," ]",'[STATUS BUY : SUCCESS]','[PRICE]',' ',harga_buy,' ','[IDR]',' ',buy,' ','[PRICE TARGET]',auto['harga_buy'])
                                        else:
                                            print("[",jam,"]","[COIN :",f['coin']," ]",'[STATUS BUY : FAILED]','[PRICE]',' ',harga_buy,' ','[IDR]',' ',buy,' ','[PRICE TARGET]',auto['harga_buy'])
                                            data.cancel_order_buy(f['trade_parameter'],cek_buy['return']['order_id'])
                                        
                                    else:
                                        print("[",jam,"]","[COIN :",f['coin']," ]",'[STATUS BUY : FAILED MONEY NOT ENAUGH]','[PRICE]',' ',harga_buy,' ','[IDR]',' ',auto['idr'],' ','[PRICE TARGET]',auto['harga_buy'])
                                else:
                                    print("[",jam,"]","[COIN :",f['coin']," ]",'[STATUS BUY : PRICE STRATEGI NOT PASS]','[PRICE]',' ',harga_buy,' ','[IDR]',' ',auto['idr'],' ','[PRICE TARGET]',auto['harga_buy'])
                            
                            else:
                               print("[",jam,"]","[COIN :",f['coin']," ]",'[STATUS BUY : PLEASE CHECK PRICE IN WEB NOT DETECT]','[PRICE]',' ',harga_buy,' ','[IDR]',' ',auto['idr'],' ','[PRICE TARGET]',auto['harga_buy']) 

                        else:
                            print("[",jam,"]","[COIN :",f['coin']," ]",'[STATUS BUY : FINISH COIN BUY]','[PRICE]',' ',auto['harga_buy'],' ','[IDR]',' ',auto['idr'],' ','[PRICE TARGET]',auto['harga_buy'])

                else:
                    print("[",jam,"]","[COIN :",f['coin']," ]",'[STATUS BUY : DUMP NOT ACTIVE]','[PRICE]',' ',harga_buy,' ','[IDR]',' ',auto['idr'],' ','[PRICE TARGET]',auto['harga_buy'])

                print("")
                print("[",jam,"]","[FINISH LOOP DUMP BUY]","[COIN :",f['coin']," ]")
                print("")

