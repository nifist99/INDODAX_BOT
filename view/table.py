from texttable import Texttable

def view_table(jam,coin,status,price_target,idr,price_indodax):
                  table = Texttable()
                  table.add_rows([
                                  ["TIME", "COIN", "STATUS","PRICE TARGET","IDR","PRICE INDODAX"],
                                  [jam, coin, status,price_target,idr,price_indodax]
                                ])
                  print(table.draw())
                  print()

def welcome():
                  table = Texttable()
                  table.add_rows([
                                  ["SELAMAT DATANG DI APLIKASI BOT INDODAX BY TANLALANA"]
                                ])
                  print(table.draw())
                  print()

def sayonara():
                  table = Texttable()
                  table.add_rows([
                                  ["TERIMAKASIH TELAH MENGGUNAKAN BOT INDODAX BY TANLALANA"]
                                ])
                  print(table.draw())
                  print()

def txt(variabel):
                  table = Texttable()
                  table.add_rows([
                                  [variabel]
                                ])
                  print(table.draw())
                  print()