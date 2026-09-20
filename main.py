from src.manager import InventoryManager


def main() -> None:
    manager = InventoryManager()
    manager.load_from_csv()

    while True:
        print("=== PY-WIM INVENTORY SYSTEM ===")
        print("1. Add New Item")
        print("2. View All Stock")
        print("3. Sell Stock")
        print("4. Restock Item")
        print("5. View Low Stock Items")
        print("6. Save & Exit")

        choice = input("Enter an option (1-6): ").strip()

        if choice == "1":
            item_id = input("Enter item ID (e.g. M9): ")
            name = input("Enter item name: ")

            try:
                quantity = int(input("Enter quantity of item (integer): "))
            except ValueError:
                print("Error: Quantity must be a valid integer.")
                continue

            if manager.add_item(item_id, name, quantity):
                print("Item added successfully!")
            else:
                print("Error: Item ID already in use.")

        elif choice == "2":
            if not manager.inventory:
                print("No items in inventory")
                continue
            else:
                print("--- CURRENT STOCK ---")
                for item in manager.inventory.values():
                    print(f"ID: {item.item_id} | Name: {item.name} | Qty: {item.quantity}")

        elif choice == "3":
            item_id = input("Enter item ID: ")
            try:
                amount = int(input("Enter amount to sell (integer): "))
            except ValueError:
                print("Invalid input.")
                continue

            if manager.sell_item(item_id, amount):
                print("Sale was successful")
            else:
                print("Sale failed. Either item ID does not exist, or insufficient stock/invalid amount.")


        elif choice == "4":
            item_id = input("Enter item ID: ")
            try:
                amount = int(input("Enter amount to restock (integer): "))
            except ValueError:
                print("Invalid input.")
                continue

            if manager.restock_item(item_id, amount):
                print("Restock was successful")
            else:
                print("Restock failed. Item ID not found or amount must be greater than 0.")

        elif choice == "5":
            low_stock = manager.get_low_stock_items(threshold=10)
            if not low_stock:
                print("All stock levels are sufficient (no low stock items).")
            else:
                print("--- LOW STOCK ALERT ---")
                for item in low_stock:
                    print(f"Item ID: {item.item_id}, Item name: {item.name}, Item Quantity: {item.quantity}")
        elif choice == "6":
            manager.save_to_csv()
            break
        else:
            print("Invalid option")


if __name__ == "__main__":
    main()
