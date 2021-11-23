import csv
import datetime
import traceback
import os

ITEMS_MASTER_PATH = 'items_master.csv'
ORDER_BALANCE_PATH = 'order_balance.csv'
_datetime = datetime.datetime.now().strftime('%Y-%m-%d_%H_%M_%S')
TRANSACTION_FILE_PATH = f'./transaction/trans_{_datetime}.txt'

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
        
        list = ItemsMaster().get_master()
        list.append(row)
        
        with open(ITEMS_MASTER_PATH, 'w', encoding='utf-8_sig', newline='') as file:
            writer = csv.writer(file, lineterminator='\n')
            writer.writerows(list)


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
        print('')
        print('### 取引明細 ###')
        print('商品コード', '商品名', '数量', '単価', '金額')
        for row in detail_list:
            print(row[0], row[1], row[2], row[3], row[4])
        print(f'合計金額 {total:,}円')
        
    #オーダー明細、合計金額をリスト化するメソッド
    def make_order_detail(self):
        item_master = ItemsMaster().get_master()
        self.item_order_list_detail = []
        self.total_amount = 0
        for order in self.item_order_list:
            for item in item_master:             
                if order[0] in item:
                    code = item[0]
                    name = item[1]
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
    # ３
    #商品マスタをCSVから登録できるようにしてください
    #商品マスタの呼び出し
    
    # マスタ登録
    #新商品のマスタ登録
    print('### 新商品マスタ登録 ###')
    confirm = input('商品登録をしますか？ はい⇒ Y(y)、 いいえ => N (n)')
    item_master = ItemsMaster().get_master()
    confirm = confirm.upper()
    if confirm == 'Y':
        check = 'Y'
        while True: 
            code = str(input('商品コードを入力して下さい。'))
            ##商品コード重複確認
            flag = 0
            for item in item_master:
                if code in item:
                    flag = 0
                    break
                else:
                    flag = 1
            
            if flag == 0:
                print('この商品コードは既に使用されています。変更してください。')
                continue
            else:
                break
                
        name = input('商品名を入力して下さい。')
        price = int(input('価格を入力して下さい。'))
        new_item = Item(code, name, price)
        new_item.add_to_master()
            
        check = input('登録を続けますか？ 続ける ⇒ Y、 終わる => N ')
        check = check.upper()

    print('注文に移ります')

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
    
    # ７
    # 課題５、６の内容を、日付時刻をファイル名としたレシートファイル（テキスト）に出力できるようにしてください
    with open(TRANSACTION_FILE_PATH, 'a', encoding='utf-8_sig', newline='\n') as file:
        print('商品コード,', '商品名,', '数量,', '単価,', '金額', file=file)
        for row in detail:
            file.write(",".join(str(_) for _ in row) + '\n')
        print(f'合計:{total_amount:,}円', file=file)
        print(f'入金:{deposit:,}円', file=file)
        print(f'釣り:{change:,}円' + '\n', file=file)
        

if __name__ == "__main__":
    main()