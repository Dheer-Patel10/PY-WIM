from src.manager import InventoryManager


def test_add_and_sell_item():
    manager = InventoryManager()

    assert manager.add_item("m9", "Widget", 10) is True
    assert manager.add_item("M9", "Duplicate", 5) is False

    assert manager.sell_item("m9", 3) is True
    assert manager.get_item("M9").quantity == 7
