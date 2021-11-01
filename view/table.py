from texttable import Texttable

def view_table(jam,coin,status,price_target,idr,price_indodax):
                  table = Texttable()
                  table.add_rows([
                                  ["TIME", "COIN", "STATUS","PRICE TARGET","IDR","PRICE INDODAX"],
                                  [jam, coin, status,price_target,idr,price_indodax]
                                ])
                  print(table.draw())
                  print()