import csv

from config import *


## 商品マスタクラス
class ItemsMaster:
    def __init__(self) -> None:
        self.item_master = []

    def get_master(self):
        with open(ITEMS_MASTER_PATH, 'r', encoding='utf-8_sig', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                self.item_master.append(row)
        return self.item_master
