# Design: Python Warehouse Inventory Manager (PY-WIM)

> **Project:** `py-wim`  
> **Phase:** System & Class Design  

---

## 1. System Architecture & Class Structure

`PY-WIM` uses a modular Object-Oriented design to separate domain models, data persistence, and application logic.

```text
PY-WIM/
├── docs/
│   ├── 01_analysis.md
│   └── 02_design.md
├── src/
│   ├── __init__.py
│   ├── models.py       # Domain Entities (StockItem)
│   ├── manager.py      # Inventory Collection & Business Logic
│   └── logger.py       # Audit Log Operations
├── data/
│   ├── stock_file.csv  # Persistent CSV Stock Records
│   └── stock_log.txt   # Timestamped Audit Logs
├── .gitignore
├── README.md
└── main.py             # CLI Application Entry Point
```

---

## 2. Domain Model Design (`src/models.py`)

### 2.1 `StockItem` Class Design

The `StockItem` class represents an individual product in the warehouse, encapsulating its attributes and validation operations.

#### Attributes
* `item_id`: `str` — Unique identifier (sanitized, uppercase).
* `name`: `str` — Descriptive product name.
* `quantity`: `int` — Current stock count ($\ge 0$).

#### Key Methods
* `__init__(item_id, name, quantity)`: Instantiates object, setting quantity to `max(0, quantity)`.
* `sell(amount: int) -> bool`: Validates `amount > 0` and `amount <= self.quantity`. Deducts stock if valid.
* `restock(amount: int) -> bool`: Validates `amount > 0`. Adds stock if valid.
* `is_low_stock(threshold: int) -> bool`: Returns `True` if `quantity < threshold`.
* `to_csv_line() -> str`: Formats item data for CSV persistence (`"ID,Name,Qty\n"`).

---

## 3. Data Structures & Efficiency Justification

### 3.1 Primary Data Structure: Python Dictionary (`dict`)
* **Mapping:** `self.inventory: Dict[str, StockItem]` where the key is `item_id`.
* **Time Complexity Justification:**
  * **Lookups / Updates:** Hash map key access yields **$O(1)$ constant time complexity**, making stock retrieval instantaneous regardless of inventory size.
  * **Alternative Comparison:** Searching a linear List requires iterating through elements with **$O(n)$ time complexity**, which does not scale efficiently for large warehouses.

---

## 4. Storage Formats & File I/O

### 4.1 Stock Data File (`data/stock_file.csv`)
Comma-separated values format:
```csv
item_id,name,quantity
A1,Hammer,15
B2,Drill,5
C3,Nails,100
D4,Ladders,2
```

### 4.2 Audit Log File (`data/stock_log.txt`)
Timestamped append-only log format:
```text
[2026-09-19 11:42:00] ACTION: SALE | ID: A1 | QTY: 2 | SUCCESS: True
[2026-09-19 11:45:12] ACTION: RESTOCK | ID: B2 | QTY: 10 | SUCCESS: True
```
---