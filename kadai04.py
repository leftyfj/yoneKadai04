import csv
# オーダー登録した商品の一覧（商品名、価格）を表示できるようにしてください

### 商品クラス
class Item:
  
  #登録
  def __init__(self, in_code, in_name, in_price):
      self.code = in_code
      self.name = in_name
      self.price = in_price
      self.items_master = []
      
  #R 読み込み
  def read_from_master(self):
    # items_master = []
    with open('items_master.csv','r', encoding='utf-8_sig', newline='') as file:
      for row in csv.reader(file):
        self.items_master.append(row)
      print(self.items_master)
      
  # U 更新 新規商品登録
  def add_new_item(self):
    # print(f'最後の商品code={last_code}')
    print('### 新商品登録 ###')
    
    #登録する商品はすでにマスターに登録されているか確認
    while True:
      name = input('商品名を入力してください。')
      for row in self.items_master:
        if name in row[1]:
          checker = 0
          break
        else:
          #同名の商品が登録されていない
          checker = 1

      if checker == 0:
        print('この商品は登録済です。')
        continue
      else :
        break
    code = input('商品コードを入力してください。')
    price = input('価格を入力してください。')
    
    new_item = [code, name, price]
    self.items_master.append(new_item)
    print(self.items_master)
    
  #一覧表示
  def show_detail(self):
    print(f'商品コード:{self.code}')
    print(f'商品名:{self.name}')
    print(f'価格:{self.price}')
    print(' ')
  
  def get_code(self):
    # return int(self.code)
    return self.code
  
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
  def __init__(self, fileName,items_master ):
    self.filename = fileName
    self.items_master = items_master
  
  def get_balance(self):
    _balance_list = []
    with open(self.filename, "r", encoding="utf-8_sig") as f:
      reader = csv.reader(f)
      for row in reader:
        _balance_list.append([int(row[0]), row[1].strip(' '), int(row[2])])
      return _balance_list
    
  #注文残表示
  def show_balance(self):
    with open(self.filename, "r", encoding="utf-8_sig") as f:
      balance_list = csv.reader(f)
      print('注文番号','コード','数量')
      for balance in balance_list:
        print(balance[0], balance[1], balance[2])
        
  #新規
  def new_order(self):
    ##codeが商品マスタに登録されているか
    flag = 0
    while flag == 0:
      code = input('商品コードを入力してください。')
      for items in self.items_master:
        if code == items.get_code():
          flag = 1
          break
      
      if flag == 0:
         print('商品マスタに登録されていません')
         continue
      quantity = input('数量(個数)を入力してください。')
      
    order_balance = self.get_balance()
    last_order_num = order_balance[-1][0]
    order = [last_order_num + 1, code, quantity]
    order_balance.append(order)
    
    #DB(csvファイル)を更新
    with open(self.filename, 'w', newline='') as f:
      writer = csv.writer(f)
      writer.writerows(order_balance)
    
    print('新規オーダーを追加しました。')
      
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
  order = Order("order_balance.csv", items_master)
  order.show_balance()
  balance_list = order.get_balance()
  print('注文番号','商品コード','商品名','残','価格','金額')
  for bal in balance_list:
    for item in items_master:
      if item.get_code() == bal[1]:
        amount = bal[2] * item.get_price()
        print(bal[0], bal[1], item.get_name(), bal[2], item.get_price(), amount)
  print('')
  
  # 新規注文
  # order.new_order()
  
  #商品マスタファイルからの読み込み
  item.read_from_master()
  
  item.add_new_item()

if __name__ == "__main__":
    main()