import time
import requests
from api.public import indodax


from requests_toolbelt import sessions
from requests.adapters import HTTPAdapter
from urllib3.util import Retry


retries = Retry(total=3, backoff_factor=0.3, status_forcelist=[500, 502, 504])
adapter = HTTPAdapter(max_retries=retries)

http = sessions.BaseUrlSession(base_url="https://tanlalana.com/api/")
http.mount("https://", adapter)
http.mount("http://", adapter)


class tanlalana:

    #MENAMBAHKAN HISTORI PEMBELIAN DAN PENJUALAN COIN
    def history_trade_add(coin,id_users,status,harga,id_coin,harga_total,read,receive_coin,spend_rp,fee,remain_rp,order_id):
        this_coin=coin
        this_status=status
        this_harga=harga
        this_id_users=id_users
        this_id_coin=id_coin
        this_harga_total=harga_total
        this_read=read
        this_receive_coin=receive_coin
        this_spend_rp=spend_rp
        this_fee=fee
        this_remain_rp=remain_rp
        this_order_id=order_id
        try:
            param={'coin':coin,'id_users':id_users,'status':status,'harga':harga,'id_coin':id_coin,'harga_total':harga_total,'read':read,'receive_coin':receive_coin,'spend_rp':spend_rp,'fee':fee,'remain_rp':remain_rp,'order_id':order_id}
            url="history_trade_add"
            r=http.post(url,data=param)
            result=r.json()
            return result
        except Exception:
                # sleep for a bit in case that helps
                time.sleep(2)
                # try again
                return tanlalana.history_trade_add(this_coin,this_id_users,this_status,this_harga,this_id_coin,this_harga_total,this_read,this_receive_coin,this_spend_rp,this_fee,this_remain_rp,this_order_id)
    # add data coin baru ke server


    #FUNGSI MENAMBAHKAN COIN BARU KE SERVER
    def add_data_to_server(coin,image,currency):
        this_coin=coin
        this_image=image
        this_currency=currency
        try:
            param={'coin':coin,'url_logo_png':image,'base_currency':currency}
            url="indodax_created"
            http.post(url,data=param)
        except Exception:
                # sleep for a bit in case that helps
                time.sleep(2)
                return tanlalana.add_data_to_server(this_coin,this_image,this_currency)


    # update data ke server coin 
    def update_data_to_server(coin,ticker_id):
        this_coin=coin
        this_ticker_id=ticker_id
        try:
            param={'coin':coin,'ticker_id':ticker_id,'status':'notactive'}
            url="indodax_update"
            http.post(url,data=param)

        except Exception:
                # sleep for a bit in case that helps
                time.sleep(2)
                return tanlalana.update_data_to_server(this_coin,this_ticker_id)    

    
    #  ini mengambil data dari server tanlalana / detail coin yang di pilih
    def get_data_from_server(coin):
        this_coin=coin
        try:
            param={'coin':coin}
            url="indodax_detail"
            r=http.post(url,data=param)
            data_trading=r.json()
            return data_trading
        except Exception:
                # sleep for a bit in case that helps
                time.sleep(2)
                return tanlalana.get_data_from_server(this_coin)

    #  fungsi yang digunakan untuk megapdate data suport dan resisten
    def update_suport_resisten_to_server(id_users,coin,suport,resisten,sell,buy):
        this_coin=coin
        this_suport=suport
        this_resisten=resisten
        this_sell=sell
        this_buy=buy
        this_id_users=id_users
        try:
            #melakukan jeda untuk memastikan koin terupdate
            time.sleep(2)
            param={'id_users':id_users,'coin':coin,'suport_update':suport,'resisten_update':resisten,'sell':sell,'buy':buy}
            url="indodax_update"
            r=http.post(url,data=param)
            respon=r.json()
            return respon
        except Exception:
                # sleep for a bit in case that helps
                time.sleep(2)
                return tanlalana.update_suport_resisten_to_server(this_id_users,this_coin,this_suport,this_resisten,this_sell,this_buy)
    
    # list data form server tanlalana
    def list_data_server():
        try:
            url="indodax_list"
            r=http.post(url)
            respon=r.json()
            global list_tanlalana
            list_tanlalana=respon['data']
            return list_tanlalana

        except Exception:
                # sleep for a bit in case that helps
                time.sleep(2)
                return tanlalana.list_data_server()

    def list_strategi_fibonanci(id_coin):
        this_id_coin=id_coin
        try:
            url="list_strategi_fibonanci"
            param={'id_coin':id_coin}
            r=http.post(url,data=param)
            respon=r.json()
            global list_strategi_fibonanci
            list_strategi_fibonanci=respon['data']
            return list_strategi_fibonanci

        except Exception:
                # sleep for a bit in case that helps
                time.sleep(2)
                return tanlalana.list_strategi_fibonanci(this_id_coin)
    
    #indodax coin active
    def list_data_server_active(id_users):
        this_id_user=id_users
        try:
            url="indodax_list_active"
            param={'id_users':id_users}
            r=http.post(url,data=param)
            respon=r.json()
            global list_tanlalana_active
            list_tanlalana_active=respon['data']
            return list_tanlalana_active
        except Exception:
                # sleep for a bit in case that helps
                time.sleep(2)
                return tanlalana.list_data_server_active(this_id_user)

     #MENAMPILKAN COIN YANG AKAN DI JUAL DI STRATEGI DUMP SELL
    def get_dump_sell():
        try:
            url="get_dump_sell"
            r=http.post(url)
            respon=r.json()
            global list_get_dump_sell
            list_get_dump_sell=respon['data']
            return list_get_dump_sell
        except Exception:
                # sleep for a bit in case that helps
                time.sleep(2)
                return tanlalana.get_dump_sell()

     #MENAMPILKAN COIN DI STRATEGI FIBO ACTIVE
    def list_fibo_active(id_users):
        try:
            url="list_fibo_active"
            param={'id_users':id_users}
            r=http.post(url,data=param)
            respon=r.json()
            list_fibo_active=respon['data']
            return list_fibo_active
        except Exception:
                # sleep for a bit in case that helps
                time.sleep(2)
                return tanlalana.list_fibo_active(id_users)

    #MENAMPILKAN KOIN FIBO YANG AKAN DIJUAL
    def update_all_trade_run():
        try:
            url="update_all_trade_run"
            r=http.post(url)
            respon=r.json()
            return respon
        except Exception:
                # sleep for a bit in case that helps
                time.sleep(2)
                return tanlalana.update_all_trade_run()

    def trade_run_detail(id_users,order_id):
        try:
            url="trade_run_detail"
            param={'id_users':id_users,'order_id':order_id}
            r=http.post(url,data=param)
            respon=r.json()
            return respon
        except Exception:
                # sleep for a bit in case that helps
                time.sleep(2)
                return tanlalana.trade_run_detail(id_users,order_id)

    #indodax list strategi dumb buy
    def list_tanlalana_auto_buy_sell(id_coin):
        coin=id_coin
        try:
            param={'id_coin':id_coin}
            url="indodax_auto_buy_sell_list"
            r=http.post(url,data=param)
            respon=r.json()
            list_tanlalana_auto_buy_sell=respon['data']
            return list_tanlalana_auto_buy_sell
        except Exception:
                # sleep for a bit in case that helps
                time.sleep(2)
                return tanlalana.list_tanlalana_auto_buy_sell(coin)

    #indodax list strategi dumb sell
    def indodax_dump_list_sell(id_coin):
        coin=id_coin
        try:
            param={'id_coin':id_coin}
            url="indodax_dump_list_sell"
            r=http.post(url,data=param)
            respon=r.json()
            indodax_dump_list_sell=respon['data']
            return indodax_dump_list_sell
        except Exception:
                # sleep for a bit in case that helps
                time.sleep(2)
                return tanlalana.indodax_dump_list_sell(coin)

    def list_trade_run_sell(id_users):
        try:
            url="list_trade_run_sell"
            param={'id_users':id_users}
            r=http.post(url,data=param)
            respon=r.json()
            list_trade_run_sell=respon['data']
            return list_trade_run_sell
        except Exception:
                # sleep for a bit in case that helps
                time.sleep(2)
                return tanlalana.list_trade_run_sell(id_users)


    #MELAKUKAN UPDATE DI STRATEGI DUMP SELL
    def update_tanlalana_auto_buy_sell(id,id_coin,status,harga_buy):
        this_id=id
        this_id_coin=id_coin
        this_status=status
        this_harga_buy=harga_buy

        try:
            #MELAKUKAN JEDA UNTUK MEMASTIKAN KOIN TERUPDATE
            time.sleep(2)
            param={'id':id,'id_coin':id_coin,'status':status,'harga_buy':harga_buy}
            url="indodax_auto_buy_sell_update"
            r=http.post(url,data=param)
        except Exception:
                # sleep for a bit in case that helps
                time.sleep(2)
                return tanlalana.update_tanlalana_auto_buy_sell(this_id,this_id_coin,this_status,this_harga_buy)

    #MELAKUKAN UPDATE DI STRATEGI DUMP SELL
    def update_trade_run(id,status):
        this_id=id
        this_status=status

        try:
            #MELAKUKAN JEDA UNTUK MEMASTIKAN KOIN TERUPDATE
            time.sleep(2)
            param={'id':id,'status':status}
            url="update_trade_run"
            r=http.post(url,data=param)
        except Exception:
                # sleep for a bit in case that helps
                time.sleep(2)
                return tanlalana.update_trade_run(this_id,this_status)

    #indodax setting
    def indodax_setting(nama,id_users):
        this_nama=nama
        this_id_users=id_users
        try:
            param={'nama':nama,'id_users':id_users}
            url="indodax_setting"
            r=http.post(url,data=param)
            respon=r.json()
            indodax_setting_ap=respon['data']
            return indodax_setting_ap

        except Exception:
                # sleep for a bit in case that helps
                time.sleep(2)
                return tanlalana.indodax_setting(this_nama,this_id_users)

    #parameter khusus koin btc
    def update_btc():
        try:
            url_btc="https://indodax.com/api/ticker/btcidr"
            r_btc=http.post(url_btc)
            ticker=r_btc.json()
            #kode update ke server tanlalana
            param={'coin':'btcidr','suport_update':ticker['ticker']['low'],'resisten_update':ticker['ticker']['high']}
            url="indodax_update"
            r=http.post(url,data=param)
            respon=r.json()
            return respon
  
        except Exception:
                # sleep for a bit in case that helps
                time.sleep(2)
                return tanlalana.update_btc()

    #melakukan strategi reset fibo
    def strategi_reset(id_coin,id_users):
        this_id_coin=id_coin
        this_id_users=id_users
        try:
            time.sleep(2)
            param={'id_coin':id_coin,'id_users':id_users}
            url="strategi_reset"
            r=http.post(url,data=param)
        except Exception:
                time.sleep(2)
                return tanlalana.strategi_reset(this_id_coin,this_id_users)

    #melakukan strategi fibo reset
    def dump_reset(id_coin,id_users):
        this_id_coin=id_coin
        this_id_users=id_users
        try:
            time.sleep(4)
            param={'id_coin':id_coin,'id_users':id_users}
            url="dump_reset"
            r=http.post(url,data=param)
        except Exception:
                time.sleep(2)
                return tanlalana.dump_reset(this_id_coin,this_id_users)

    #fungsi untuk control bot indodax mematikan dan  menghidupkan fungsi
    def control_indodax(nama,id_users):
            this_nama=nama
            this_id_users=id_users
            try:
                param={'nama':nama,'id_users':id_users}
                url="control_indodax"
                r=http.post(url,data=param)
                control=r.json()
                return control['data']
            except Exception:
                    # sleep for a bit in case that helps
                    time.sleep(2)
                    return tanlalana.control_indodax(this_nama,this_id_users)

    #FUNGSI UNTUK MENJUAL ALL KOIN JIKA SUDAH SESUI TARGET
    def indodax_simple_sell():
            try:
                url="indodax_simple_sell"
                r=http.post(url)
                respon=r.json()
                global indodax_simple_sell
                indodax_simple_sell=respon['data']
                return indodax_simple_sell
            except Exception:
                    # sleep for a bit in case that helps
                    time.sleep(2)
                    return tanlalana.indodax_simple_sell()

    #ADD DATA SELL

    def trade_run_add(nama,id_users,id_coin,harga_buy,harga,keuntungan,status,receive_coin,spend_rp,fee,remain_rp,order_id):
            this_nama=nama
            this_keuntungan=keuntungan
            this_id_users=id_users
            this_id_coin=id_coin
            this_harga_buy=harga_buy
            this_harga=harga
            this_status=status
            this_receive_coin=receive_coin
            this_spend_rp=spend_rp
            this_fee=fee
            this_remain_rp=remain_rp
            this_order_id=order_id
            try:
                param={'nama':nama,'id_users':id_users,'id_coin':id_coin,'harga_buy':harga_buy,'harga':harga,'keuntungan':keuntungan,'status':status,'receive_coin':receive_coin,'spend_rp':spend_rp,'fee':fee,'remain_rp':remain_rp,'order_id':order_id}
                url="trade_run_add"
                r=http.post(url,data=param)
                result=r.json()
                return result
            except Exception:
                    # sleep for a bit in case that helps
                    time.sleep(2)
                    return tanlalana.trade_run_add(this_nama,this_id_users,this_id_coin,this_harga_buy,this_harga,this_status,this_keuntungan,this_receive_coin,this_spend_rp,this_fee,this_remain_rp,this_order_id)

