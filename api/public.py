import time
import requests

from requests_toolbelt import sessions
from requests.adapters import HTTPAdapter
from urllib3.util import Retry


retries = Retry(total=3, backoff_factor=0.3, status_forcelist=[500, 502, 504])
adapter = HTTPAdapter(max_retries=retries)

http = sessions.BaseUrlSession(base_url="https://indodax.com/api/")
http.mount("https://", adapter)
http.mount("http://", adapter)

class indodax:
    
    # memgambil data dari server indodax
    def __init__(self, coin):
        self.coin=coin
    
    # mengambil semua data dari server indodax untuk mengetahui detail coin
    def get_all_data_coin(self):
        try:
            url="pairs"
            r=http.post(url)
            global data_trading
            data_trading=r.json()
            return data_trading
        except Exception:
                    # sleep for a bit in case that helps
                    time.sleep(2)
                    return indodax.get_all_data_coin(self)

    # mengetahui semua harga coin sekarang
    def api_summary(self):
        try:
            url="summaries"
            r=http.post(url)
            global data_summary
            data_summary=r.json()
            return data_summary
        except Exception:
                    # sleep for a bit in case that helps
                    time.sleep(2)
                    return indodax.api_summary(self)
    
    # melihat dan memeilih detail coin
    def api_ticker_detail(self):
        try:
            url="ticker/"+self.coin
            r=http.post(url)
            detail_ticker=r.json()
            return detail_ticker
        except Exception:
                    time.sleep(2)
                    In=indodax(self.coin)
                    return In.api_ticker_detail()

    def api_detail_btc(self):
        try:
            url="ticker"
            r=http.post(url)
            detail_btc=r.json()
            return detail_btc
        except Exception:
                    # sleep for a bit in case that helps
                    time.sleep(2)
                    return indodax.api_detail_btc(self)

#MAIN FUNGSI UNTUK MENCOBA FUNGSI API

# def main():
#         In=indodax('repv2idr')
#         result=In.api_summary()
#         print(result)
#         print("")


 
   
# if __name__ == "__main__":
#       main()

