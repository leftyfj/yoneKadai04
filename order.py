### オーダークラス
class Order:
    def __init__(self, item_master):
        self.item_order_list = []
        self.item_master = item_master
        self.item_order_list_detail = []

    # ４
    #オーダー登録時に個数も登録できるようにしてください
    def add_item_order(self, item_code, quantity):
        one_order = [item_code, quantity]
        self.item_order_list.append(one_order)

    #注文一覧を表示するメソッド
    def view_item_list(self):
        print('### 注文表 ###')
        print('商品コード', '数量')
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
                    self.item_order_list_detail.append(
                        [code, name, price, quantity, amount])
                    self.total_amount += amount
        return self.item_order_list_detail, self.total_amount
