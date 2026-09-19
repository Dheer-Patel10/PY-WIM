# Analysis: Python Warehouse Inventory Manager (PY-WIM)

> **Project:** `py-wim`  
> **Target Audience:** Small warehouse managers, stock clerks, and retail workshop supervisors  
> **Architecture:** Modular, Object-Oriented Python Application  

---

## 1. Problem Definition

### 1.1 Real-World Warehouse Bottlenecks
Manual inventory logs are time-consuming to maintain and introduce a significant risk of human error. Small firms typically rely on paper logs, basic spreadsheets, or unstructured text files, leading to inaccurate stock records and operational delays.

### 1.2 Key System Failures
* **Lack of Data Validation:** Existing workflows allow invalid data entries, such as negative stock counts, empty product names, or malformed product IDs.
* **Absence of Audit Logs:** There is no mechanism to track who altered stock levels, what changes were made, or when transactions occurred.
* **Risk of Stockouts:** Manual tracking lacks automated low-stock warnings, increasing the likelihood of unmonitored inventory shortages.

---

## 2. Proposed Solution

`PY-WIM` is a modular, Object-Oriented Python application designed to make stock management reliable, fast, and error-free.

### Key Architectural Features
* **Encapsulated OOP Domain:** A robust `StockItem` class with strict built-in validation methods.
* **High-Efficiency Memory State:** Dictionary-based inventory mapping enabling $O(1)$ constant-time lookups.
* **Persistent File Storage:** Safe file read and write operations to protect data integrity across sessions.
* **Automated Audit Logging:** Instant logging of every stock modification to an external append-only log file.

---

## 3. System Inputs, Processing & Outputs

### 3.1 Inputs (Domain)
* **Item Metadata:** `item_id` (string), `name` (string), and `quantity` (integer).
* **User Commands:** Search queries, transaction actions (`sell`, `restock`), and menu navigation choices.
* **Persistent Files:** Formatted CSV data strings loaded directly from `data/stock_file.txt`.

### 3.2 Processing
* **Input Validation:** Enforces non-negative stock constraints, sanitizes strings, and validates ID formats.
* **State Management:** Mutates active in-memory `StockItem` properties strictly through validated class methods.
* **Direct Lookups:** Uses hash-map key indexing to access inventory records in $O(1)$ time complexity.

### 3.3 Outputs (Range)
* **CLI Interface:** Structured terminal displays for inventory tables, transaction status feedback, and low-stock alerts.
* **Persistent Storage:** Sanitized CSV records written back to `data/stock_file.txt`.
* **Audit Logs:** Timestamped transaction history entries appended to `data/stock_log.txt`.

---

## 4. Measurable Success Criteria

1. **Validation & Error Handling:** The system must reject invalid user inputs (such as negative stock quantities or empty item names) without raising unhandled Python exceptions.
2. **Encapsulation:** The core domain (`StockItem`) must encapsulate data changes through methods (`.sell()`, `.restock()`) rather than direct attribute mutation from external scripts.
3. **Lookup Efficiency:** The system must use dictionary key mapping to ensure active stock lookups operate at $O(1)$ time complexity.
4. **Low Stock Alerting:** The manager must automatically generate a filtered list of all inventory items where quantity falls below a configurable threshold.
5. **Persistence & Auditing:** Every transaction (sale or restock) must instantly write a timestamped record to `data/stock_log.txt` and save updated state to `data/stock_file.txt`.