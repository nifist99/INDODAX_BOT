import json,os,sys,time,urllib
import requests 
from hmac import HMAC
import hashlib
import urllib.parse

from requests_toolbelt import sessions
from requests.adapters import HTTPAdapter
from urllib3.util import Retry

retries = Retry(total=3, backoff_factor=0.3, status_forcelist=[500, 502, 504])
adapter = HTTPAdapter(max_retries=retries)

http=requests.Session()
http.mount("https://", adapter)
http.mount("http://", adapter)

class private_api:
  '''Ini dirancang agar mempermudah jual beli mata uang digital di indodax ambil key dan secret di akun anda
  >>> from Indodax import indodax
  >>> key = 'ABCD-EFGH-IJKL-MNOP' # Ambil dari akun indodax anda
  >>> secret = b'hiwiwijwjsjsjsj' # Ini jg sama
  >>> a = indodax(key, secret)
  >>> a.get_info() # Nanti akan muncul informasi saldo
  '''


  def __init__(self, key, secret):
    #key dari indodax
    self.key = key
    #secret dari indodax
    self.secret = secret


  def query(self, method, **kwargs: dict):
    # self.method=method
    # self.kwargs=kwargs
    # try:
        url = 'https://indodax.com/tapi/'

        kwargs['method'] = method
        kwargs['nonce'] = int(time.time())

        post_data = kwargs
        byte_key = bytes(self.secret, 'UTF-8') 
        

        sign = HMAC(byte_key, urllib.parse.urlencode(post_data).encode('utf-8'), hashlib.sha512).hexdigest()
        headers = {
          'Sign': sign,
          'Key': self.key
        }

        r = http.post(url, headers=headers, data=kwargs)
        js = r.json()
        return js
    # except Exception:
    #                 time.sleep(2)
    #                 return private_api.query(self, self.method, self.kwargs)


  def get_info(self):
    return self.query('getInfo')


  def history(self):
    return self.query('transHistory')


  def trade_buy(self, coin, diharga, jumlah, idr_or_btc='idr'):
    ''' lanjutan intruksi di atas
    >>> a.trade_buy('doge', '41', '50000') # kita akan membeli doge 50rb
    '''
    pair = coin+'_'+idr_or_btc
    m = {
      'pair': pair,
      'type': 'buy',
      'price': diharga,
      idr_or_btc: jumlah,
    }

    return self.query('trade', **m)


  def trade_sell(self, coin, diharga, jumlah, idr_or_btc='idr'):
    ''' disini sama cara penggunaanya seperti trade_buy()
    hanya saja ini untuk menjual
    '''
    pair = coin+'_'+idr_or_btc
    m = {
      'pair': pair,
      'type': 'sell',
      'price': diharga,
      coin: jumlah
    }

    return self.query('trade', **m)


  def open_order(self,coin, idr_or_btc='idr'):
    pair = coin+'_'+idr_or_btc
    m = {
      'pair': pair
    }

    return self.query('openOrders', **m)


  def order_history(self, coin, idr_or_btc='idr'):
    pair = coin+'_'+idr_or_btc
    m = {'pair': pair}

    return self.query('orderHistory', **m)


  def get_order(self, coin, order_id, idr_or_btc='idr'):
    pair = coin+'_'+idr_or_btc
    m = {
      'pair': pair,
      'order_id': order_id
    }

    return self.query('getOrder', **m)


  def cancel_order_buy(self, coin, order_id, idr_or_btc='idr'):
    pair = coin+'_'+idr_or_btc
    m = {
      'pair': pair,
      'order_id': order_id,
      'type': 'buy'
    }
    return self.query('cancelOrder', **m)


  def cancel_order_sell(self, coin, order_id, idr_or_btc='idr'):
    pair = coin+'_'+idr_or_btc
    m = {
      'pair': pair,
      'order_id': order_id,
      'type': 'sell'
    }

    return self.query('cancelOrder', **m)


  def withdraw(self, coin, address, amount, memo='', req_id=''):
    '''Hati2 dengan ini, jika anda salah maka coin kalian akan hilang
    '''
    m = {
      'currency': coin,
      'withdraw_address': address,
      'withdraw_amount': amount,
      'withdraw_memo': memo,
      'request_id': req_id
    }
    return self.query('withdrawCoin', **m)
