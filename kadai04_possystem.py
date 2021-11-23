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
    
    def view_item(self):
        print('--------------------')
        print(f'商品コード:{self.item_code}')
        print(f'商品名:{self.item_name}')
        print(f'価格:{self.price}円')
        print('--------------------')
        print(' ')

    def add_to_master(self):
        row = [self.item_code, self.item_name, self.price]
        with open(ITEMS_MASTER_PATH, 'a', encoding='utf-8_sig', newline=None) as file:
            writer = csv.writer(file)
            writer.writerow(row)


### オーダークラス
class Order:
    def __init__(self,item_master):
        self.item_order_list=[]
        self.item_master=item_master
        self.item_order_list_detail = []
        
    # ４
    #オーダー登録時に個数も登録できるようにしてください
    def add_item_order(self, item_code, quantity):
        one_order = [item_code, quantity]
        self.item_order_list.append(one_order)
     
    #注文一覧を表示するメソッド   
    def view_item_list(self):
        print('### 注文表 ###')
        print('商品コード','数量')
        for item in self.item_order_list:
            print(item[0], item[1])
    
    #注文の明細を表示するメソッド
    def view_order_detail(self):
        detail_list, total = self.make_order_detail()
        print('商品コード', '商品名', '数量', '単価', '金額')
        for row in detail_list:
            print(row[0], row[1], row[2], row[3], row[4])
        print(f'合計金額 {total:,}円')
        
    #オーダー明細、合計金額をリスト化するメソッド
    def make_order_detail(self):
        self.total_amount = 0
        for order in self.item_order_list:
            for item in self.item_master:
                # if order[0] == item.get_code():
                if order[0] == item[0]:
                    #code = item.get_code()
                    #name = item.get_name()
                    code = item[0]
                    name = item[1]
                    #price = int(item.get_price())
                    price = int(item[2])
                    quantity = int(order[1])
                    amount = price * quantity
                    self.item_order_list_detail.append([code, name,price, quantity, amount])
                    self.total_amount += amount
        return self.item_order_list_detail, self.total_amount
                
    ### 商品マスタクラス
class ItemsMaster:
    def __init__(self) -> None:
        self.item_master = []

    def get_master(self):
        with open(ITEMS_MASTER_PATH, 'r', encoding='utf-8_sig', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                self.item_master.append(row)
        return self.item_master
    
### メイン処理
def main():

    # マスタ登録
    
    
    
    # ３
    #商品マスタをCSVから登録できるようにしてください
    item_master = ItemsMaster().get_master()
    # item_master=[]
    # item_master.append(Item("001","りんご",100))
    # item_master.append(Item("002","なし",120))
    # item_master.append(Item("003","みかん",150))
    
    # apple = Item("001", "りんご", 100)
    # pear = Item("002", "なし", 120)
    # orange = Item("003", "みかん", 150)
    # strawberry = Item('004',"いちご", 250)
    # strawberry.add_to_master()
    

    # ２
    # オーダーをコンソール（ターミナル）から登録できるようにしてください
    # 登録時は商品コードをキーとする
    
    # ６
    # お客様からのお預かり金額を入力しお釣りを計算できるようにしてください
    # オーダー登録
    order = Order(item_master)
    check = 'Y'
    while check == 'Y':
        code = input('商品コードを入力して下さい。')
        quantity = input('数量を入力して下さい。')
        order.add_item_order(code, quantity)
        
        check = input('続けますか？ 続ける ⇒ Y、 終わる => N ')
        check = check.upper()
    else:
        deposit = int(input('お預かりした金額を入力して下さい。'))
        print('注文を終了します。')   
        
    # order.add_item_order("001")
    # order.add_item_order("002")
    # order.add_item_order("003")

    # オーダー表示
    # １
    #オーダー登録した商品の一覧（商品名、価格）を表示できるようにしてください
    order.view_item_list()
    # ５
    # オーダー登録した商品の一覧（商品名、価格）を表示し、かつ合計金額、個数を表示できるようにしてください
    order.view_order_detail()
    
    detail, total_amount = order.make_order_detail()
    change = deposit - total_amount
    print(f'お預かり {deposit:,}円')
    print(f'お釣り:{change:,}円')
    
if __name__ == "__main__":
    main()