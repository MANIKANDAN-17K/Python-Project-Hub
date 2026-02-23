"""
converter.py — Conversion Logic Module
========================================
Handles all currency conversion calculations and validation.
No GUI code here — pure logic only.
This module can be imported OR run directly to test conversions.

Usage:
    python converter.py
"""

from rates import RATES


# ──────────────────────────────────────────
#  CONVERSION FUNCTION
# ──────────────────────────────────────────

def convert(amount, from_code, to_code):
    """
    Convert an amount from one currency to another.

    How it works (two-step via USD base):
        Step 1: from_currency → USD   →  usd = amount / from_rate
        Step 2: USD → to_currency     →  result = usd * to_rate

    Parameters:
        amount    (float) : the value to convert
        from_code (str)   : source currency e.g. "USD"
        to_code   (str)   : target currency e.g. "MYR"

    Returns:
        float : converted result

    Raises:
        ValueError : if currency code is not found in RATES
    """
    from_code = from_code.upper()
    to_code   = to_code.upper()

    if from_code not in RATES:
        raise ValueError(f"Unknown currency code: '{from_code}'")
    if to_code not in RATES:
        raise ValueError(f"Unknown currency code: '{to_code}'")

    usd_amount = amount / RATES[from_code]   # Step 1 — normalise to USD
    result     = usd_amount * RATES[to_code] # Step 2 — convert to target

    return round(result, 4)


def get_exchange_rate(from_code, to_code):
    """
    Return how much 1 unit of from_code equals in to_code.
    Example: get_exchange_rate("USD", "MYR") → 4.72
    """
    return convert(1.0, from_code, to_code)


# ──────────────────────────────────────────
#  VALIDATION FUNCTION
# ──────────────────────────────────────────

def validate_input(raw_amount, from_code, to_code):
    """
    Validate user inputs before converting.

    Returns:
        (True,  float,   "")            on success
        (False, None,  "error message") on failure
    """
    # Check 1 — empty amount
    if not raw_amount or raw_amount.strip() == "":
        return False, None, "Please enter an amount."

    # Check 2 — numeric check
    try:
        amount = float(raw_amount)
    except ValueError:
        return False, None, "Invalid number. Please enter digits only."

    # Check 3 — positive number
    if amount <= 0:
        return False, None, "Amount must be greater than zero."

    # Check 4 — currencies selected
    if not from_code or not to_code:
        return False, None, "Please select both currencies."

    # Check 5 — same currency
    if from_code.upper() == to_code.upper():
        return False, None, "Please select two different currencies."

    return True, amount, ""


# ──────────────────────────────────────────
#  TERMINAL TEST  (run: python converter.py)
# ──────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 55)
    print("  MODULE: converter.py — Conversion Logic")
    print("=" * 55)

    # --- Test conversions ---
    test_cases = [
        (100,  "USD", "MYR"),
        (100,  "MYR", "USD"),
        (50,   "USD", "EUR"),
        (1000, "JPY", "INR"),
        (200,  "GBP", "AED"),
        (500,  "INR", "PKR"),
    ]

    print("\n  [TEST 1] Conversion Results")
    print(f"  {'AMOUNT':<10} {'FROM':<6} {'TO':<6}  {'RESULT':>12}")
    print(f"  {'-'*10} {'-'*6} {'-'*6}  {'-'*12}")

    for amount, frm, to in test_cases:
        result = convert(amount, frm, to)
        print(f"  {amount:<10} {frm:<6} {to:<6}  {result:>12.4f}")

    # --- Test exchange rates ---
    print("\n  [TEST 2] Exchange Rates (1 unit)")
    pairs = [("USD","MYR"), ("USD","EUR"), ("USD","JPY"), ("EUR","GBP")]
    for f, t in pairs:
        rate = get_exchange_rate(f, t)
        print(f"  1 {f} = {rate:.4f} {t}")

    # --- Test validation ---
    print("\n  [TEST 3] Input Validation")
    validations = [
        ("",      "USD", "MYR", "Empty amount"),
        ("abc",   "USD", "MYR", "Non-numeric"),
        ("-50",   "USD", "MYR", "Negative number"),
        ("100",   "USD", "USD", "Same currency"),
        ("100",   "",    "MYR", "Missing from"),
        ("100",   "USD", "MYR", "Valid input"),
    ]

    for raw, f, t, label in validations:
        ok, val, msg = validate_input(raw, f, t)
        status = "✅ PASS" if ok else f"❌ {msg}"
        print(f"  [{label:<18}]  {status}")

    print()
    print("  ✅ converter.py loaded and tested successfully!")
    print("=" * 55)