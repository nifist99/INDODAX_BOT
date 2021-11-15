from api.web import tanlalana,tanlalana_fungsi
from api.public import indodax
from config import setting
from api.private import private_api
import time
from view.table import view_table


def strategi_manual(id_users):
            NewTanlalana=tanlalana
            Setting=setting(id_users)
            data=private_api(Setting.apikey(),Setting.screetkey())
            list=NewTanlalana.list_manual_active(id_users)
            get_spesific=data.get_info()

        #membuat info uang jadi int
            balance_idr=float(get_spesific['return']['balance']['idr'])

            print("[NAMA] :",get_spesific['return']['name'])
            print("[MONEY BALANCE] :",balance_idr)
            print("")
            print("===============================================")
            print("[START PROGRAM MANUAL BUY]")
            for f in list:
                if(f['status_manual']=='active'):
                #mengetahui harga sekarang
                    jam=time.strftime("%H:%M:%S", time.localtime())
                    NewIndodax=indodax(f['coin'])
                    result=NewIndodax.api_ticker_detail()
                    harga_buy=float(result['ticker']['sell'])
                    
                    autobuy=NewTanlalana.list_manual_strategi(f['id'])
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

                                            NewTanlalana.trade_run_add('manual',f['id_users'],f['id'],harga_buy,buy,auto['keuntungan'],'sell',cek_buy['return'][re+trade_c],cek_buy['return']['spend_rp'],cek_buy['return']['fee'],cek_buy['return']['remain_rp'],cek_buy['return']['order_id'])

                                            NewTanlalana.history_trade_add(f['coin'],f['id_users'],"buy",harga_buy,auto['id_coin'],buy,0,cek_buy['return'][re+trade_c],cek_buy['return']['spend_rp'],cek_buy['return']['fee'],cek_buy['return']['remain_rp'],cek_buy['return']['order_id'])

                                            #update parameter strategi jadi sell
                                            NewTanlalana.update_manual_strategi(auto['id'],auto['id_coin'],'sell',harga_buy)

                                            view_table(jam,f['coin'],"SUCCESS BUY",auto['harga_buy'],buy,harga_buy)
                                        else:
                                            view_table(jam,f['coin'],"CANCEL BUY",auto['harga_buy'],buy,harga_buy)
                                            data.cancel_order_buy(f['trade_parameter'],cek_buy['return']['order_id'])
                                        
                                    else:
                                        view_table(jam,f['coin'],"FAILED MONEY NOT ENAUGH",auto['harga_buy'],auto['idr'],harga_buy)
                                else:
                                    view_table(jam,f['coin'],"PRICE STRATEGI NOT PASS",auto['harga_buy'],auto['idr'],harga_buy)
                            
                            else:
                               view_table(jam,f['coin'],"ERROR PLEASE CHECK PARAMETER WEB",auto['harga_buy'],auto['idr'],harga_buy) 

                        else:
                            view_table(jam,f['coin'],"FINISH BUY",auto['harga_buy'],auto['idr'],harga_buy)

                else:
                    view_table(jam,f['coin'],"MANUAL BUY NOT ACTIVE",auto['harga_buy'],auto['idr'],harga_buy)

                print("")
                print("[",jam,"]","[FINISH LOOP MANUAL BUY]","[COIN :",f['coin']," ]")
                print("")

