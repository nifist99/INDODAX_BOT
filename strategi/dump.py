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

            print("nama =",get_spesific['return']['name'])
            print("uang di aplikasi indodax =",get_spesific['return']['balance']['idr'])

            for f in list:
                if(f['status_dump']=='active'):
                #mengetahui harga sekarang
                    
                    NewIndodax=indodax(f['coin'])
                    result=NewIndodax.api_ticker_detail()
                    harga_buy=float(result['ticker']['sell'])
                    
                    print("")
                    print("===============================================")
                    print("memulai program dump buy =",f['coin'])
                    autobuy=NewTanlalana.list_tanlalana_auto_buy_sell(f['id'])
                    for auto in autobuy:
                        if(auto['status']=='buy'):
                            if(auto['harga_buy']!=0):
                                if(harga_buy<=auto['harga_buy']):
                                    if(balance_idr>=auto['idr']):
                                        print("")
                                        print("===============================================")
                                        print("sedang melakukan pembelian di harga =",harga_buy)
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

                                            print("terbeli dengan harga =",harga_buy)
                                            print("Eksekusi Jam :",time.strftime("%H:%M:%S", time.localtime()))
                                            print("")
                                        else:
                                            print("gagal melakukan pembelian")
                                            data.cancel_order_buy(f['trade_parameter'],cek_buy['return']['order_id'])
                                        
                                    else:
                                        print("sisa uang di aplikasi tidak cukup jumlah =",balance_idr)
                                        print("Eksekusi Jam :",time.strftime("%H:%M:%S", time.localtime()))
                                        print("")
                                else:
                                    print("===============================================")
                                    print("coin belum terbeli =",f['coin'])
                                    print("harga sekarang =",harga_buy)
                                    print("target beli =",auto['harga_buy'])
                                    print("Eksekusi Jam :",time.strftime("%H:%M:%S", time.localtime()))
                                    print("")
                            
                            else:
                               print("===============================================")
                               print("silahkan isikan posisi harga beli") 

                        else:
                            print("===============================================")
                            print("coin sudah terbeli =",auto['harga_buy'])

                else:
                    print("")
                    print("===============================================")
                    print("coin=",f['coin'])
                    print("status coin =",f['status_dump'])
                    print("Eksekusi Jam :",time.strftime("%H:%M:%S", time.localtime()))
                    print("")

                print("selesai melakukan screening crypto beli active")
                print("Eksekusi Jam :",time.strftime("%H:%M:%S", time.localtime()))
                print("")

