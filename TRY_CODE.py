from api.web import tanlalana,tanlalana_fungsi
from api.public import indodax 
from config import WindowsInhibitor
from api.private import private_api
import time
import os
from config import setting
#aksi looping 
from INDODAXSELL import view_coin_jumlah
from texttable import Texttable
from countdown import countdown


def main():
                    # data=private_api(setting.apikey(),setting.screetkey())
                    # list_coin=data.get_info()
                    # print("ini adalah list")
                    # NewIndodax=indodax('zilidr')

                    # #ambil data dari server indodax
                    # result=NewIndodax.api_ticker_detail()
                    # coin=float(list_coin['return']['balance']['zil'])

                    # #strategi fibonanci harga sell server indodax
                    # harga_sell=float(result['ticker']['buy'])

                    # cek=data.trade_sell('zil',harga_sell,7.08167613)

                    # print(cek)
                  # NewTanlalana=tanlalana
                  # test=NewTanlalana.trade_run_add('dump',int(3),int(187),float(1000),float(10000),int(5),'sell',float(9000),float(9200),float(29),float(0),int(18888))
                  # test=NewTanlalana.history_trade_add('zil',int(3),'buy',float(1200),int(187),float(15000),0,float(9000),float(9200),float(29),float(0),int(18888))
                  # test=tanlalana.list_trade_run_sell()
                  # print(test)
                  # cek=view_coin_jumlah()
                  # print(cek)

                  table = Texttable()
                  table.add_rows([
                                  ["DELAY PROGRAM"]
                                ])
                  print(table.draw())
                  print()
                  countdown(1)
                  print("lanjut")

if __name__ == "__main__":
      main()