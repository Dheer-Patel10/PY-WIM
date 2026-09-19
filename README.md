# PY-WIM

> **Python Warehouse Inventory Manager**  
> A modular, Object-Oriented Python application for reliable stock management, transaction auditing, and safe persistence.

---

## 📌 Overview

`PY-WIM` is designed to streamline inventory tracking for smaller warehouse managers and retail supervisors. It addresses common manual inventory issues—such as lack of data validation, missing audit trails, and stockout risks—by leveraging OOP principles and fast in-memory dictionary data structures.

---

## ✨ Features

* **Data Validation:** Enforces non-negative stock counts and prevents empty or malformed item records.
* **$O(1)$ Fast Lookups:** Memory state mapped via Python dictionaries for constant-time key access.
* **CSV Persistence:** Reads and writes inventory state safely to `data/stock_file.csv`.
* **Transaction Auditing:** Automatically appends timestamped actions (`SALE`, `RESTOCK`) to `data/stock_log.txt`.
* **Low-Stock Alerting:** Identifies items falling below configurable safety thresholds.

---

## 📁 Repository Structure

```text
PY-WIM/
├── docs/               # OCR A-Level CS NEA Documentation
│   ├── 01_analysis.md
│   └── 02_design.md
├── src/                # Modular Source Code
│   ├── __init__.py
│   ├── models.py       # Domain Entities (StockItem)
│   ├── manager.py      # Inventory Management Logic
│   └── logger.py       # Audit Trail Logger
├── data/               # Persistent Storage
│   ├── stock_file.csv  # Inventory CSV File
│   └── stock_log.txt   # Timestamped Audit Logs
├── .gitignore
├── README.md
└── main.py             # Application Entry Point