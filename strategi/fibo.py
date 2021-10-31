from api.web import tanlalana,tanlalana_fungsi
from api.public import indodax
from config import setting
from api.private import private_api
import time

class strategi:
    def __init__(self,suport, resisten,angka_fibo):
    #key dari indodax
        self.suport = suport
        self.resisten= resisten
        self.angka_fibo=angka_fibo

    def fibonanci(self):
        #mencari total kenaikan resisten dan suport
        self.value=self.resisten-self.suport

        #mencari nilai vibonanci rupiah dalam kenaikan
        self.value_fibonanci=(self.value*self.angka_fibo)/100
        
        #mencari penurunan harga dalam fibonanci untuk parameter buy resisten - fibo
        self.result_fibo=self.resisten-self.value_fibonanci

        return self.result_fibo

class fungsi_strategi_fibo:

    def __init__(self,crypto):
    #coin active dari screening server tanlalana
        self.crypto = crypto

    def fibonanci(self):
            print("")
            print("==================================")
            print("menjalankan strategi fibonanci buy")
            print("")
            NewTanlalana=tanlalana
            data=private_api(setting.apikey(),setting.screetkey())
            get_spesific=data.get_info()

            balance_idr=float(get_spesific['return']['balance']['idr'])

            NewIndodax=indodax(self.crypto)
            result=NewIndodax.api_ticker_detail()
            detail=NewTanlalana.get_data_from_server(self.crypto)
                
            harga_buy=float(result['ticker']['sell'])            
            suport=int(detail['data']['suport'])
            resisten=int(detail['data']['resisten'])

            list_strategi=tanlalana.list_strategi_fibonanci(detail['data']['id'])

            for n in list_strategi:
                    NewStrategi=strategi(suport,resisten,n['angka_fibo'])
                    starategi_result=NewStrategi.fibonanci()
                    harga_beli_fibo=starategi_result
                    print("")
                    print("===============================================")
                    print("Harga Beli :",harga_buy)
                    print("Target Beli :",harga_beli_fibo)
                    if(harga_buy<=harga_beli_fibo):
                        if(n['status'] == 'buy'):
                            if(balance_idr>=n['idr']):
                                # buy=uang*30/100
                                print("")
                                print("===============================================")
                                print("coin :",self.crypto)
                                print("sedang melakukan pembelian di....",n['strategi'])
                                buy=n['idr']
                                # data.trade_buy('zil',harga_buy,buy)
                                cek_buy=data.trade_buy(detail['data']['trade_parameter'],harga_buy,buy)
                                #add history trade
                                if(cek_buy['success']==1):
                                    re='receive_'
                                    trade_c=detail['data']['trade_parameter']

                                    NewTanlalana.trade_run_add(n['strategi'],detail['data']['id_users'],detail['data']['id'],harga_buy,buy,n['keuntungan'],'sell',cek_buy['return'][re+trade_c],cek_buy['return']['spend_rp'],cek_buy['return']['fee'],cek_buy['return']['remain_rp'],cek_buy['return']['order_id'])
                                    NewTanlalana.history_trade_add(self.crypto,detail['data']['id_users'],"buy",harga_buy,n['id_coin'],buy,0,cek_buy['return'][re+trade_c],cek_buy['return']['spend_rp'],cek_buy['return']['fee'],cek_buy['return']['remain_rp'],cek_buy['return']['order_id'])

                                    #update strategi indodax
                                    tanlalana_fungsi.update_data_strategi(n['strategi'],detail['data']['id'],harga_buy,buy,"sell",n['id'])
                                    print("terbeli dengan harga",harga_buy)
                                    print("coin :",self.crypto)
                                    print("Eksekusi Jam :",time.strftime("%H:%M:%S", time.localtime()))
                                    print("")
                                else:
                                    print("coin :",self.crypto)
                                    print("gagal melakukan pembelian")
                                    data.cancel_order_buy(detail['data']['trade_parameter'],cek_buy['return']['order_id'])
                            else:
                                print("coin :",self.crypto)
                                print("uang indodax tidak cukup untuk membeli =",balance_idr)
                                print("Eksekusi Jam :",time.strftime("%H:%M:%S", time.localtime()))
                                print("")
                        else:
                            print("")
                            print("coin :",self.crypto)
                            print("===============================================")
                            print("sudah terbeli coin di",n['strategi'])
                            print("Eksekusi Jam :",time.strftime("%H:%M:%S", time.localtime()))
                            print("")
                    else:
                        print("")
                        print("coin :",self.crypto)
                        print("===============================================")
                        print("harga belum sesui setrategi fibo",n['strategi'])
                        print("Eksekusi Jam :",time.strftime("%H:%M:%S", time.localtime()))
                        print("")
                        