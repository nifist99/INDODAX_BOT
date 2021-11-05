from api.web import tanlalana,tanlalana_fungsi
from api.public import indodax
from config import setting
from api.private import private_api
import time
from view.table import view_table

def sell_all(id_users):
            NewTanlalana=tanlalana
            Setting=setting(id_users)
            data=private_api(Setting.apikey(),Setting.screetkey())
            list=NewTanlalana.list_trade_run_sell(id_users)
            get_spesific=data.get_info()

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
                        
                        jam=time.strftime("%H:%M:%S", time.localtime())
                        keuntungan=float(f['keuntungan']*f['harga_buy']/100)
                        harga_target_jual=float(f['harga_buy']+keuntungan)
                        if(harga_sell>=harga_target_jual):
                            data.trade_sell(detail['data']['trade_parameter'],harga_sell,f['receive_coin'])

                            receive=harga_sell*f['receive_coin']
      
                            NewTanlalana.history_trade_add(f['coin'],f['id_users'],"sell",harga_sell,f['id_coin'],receive,1,f['receive_coin'],0,f['fee'],0,f['order_id'])                               
                                        #update strategi indodax
                            NewTanlalana.update_tanlalana_auto_buy_sell(f['id'],f['id_coin'],'finish',harga_sell)

                            NewTanlalana.update_trade_run(f['id'],'finish')
                                        
                            view_table(jam,f['coin'],"SUCCESS",harga_target_jual,f['harga'],harga_sell)
                        else:
                            view_table(jam,f['coin'],"PRICE STRATEGI NOT PASS",harga_target_jual,f['harga'],harga_sell)
                else:
                    view_table(jam,f['coin'],"CEK STATUS WEB",harga_target_jual,f['harga'],harga_sell)

            print("")
            print("[",jam,"]","[FINISH LOOP SELL]")
            print("")
