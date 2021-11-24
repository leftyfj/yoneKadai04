## 商品クラス
class Item:
    def __init__(self, item_code, item_name, price):
        self.item_code = item_code
        self.item_name = item_name
        self.price = price

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
