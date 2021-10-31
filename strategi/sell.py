from api.web import tanlalana,tanlalana_fungsi
from api.public import indodax
from config import setting
from api.private import private_api
import time

def sell_all():
            NewTanlalana=tanlalana
            data=private_api(setting.apikey(),setting.screetkey())
            list=NewTanlalana.list_trade_run_sell()
            get_spesific=data.get_info()

            print("nama =",get_spesific['return']['name'])
            print("uang di aplikasi indodax =",get_spesific['return']['balance']['idr'])

            for f in list:
                if(f['status']=='sell'):
                        detail=NewTanlalana.get_data_from_server(f['coin'])
                        #mengetahui harga sekarang
                        NewIndodax=indodax(f['coin'])
                        result=NewIndodax.api_ticker_detail()
                        harga_sell=float(result['ticker']['buy'])
                        
                        print("")
                        print("===============================================")
                        print("memulai program screeneing sell coin =",f['coin'])
                        
                        keuntungan=float(f['keuntungan']*f['harga_buy']/100)
                        harga_target_jual=float(f['harga_buy']+keuntungan)
                        print("Harga Sekarang :",harga_sell)
                        print("Target Jual :",harga_target_jual)
                        if(harga_sell>=harga_target_jual):
                                if(f['status'] == 'sell'):
                                    cek_sell=data.trade_sell(detail['data']['trade_parameter'],harga_sell,f['receive_coin'])
                                    #add history trade
                                    sold='sold_'+detail['data']['trade_parameter']
                                    receive='receive_rp'
                                    remain='remain_'+detail['data']['trade_parameter']
      
                                    NewTanlalana.history_trade_add(f['coin'],f['id_users'],"sell",harga_sell,f['id_coin'],receive,1,cek_sell['return'][sold],cek_sell['return'][receive],cek_sell['return']['fee'],cek_sell['return'][receive],cek_sell['return']['order_id'])                               
                                        #update strategi indodax
                                    NewTanlalana.update_tanlalana_auto_buy_sell(f['id'],f['id_coin'],'finish',harga_sell)

                                    NewTanlalana.update_trade_run(f['id'],'finish')
                                        
                                    print("coin =",f['coin'])
                                    print("terjual di harga =",harga_sell)
                                    print("Eksekusi Jam :",time.strftime("%H:%M:%S", time.localtime()))
                                    print("")

                                else:
                                    print("===============================================")
                                    print("coin belum terjual, harga saat ini =",harga_sell)
                                    print("target jual =",harga_target_jual)
                                    print("Eksekusi Jam :",time.strftime("%H:%M:%S", time.localtime()))
                                    print("")
                        else:
                                print("harga belum sesui target")
                                print("Eksekusi Jam :",time.strftime("%H:%M:%S", time.localtime()))
                                print("")
                else:
                    print("")
                    print("===============================================")
                    print("coin=",f['coin'])
                    print("status coin =",f['status_dump'])
                    print("Eksekusi Jam :",time.strftime("%H:%M:%S", time.localtime()))
                    print("")

                print("")
                print("selesai melakukan secrening dump sell.............")
                print("Eksekusi Jam :",time.strftime("%H:%M:%S", time.localtime()))
