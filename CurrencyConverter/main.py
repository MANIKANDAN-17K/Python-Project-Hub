"""
main.py — Application Entry Point
====================================
Wires together all modules:
    rates.py     → exchange rate data
    converter.py → conversion logic & validation
    ui.py        → GUI widgets & layout

Run this file to launch the full application.

Usage:
    python main.py
"""

import tkinter as tk
from converter import convert, validate_input, get_exchange_rate
from ui import (
    Theme, setup_window, build_title, build_amount_input,
    build_combo, build_swap_button, build_action_buttons,
    build_result_card, code_from_display
)


# ──────────────────────────────────────────
#  APPLICATION CONTROLLER CLASS
# ──────────────────────────────────────────

class CurrencyConverterApp:
    """
    Controller — connects UI widgets to conversion logic.
    Reads inputs from ui.py → calls converter.py → updates result display.
    """

    def __init__(self, root):
        self.root = root

        # ── Build window & all widgets ──
        setup_window(root)
        build_title(root)

        self.amount_var, self.amount_entry = build_amount_input(root)
        self.from_var,   _                 = build_combo(root, "From", "USD")
        build_swap_button(root, self.swap)
        self.to_var,     _                 = build_combo(root, "To",   "MYR")
        build_action_buttons(root, self.do_convert, self.do_clear)
        self.result_var, self.rate_var, self.result_label = build_result_card(root)

        # ── Keyboard shortcut ──
        root.bind("<Return>", lambda e: self.do_convert())

        self.amount_entry.focus()

    # ──────────────────────────────────────
    #  CONVERT ACTION
    # ──────────────────────────────────────

    def do_convert(self):
        """Read inputs → validate → convert → display result."""
        raw_amount   = self.amount_var.get().strip()
        from_display = self.from_var.get()
        to_display   = self.to_var.get()

        from_code = code_from_display(from_display)
        to_code   = code_from_display(to_display)

        # Validate inputs via converter module
        ok, amount, error_msg = validate_input(raw_amount, from_code, to_code)

        if not ok:
            self._show_error(error_msg)
            return

        # Convert via converter module
        result = convert(amount, from_code, to_code)

        # Format numbers nicely
        fmt_input  = f"{amount:,.2f}"
        fmt_result = f"{result:,.4f}" if result < 1 else f"{result:,.2f}"

        self.result_var.set(f"{fmt_input} {from_code}  =  {fmt_result} {to_code}")
        self.result_label.config(fg=Theme.SUCCESS)

        # Show exchange rate info
        rate = get_exchange_rate(from_code, to_code)
        self.rate_var.set(f"1 {from_code} = {rate:.4f} {to_code}")

    # ──────────────────────────────────────
    #  SWAP ACTION
    # ──────────────────────────────────────

    def swap(self):
        """Swap From and To currencies, then re-convert if amount exists."""
        from_val = self.from_var.get()
        to_val   = self.to_var.get()
        self.from_var.set(to_val)
        self.to_var.set(from_val)

        if self.amount_var.get().strip():
            self.do_convert()

    # ──────────────────────────────────────
    #  CLEAR ACTION
    # ──────────────────────────────────────

    def do_clear(self):
        """Reset all fields to default state."""
        self.amount_var.set("")
        self.result_var.set("Result will appear here")
        self.result_label.config(fg=Theme.SUBTEXT)
        self.rate_var.set("")
        self.amount_entry.focus()

    # ──────────────────────────────────────
    #  HELPERS
    # ──────────────────────────────────────

    def _show_error(self, message):
        """Display an error message inside the result card."""
        self.result_var.set(message)
        self.result_label.config(fg=Theme.ERROR)
        self.rate_var.set("")


# ──────────────────────────────────────────
#  ENTRY POINT
# ──────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 50)
    print("  MODULE: main.py — Application Entry Point")
    print("=" * 50)
    print()
    print("  Modules loaded:")
    print("    ✅ rates.py     → exchange rate data")
    print("    ✅ converter.py → conversion logic")
    print("    ✅ ui.py        → GUI widgets")
    print()
    print("  Starting Currency Converter GUI...")
    print("  Close the window to exit.")
    print("=" * 50)

    root = tk.Tk()
    CurrencyConverterApp(root)
    root.mainloop()

    print()
    print("  Application closed.")