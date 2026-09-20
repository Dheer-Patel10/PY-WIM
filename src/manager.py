import os
from src.models import StockItem


class InventoryManager:
    def __init__(self, filepath: str = "data/stock_file.csv") -> None:
        self.filepath = filepath
        self.inventory: dict[str, StockItem] = {}

    def add_item(self, item_id: str, name: str, quantity: int = 0) -> bool:
        item_id = item_id.strip().upper()
        if item_id in self.inventory:
            return False
        self.inventory[item_id] = StockItem(item_id, name, quantity)
        return True

    def get_item(self, item_id: str) -> StockItem | None:
        return self.inventory.get(item_id.strip().upper(), None)

    def remove_item(self, item_id: str) -> bool:
        item_id = item_id.strip().upper()
        if item_id in self.inventory:
            del self.inventory[item_id]
            return True
        return False

    def sell_item(self, item_id: str, amount: int) -> bool:
        item = self.get_item(item_id)
        if item is None:
            return False
        return item.sell(amount)

    def restock_item(self, item_id: str, amount: int) -> bool:
        item = self.get_item(item_id)
        if item is None:
            return False
        return item.restock(amount)

    def get_low_stock_items(self, threshold: int = 5) -> list[StockItem]:
        low_stock_list = []
        for item in self.inventory.values():
            if item.is_low_stock(threshold):
                low_stock_list.append(item)
        return low_stock_list

    def save_to_csv(self) -> None:
        os.makedirs(os.path.dirname(self.filepath), exist_ok=True)

        with open(self.filepath, "w", encoding="utf-8") as file:
            for item in self.inventory.values():
                file.write(item.to_csv_line())

    def load_from_csv(self) -> bool:
        if not os.path.exists(self.filepath):
            return False

        with open(self.filepath, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue

                parts = line.split(",")
                if len(parts) == 3:
                    item_id, name, quantity_str = parts
                    try:
                        quantity = int(quantity_str)
                        self.add_item(item_id, name, quantity)
                    except ValueError:
                        continue
        return True
