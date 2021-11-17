import csv
# １
# オーダー登録した商品の一覧（商品名、価格）を表示できるようにしてください

### 商品クラス
class Item:
  
  #登録
  def __init__(self, in_code, in_name, in_price):
      self.code = in_code
      self.name = in_name
      self.price = in_price
      
  #読み込み
  def show_detail(self):
    print(f'商品コード:{self.code}')
    print(f'商品名:{self.name}')
    print(f'価格:{self.price}')
    print(' ')
  
    
    # return self.name, self.price
  
  def get_code(self):
    return int(self.code)
  
  def get_name(self):
    return self.name
  
  def get_price(self):
    return int(self.price)
  
  #更新
  def update_code(self, new_code):
    self.code = new_code
    
  def update_name(self, new_name):
    self.name= new_name
    
  def update_price(self, new_price):
    self.price= new_price
    
  #削除


# オーダークラス
class Order:
  def __init__(self, fileName):
    self.filename = fileName
  
  def get_balance(self):
    with open(self.filename, "r", encoding="utf-8_sig") as f:
      # balance_list = f.read().splitlines()
      reader = csv.reader(f)
      _balance_list = [row for row in reader]
      return _balance_list
    
  #注文残表示
  def show_balance(self):
    with open(self.filename, "r", encoding="utf-8_sig") as f:
      # balance_list = f.read().splitlines()
      balance_list = csv.reader(f)
      print('注文番号','コード','数量')
      for balance in balance_list:
        print(balance[0], balance[1], balance[2])
  #新規
  def new_order(self):
    code = input('商品コードを入力してください。')
    quantity = input('数量(個数)を入力しえください。')
    
    ##codeが商品マスタに登録されているか
  #変更
  
  #取り消し
  
  ### メイン処理
def main():
  
  #商品マスタ生成
  items_master = []
  items_master.append(Item('001', 'みかん', 100))
  items_master.append(Item('002', 'りんご', 200))
  print('### 商品マスタ ###')
  print('コード','商品名','価格')
  for item in items_master:
    code = item.get_code()
    name = item.get_name()
    price = item.get_price()
    print(code, name, price)
    
  # １
# オーダー登録した商品の一覧（商品名、価格）を表示できるようにしてください


# ２
# オーダーをコンソール（ターミナル）から登録できるようにしてください
# 登録時は商品コードをキーとする
  print('### オーダー残 ###')
  order = Order("order_balance.csv")
  # order.show_balance()
  balance_list = order.get_balance()
  print('注文番号','商品コード','商品名','残','価格','金額')
  for bal in balance_list:
    for item in items_master:
      if(int(bal[1]) == item.get_code()):
        amount = int(bal[2]) * item.get_price()
        print(bal[0], bal[1], item.get_name(), bal[2], item.get_price(), amount)
  print('')
  order.new_order()
  
if __name__ == "__main__":
    main()