class tanlalana_fungsi:
        def update_sr_to_server(id_users,crypto):
            this_crypto=crypto
            this_id_users=id_users
            try:
                #melakukan jeda untuk memastikan proses sudah selesai
                time.sleep(2)
                print("ini adalah update data to server")
                NewTanlalana=tanlalana
                NewIndodax=indodax(crypto)
                #ambil info status coin sekarang dari server
                result=NewIndodax.api_ticker_detail()
                #update suport resisten ke server tanlalna
                status=NewTanlalana.update_suport_resisten_to_server(id_users,crypto,result['ticker']['low'],result['ticker']['high'])
                NewTanlalana.update_btc()
                print(status)
            except Exception:
                    # sleep for a bit in case that helps
                    time.sleep(2)
                    return tanlalana_fungsi.update_sr_to_server(this_crypto)

        def get_data_strategi(name,id_coin):
            this_name=name
            this_id_coin=id_coin
            try:
                param={'strategi':name,'id_coin':id_coin}
                url="indodax_strategi_detail"
                r=http.post(url,data=param)
                indodax_strategi=r.json()
                return indodax_strategi['data']
            except Exception:
                    # sleep for a bit in case that helps
                    time.sleep(2)
                    return tanlalana_fungsi.get_data_strategi(this_name,this_id_coin)


        def update_data_strategi(name,id_coin,buy,idr,status,id):
            this_name=name
            this_id_coin=id_coin
            this_buy=buy
            this_idr=idr
            this_status=status
            this_id=id

            try:
                #melakukan jeda untuk memastikan proses selesai
                time.sleep(2)
                param={'strategi':name,'id_coin':id_coin,'buy':buy,'idr':idr,'status':status,'id':id}
                url="indodax_strategi_update"
                http.post(url,data=param)
            except Exception:
                    # sleep for a bit in case that helps
                    time.sleep(2)
                    return tanlalana_fungsi.update_data_strategi(this_name,this_id_coin,this_buy,this_idr,this_status,this_id)

     
