# 💱 Currency Converter
A simple desktop GUI application that converts currency values between 20 world currencies using fixed exchange rates. Built with **Python 3** and **tkinter** — no third-party packages required.

---

## 📋 Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Module Breakdown](#module-breakdown)
- [How It Works](#how-it-works)
- [Installation & Setup](#installation--setup)
- [How to Run](#how-to-run)
- [Supported Currencies](#supported-currencies)
- [Error Handling](#error-handling)
- [Screenshots](#screenshots)
- [Requirements](#requirements)

---

## 📌 Project Overview

This application converts currency values from one country's currency to another using **fixed exchange rates** stored directly in the program.

| Detail       | Info                          |
|--------------|-------------------------------|
| Language     | Python 3.6+                   |
| GUI Library  | tkinter (built-in)            |
| Architecture | Modular (3-layer separation)  |
| Rate Source  | Static (USD base rates)       |
| Currencies   | 20 world currencies           |

---

## ✅ Features

| Feature                  | Status |
|--------------------------|--------|
| Amount input field       | ✅     |
| From currency dropdown   | ✅     |
| To currency dropdown     | ✅     |
| Convert button           | ✅     |
| Result display           | ✅     |
| Swap currencies button   | ✅     |
| Clear button             | ✅     |
| Exchange rate display    | ✅     |
| Keyboard shortcut Enter  | ✅     |
| Input validation         | ✅     |
| Error messages           | ✅     |

---

## 📁 Project Structure

```
CurrencyConverter/
│
├── main.py            ← Entry point — wires all modules together
├── rates.py           ← Data layer — exchange rates & currency names
├── converter.py       ← Logic layer — conversion formula & validation
├── ui.py              ← Presentation layer — all GUI widgets & theme
├── requirements.txt   ← Dependency notes (no pip install needed)
└── README.md          ← This file
```

---

## 🧩 Module Breakdown

### `rates.py` — Data Layer
- Stores all 20 exchange rates relative to USD = 1.0
- Stores full currency names dictionary
- Helper functions: `get_all_codes()`, `get_rate()`, `get_name()`
- **Test it:** `python3 rates.py` → prints full rates table in terminal

### `converter.py` — Logic Layer
- `convert(amount, from_code, to_code)` → performs two-step conversion
- `validate_input(raw, from, to)` → checks all error cases
- `get_exchange_rate(from, to)` → returns rate for 1 unit
- **Test it:** `python3 converter.py` → runs 3 test groups in terminal

### `ui.py` — Presentation Layer
- Defines the `Theme` class with all colours and fonts
- Widget builder functions: `build_title()`, `build_amount_input()`, `build_combo()`, `build_action_buttons()`, `build_result_card()`
- **Test it:** `python3 ui.py` → opens a styled preview window (no logic)

### `main.py` — Entry Point
- `CurrencyConverterApp` class connects UI ↔ logic
- Handles all button actions: `do_convert()`, `swap()`, `do_clear()`
- **Run it:** `python3 main.py` → launches the full application

---

## ⚙️ How It Works

Conversion uses a **two-step USD base formula**:

```
Step 1 — Normalise to USD:   usd_amount = amount / from_rate
Step 2 — Convert to target:  result     = usd_amount × to_rate
```

**Example — 100 MYR → EUR:**
```
usd    = 100 / 4.72  = 21.186 USD
result = 21.186 × 0.92 = 19.49 EUR
```

---

## 🛠️ Installation & Setup

### 1. Install Python 3
Download from [python.org](https://python.org) if not already installed.

### 2. Install tkinter (Linux/Ubuntu only)
```bash
sudo apt update
sudo apt install python3-tk
```

> **Windows / macOS:** tkinter is included with Python by default.

### 3. Verify tkinter works
```bash
python3 -m tkinter
```
A small test window should appear. ✅

### 4. Clone or download this project
```bash
git clone <your-repo-url>
cd CurrencyConverter
```

### 5. (Optional) Create a virtual environment
```bash
# Create venv AFTER installing python3-tk
python3 -m venv .venv
source .venv/bin/activate        # Linux/macOS
.venv\Scripts\activate           # Windows
```

> ⚠️ **Important:** On Ubuntu, always install `python3-tk` **before** creating your `.venv`. If you installed it after, delete and recreate the venv.

---

## ▶️ How to Run

### Run the full application
```bash
python3 main.py
```

### Test each module independently
```bash
python3 rates.py        # prints rates table
python3 converter.py    # runs conversion & validation tests
python3 ui.py           # opens GUI preview window
```

---

## 🌍 Supported Currencies

| Code | Currency              | Code | Currency            |
|------|-----------------------|------|---------------------|
| USD  | US Dollar             | MYR  | Malaysian Ringgit   |
| EUR  | Euro                  | SGD  | Singapore Dollar    |
| GBP  | British Pound         | AED  | UAE Dirham          |
| JPY  | Japanese Yen          | SAR  | Saudi Riyal         |
| INR  | Indian Rupee          | KRW  | South Korean Won    |
| AUD  | Australian Dollar     | BRL  | Brazilian Real      |
| CAD  | Canadian Dollar       | MXN  | Mexican Peso        |
| CHF  | Swiss Franc           | ZAR  | South African Rand  |
| CNY  | Chinese Yuan          | NGN  | Nigerian Naira      |
| EGP  | Egyptian Pound        | PKR  | Pakistani Rupee     |

---

## ⚠️ Error Handling

| Error Condition         | Message Shown                              |
|-------------------------|--------------------------------------------|
| Empty amount field      | Please enter an amount.                    |
| Letters in amount       | Invalid number. Please enter digits only.  |
| Zero or negative value  | Amount must be greater than zero.          |
| Same currency selected  | Please select two different currencies.    |
| No currency selected    | Please select both currencies.             |

---

## 📸 Screenshots

> _Add your app screenshots here after running it._

```
[ Place screenshot of main window here ]
[ Place screenshot of result display here ]
[ Place screenshot of error message here ]
```

---

## 📦 Requirements

| Requirement  | Detail                              |
|--------------|-------------------------------------|
| Python       | 3.6 or higher                       |
| tkinter      | Built-in (Linux: `apt install python3-tk`) |
| pip packages | **None** — no installs required     |

---

## 🚀 Future Improvements

- [ ] Fetch live exchange rates from an API (e.g. exchangerate-api.com)
- [ ] Add conversion history log
- [ ] Add dark/light theme toggle
- [ ] Package as standalone `.exe` using PyInstaller
- [ ] Add unit tests using `unittest` module

---

## 👨‍💻 Author

**Manikandan**
Python Learning Project — Currency Converter GUI