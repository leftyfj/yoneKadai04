import csv

ITEMS_MASTER_PATH = 'items_master.csv'
ORDER_BALANCE_PATH = 'order_balance.csv'

#商品クラス
class Item:
  #初期化
  def __init__(self, in_code, in_name, in_price):
    self.code = in_code
    self.name = in_name
    self.price = in_price
    self.detail = [self.code, self.name, self.price]
    # self.items_master = []
    
  #Read 表示
  def show_detail(self):
    print('--------------------')
    print(f'商品コード:{self.code}')
    print(f'商品名:{self.name}')
    print(f'価格:{self.price}円')
    print('--------------------')
    print(' ')
 
    #項目内容の取得   
  def get_code(self):
      # return int(self.code)
    return self.code

  def get_name(self):
    return self.name

  def get_price(self):
    return int(self.price)
  
  #Update 更新 商品コード、商品名、価格
  def update_code(self, new_code):
    self.code = new_code
    
  def update_name(self, new_name):
    self.name= new_name
    
  def update_price(self, new_price):
    self.price= new_price 

#商品マスタクラス
class ItemsMaster:
  #初期化 インスタンス化
  def __init__(self):
    self.items_master = []
    
  def get_master_list(self):
    with open(ITEMS_MASTER_PATH, 'r', encoding='utf-8_sig', newline='') as file:
      reader = csv.reader(file)
      for row in reader:
        self.items_master.append(row)
    return self.items_master
  
  #Read 詳細表示表示
  def show(self):
    items = self.get_master_list()
    print('商品コード','商品名', '価格')
    print('-------------------------')
    for item in items:
      print(item[0], item[1], item[2])
    print('')
    
  #UPdate 商品登録
  def add_new_item(self):
    print('### 新商品登録 ###')
    #登録済ではないか、点検
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
      else:
        break
    
    while True:
      code = input('商品コードを入力してください。')
      for row in self.items_master:
        if code in row[0]:
          checker = 0
          break
        else:
          #同名の商品が登録されていない
          checker = 1

      if checker == 0:
        print('この商品コードは既に使用されています。変更してください。')
        continue
      else:
        break
    price = input('価格を入力してください。')
    
    newItem = Item(code, name, price)
    self.items_master.append(newItem.detail)
    print(self.items_master)
    with open(ITEMS_MASTER_PATH, 'w', encoding='utf-8_sig', newline='') as file:
      writer = csv.writer(file)
      writer.writerows(self.items_master)

  #Delete 商品削除
  

#注文クラス
class Order:
  #初期化 ファイルから情報を取得
  def __init__(self, fileName):
    self.filename = fileName
    self.order_balance_list = []
  
  def get_balance(self):
    with open(self.filename, "r", encoding="utf-8_sig") as file:
      reader = csv.reader(file)
      for row in reader:
        self.order_balance_list.append([int(row[0]), row[1].strip(' '), int(row[2])])
    return self.order_balance_list
    
  #Read 注文残表示
  def show_balance(self):
    print('注文番号', '商品コード', '数量')
    print('-------------------------')
    # list = self.get_balance()
    with open(self.filename, "r", encoding="utf-8_sig") as file:
      reader = csv.reader(file)
      for row in reader:
        print(row[0], row[1], row[2])
  

#注文明細の一覧を作成する関数      
def order_detail(item_list, order_list):                                           
  print('注文番号', '商品コード', '商品名', '残', '価格', '金額')
  print('----------------------------------------')
  for order in order_list:
     for item in item_list:
       if order[1] in item[0]:
         code = item[0]
         name = item[1]
         price = int(item[2])
         quantity = int(order[2])
         amount = price * quantity
         print(order[0], code, name, quantity, price, amount)
         break

  #Update 新規注文
  
  #Delete 注文削除

def main():
  # Orange = Item('001', 'みかん', 100)
  # Apple = Item('002', 'りんご', 200)
  
  # Orange.show_detail()
  # Apple.show_detail()
  
  items_master = ItemsMaster()
  items_master.show()
  
  order = Order(ORDER_BALANCE_PATH)
  order.show_balance()
  
  order_detail(items_master.get_master_list(), order.get_balance())

if __name__ == "__main__":
    main()
