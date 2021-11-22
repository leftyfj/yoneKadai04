import csv

ITEMS_MASTER_PATH = 'items_master.csv'
ORDER_BALANCE_PATH = 'order_balance.csv'

### 商品クラス
class Item:
    def __init__(self,item_code,item_name,price):
        self.item_code=item_code
        self.item_name=item_name
        self.price=price
    
    def get_code(self):
        return self.item_code
    
    def get_price(self):
        return self.price
    
    def get_name(self):
        return self.item_name

### オーダークラス
class Order:
    def __init__(self,item_master):
        self.item_order_list=[]
        self.item_master=item_master
    
    # ４
    #オーダー登録時に個数も登録できるようにしてください
    def add_item_order(self,item_code, quantity):
        one_order = [item_code, quantity]
        self.item_order_list.append(one_order)
        
    def view_item_list(self):
        print('### 注文残高 ###')
        print('商品コード','数量')
        for item in self.item_order_list:
            print(item[0], item[1])
    
    # ５
    #オーダー登録した商品の一覧（商品名、価格）を表示し、かつ合計金額、
    # 個数を表示できるようにしてください
    
    def view_order_detail(self):
        print('### 注文残高明細 ###')
        print('商品コード', '商品名', '残', '価格', '金額')
        print('----------------------------------------')
        total_amount = 0
        for order in self.item_order_list:
            for item in self.item_master:
                if order[0] == item[0]:
                    code = item[0]
                    name = item[1]
                    price = int(item[2])
                    quantity = int(order[1])
                    amount = price * quantity
                    total_amount += amount
                    print(code, name, quantity, price, amount)
                    break
        print(f'合計金額 {total_amount}円')
    
    def calc_sales_amount(self, code, quantity):
        #注文を受け付ける
        self.add_item_order(code, quantity)
        #商品マスタから商品code、価格を検索する
        for item in self.item_master:
            if item[0] == code:
                price = int(item[2])
                break
        
        #売上金額を計算する
        sales = price * quantity
        
        return sales
### メイン処理
def main():
   
    # item_master=[]
    # item_master.append(Item("001","りんご",100))
    # item_master.append(Item("002","なし",120))
    # item_master.append(Item("003","みかん",150))
    # print(item_master)
    
    # ３
    #商品マスタをCSVから登録できるようにしてください
    # マスタ登録
    #(1) 商品マスタファイルを読み込む
    item_master = []
    with open(ITEMS_MASTER_PATH, 'r', encoding='utf-8_sig', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            item_master.append(row)
            
    #(2) 商品の登録
    # code= input('商品コードを入力して下さい。')
    # code = str(code)
    # name = input('商品名を入力して下さい。')
    # price = input('価格を入力して下さい。')
    # price = int(price)
    # new_item = Item(code, name, price)
    # new_row = [new_item.get_code(), new_item.get_name(), new_item.get_price()]
    # item_master.append(new_row)
    print(item_master)
    
    # (3) 商品マスタファイルを更新
    # with open(ITEMS_MASTER_PATH, 'w', encoding='utf-8_sig', newline='') as file:
    #   writer = csv.writer(file)
    #   writer.writerows(item_master)
      
    # オーダー登録
    order=Order(item_master)
    order.add_item_order("001", 34)
    order.add_item_order("002", 54)
    order.add_item_order("003", 100)
    
    # オーダー表示
    # １
    #オーダー登録した商品の一覧（商品名、価格）を表示できるようにしてください
    order.view_item_list()
    
    # ２
    #オーダーをコンソール（ターミナル）から登録できるようにしてください
    #登録時は商品コードをキーとする
    # code = input("商品コードを入力して下さい。")
    # code = str(code)
    # quantity = input("数量を入力して下さい。")
    # quantity = int(quantity)
    # order.add_item_order(code, quantity)
    # order.view_item_list()
    
    # ５
    #オーダー登録した商品の一覧（商品名、価格）を表示し、かつ合計金額、
    #個数を表示できるようにしてください
    order.view_order_detail()
    

    # ６
    # お客様からのお預かり金額を入力しお釣りを計算できるようにしてください
    code = input('商品コードを入力して下さい。')
    quantity = int(input('数量を入力して下さい。'))
    cash = int(input('お預かりした金額を入力して下さい。'))
    sales_amount = order.calc_sales_amount(code, quantity)
    change = cash - sales_amount
    print(f'お釣りは{change}円です。')
    
if __name__ == "__main__":
    main()