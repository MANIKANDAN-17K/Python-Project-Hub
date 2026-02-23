"""
rates.py — Exchange Rate Data Module
======================================
Stores all currency exchange rates relative to USD = 1.0.
This module can be imported by other modules OR run directly
to test/display all available rates in the terminal.

Usage:
    python rates.py
"""

# ──────────────────────────────────────────
#  EXCHANGE RATES  (Base: 1 USD = 1.0)
# ──────────────────────────────────────────

RATES = {
    "USD": 1.0,
    "EUR": 0.92,
    "GBP": 0.79,
    "JPY": 149.50,
    "INR": 83.12,
    "AUD": 1.53,
    "CAD": 1.36,
    "CHF": 0.88,
    "CNY": 7.24,
    "MYR": 4.72,
    "SGD": 1.34,
    "AED": 3.67,
    "SAR": 3.75,
    "KRW": 1325.0,
    "BRL": 4.97,
    "MXN": 17.15,
    "ZAR": 18.63,
    "NGN": 1550.0,
    "EGP": 30.90,
    "PKR": 278.0,
}

CURRENCY_NAMES = {
    "USD": "US Dollar",
    "EUR": "Euro",
    "GBP": "British Pound",
    "JPY": "Japanese Yen",
    "INR": "Indian Rupee",
    "AUD": "Australian Dollar",
    "CAD": "Canadian Dollar",
    "CHF": "Swiss Franc",
    "CNY": "Chinese Yuan",
    "MYR": "Malaysian Ringgit",
    "SGD": "Singapore Dollar",
    "AED": "UAE Dirham",
    "SAR": "Saudi Riyal",
    "KRW": "South Korean Won",
    "BRL": "Brazilian Real",
    "MXN": "Mexican Peso",
    "ZAR": "South African Rand",
    "NGN": "Nigerian Naira",
    "EGP": "Egyptian Pound",
    "PKR": "Pakistani Rupee",
}

def get_all_codes():
    """Return sorted list of all currency codes."""
    return sorted(RATES.keys())

def get_rate(code):
    """Return the exchange rate for a given currency code."""
    return RATES.get(code.upper(), None)

def get_name(code):
    """Return the full name of a currency."""
    return CURRENCY_NAMES.get(code.upper(), "Unknown Currency")


# ──────────────────────────────────────────
#  TERMINAL TEST  (run: python rates.py)
# ──────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 50)
    print("  MODULE: rates.py — Exchange Rate Data")
    print("=" * 50)
    print(f"  Total currencies loaded : {len(RATES)}")
    print(f"  Base currency           : USD = 1.0")
    print()
    print(f"  {'CODE':<6} {'RATE':>10}   FULL NAME")
    print(f"  {'-'*6} {'-'*10}   {'-'*20}")

    for code in sorted(RATES.keys()):
        rate = RATES[code]
        name = CURRENCY_NAMES.get(code, "?")
        print(f"  {code:<6} {rate:>10.4f}   {name}")

    print()
    print("  ✅ rates.py loaded successfully!")
    print("=" * 50)