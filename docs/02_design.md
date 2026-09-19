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