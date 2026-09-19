class StockItem:
    def __init__(self, item_id: str, name: str, quantity: int = 0) -> None:
        self.item_id = item_id.strip().upper()
        self.name = name.strip()
        self.quantity = max(0, quantity)

    def sell(self, amount: int) -> bool:
        if amount <= 0 or amount > self.quantity:
            return False
        self.quantity -= amount
        return True

    def restock(self, amount: int) -> bool:
        if amount <= 0:
            return False
        self.quantity += amount
        return True

    def is_low_stock(self, threshold: int = 5) -> bool:
        return self.quantity < threshold

    def to_csv_line(self) -> str:
        return f"{self.item_id},{self.name},{self.quantity}\n"
