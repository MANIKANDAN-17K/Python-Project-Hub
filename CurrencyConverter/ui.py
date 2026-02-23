"""
ui.py — GUI Layout & Widget Module
=====================================
Builds all visual widgets: window, labels, inputs, buttons, dropdowns.
No conversion logic here — pure GUI construction only.
Run directly to preview the styled empty window.

Usage:
    python ui.py
"""

import tkinter as tk
from tkinter import ttk
from rates import get_all_codes, CURRENCY_NAMES


# ──────────────────────────────────────────
#  THEME / COLOUR CONSTANTS
# ──────────────────────────────────────────

class Theme:
    BG           = "#1E1E2E"   # main background
    CARD         = "#2A2A3E"   # input / card background
    ACCENT       = "#7C3AED"   # purple button
    ACCENT_HOVER = "#9D5FFF"   # purple hover
    TEXT         = "#E2E8F0"   # primary text
    SUBTEXT      = "#94A3B8"   # secondary / placeholder text
    SUCCESS      = "#10B981"   # green result
    ERROR        = "#F87171"   # red error
    BORDER       = "#3B3B52"   # subtle border

    FONT_TITLE   = ("Georgia",    22, "bold")
    FONT_LABEL   = ("Helvetica",  10)
    FONT_ENTRY   = ("Courier",    14)
    FONT_BUTTON  = ("Helvetica",  11, "bold")
    FONT_RESULT  = ("Georgia",    16, "bold")
    FONT_SMALL   = ("Helvetica",   9)


# ──────────────────────────────────────────
#  DISPLAY NAME HELPERS
# ──────────────────────────────────────────

def make_display_list():
    """Return list like ['USD — US Dollar', 'EUR — Euro', ...]"""
    return [f"{c} — {CURRENCY_NAMES.get(c, c)}" for c in get_all_codes()]

def code_from_display(display_str):
    """Extract 'USD' from 'USD — US Dollar'."""
    return display_str.split("—")[0].strip()


# ──────────────────────────────────────────
#  WIDGET BUILDER FUNCTIONS
# ──────────────────────────────────────────

def setup_window(root):
    """Configure the main window: size, title, colour, position."""
    root.title("Currency Converter")
    root.resizable(False, False)
    root.configure(bg=Theme.BG)

    width, height = 420, 580
    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()
    x  = (sw - width) // 2
    y  = (sh - height) // 2
    root.geometry(f"{width}x{height}+{x}+{y}")


def build_title(parent):
    """Create title and subtitle labels."""
    tk.Label(
        parent, text="💱 Currency Converter",
        font=Theme.FONT_TITLE, bg=Theme.BG, fg=Theme.TEXT
    ).pack(pady=(30, 4))

    tk.Label(
        parent, text="Fixed exchange rates · USD base",
        font=Theme.FONT_SMALL, bg=Theme.BG, fg=Theme.SUBTEXT
    ).pack(pady=(0, 20))


def build_amount_input(parent):
    """Create the amount input field. Returns StringVar."""
    tk.Label(parent, text="Amount", font=Theme.FONT_LABEL,
             bg=Theme.BG, fg=Theme.SUBTEXT).pack(anchor="w", padx=30)

    amount_var = tk.StringVar()

    frame = tk.Frame(parent, bg=Theme.CARD,
                     highlightbackground=Theme.BORDER, highlightthickness=1)
    frame.pack(fill="x", padx=30, pady=(2, 14))

    entry = tk.Entry(
        frame, textvariable=amount_var,
        font=Theme.FONT_ENTRY, bg=Theme.CARD, fg=Theme.TEXT,
        insertbackground=Theme.TEXT, relief="flat", bd=10
    )
    entry.pack(fill="x")

    return amount_var, entry


def build_combo(parent, label_text, default_code):
    """Create a labelled currency dropdown. Returns StringVar."""
    display_list = make_display_list()

    tk.Label(parent, text=label_text, font=Theme.FONT_LABEL,
             bg=Theme.BG, fg=Theme.SUBTEXT).pack(anchor="w", padx=30)

    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Dark.TCombobox",
        fieldbackground=Theme.CARD, background=Theme.CARD,
        foreground=Theme.TEXT, selectbackground=Theme.ACCENT,
        selectforeground="white", bordercolor=Theme.BORDER,
        arrowcolor=Theme.SUBTEXT, relief="flat", padding=8)

    var = tk.StringVar()
    combo = ttk.Combobox(
        parent, textvariable=var, values=display_list,
        state="readonly", style="Dark.TCombobox", font=Theme.FONT_LABEL
    )
    default_display = f"{default_code} — {CURRENCY_NAMES.get(default_code, '')}"
    var.set(default_display)
    combo.pack(fill="x", padx=30, pady=(2, 14))

    return var, combo


def build_swap_button(parent, command):
    """Create the swap currencies button."""
    row = tk.Frame(parent, bg=Theme.BG)
    row.pack(pady=(0, 4))
    btn = tk.Button(
        row, text="⇅  Swap Currencies",
        font=Theme.FONT_SMALL, bg=Theme.CARD, fg=Theme.SUBTEXT,
        relief="flat", cursor="hand2", bd=0,
        activebackground=Theme.CARD, activeforeground=Theme.TEXT,
        command=command
    )
    btn.pack()
    return btn


def build_action_buttons(parent, convert_cmd, clear_cmd):
    """Create Convert and Clear buttons side by side."""
    row = tk.Frame(parent, bg=Theme.BG)
    row.pack(pady=(4, 20), padx=30, fill="x")

    convert_btn = tk.Button(
        row, text="Convert →",
        font=Theme.FONT_BUTTON, bg=Theme.ACCENT, fg="white",
        relief="flat", cursor="hand2", bd=0,
        activebackground=Theme.ACCENT_HOVER, activeforeground="white",
        padx=20, pady=10, command=convert_cmd
    )
    convert_btn.pack(side="left", expand=True, fill="x", padx=(0, 6))

    clear_btn = tk.Button(
        row, text="Clear",
        font=Theme.FONT_BUTTON, bg=Theme.CARD, fg=Theme.SUBTEXT,
        relief="flat", cursor="hand2", bd=0,
        activebackground=Theme.BORDER, activeforeground=Theme.TEXT,
        padx=20, pady=10, command=clear_cmd
    )
    clear_btn.pack(side="left")

    return convert_btn, clear_btn


def build_result_card(parent):
    """Create the result display card. Returns result_var and rate_var."""
    card = tk.Frame(parent, bg=Theme.CARD,
                    highlightbackground=Theme.BORDER, highlightthickness=1)
    card.pack(fill="x", padx=30, pady=(0, 10))

    result_var = tk.StringVar(value="Result will appear here")
    result_label = tk.Label(
        card, textvariable=result_var,
        font=Theme.FONT_RESULT, bg=Theme.CARD, fg=Theme.SUBTEXT,
        wraplength=340, justify="center", pady=18
    )
    result_label.pack()

    rate_var = tk.StringVar(value="")
    tk.Label(card, textvariable=rate_var, font=Theme.FONT_SMALL,
             bg=Theme.CARD, fg=Theme.SUBTEXT, pady=4).pack()

    return result_var, rate_var, result_label


# ──────────────────────────────────────────
#  TERMINAL TEST  (run: python ui.py)
# ──────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 50)
    print("  MODULE: ui.py — GUI Layout & Widgets")
    print("=" * 50)
    print()
    print("  Launching preview window (no logic attached)...")
    print("  Close the window to exit.")
    print()

    root = tk.Tk()
    setup_window(root)
    build_title(root)

    amount_var, entry = build_amount_input(root)
    from_var, _       = build_combo(root, "From", "USD")
    build_swap_button(root, lambda: print("  [SWAP clicked]"))
    to_var, _         = build_combo(root, "To", "MYR")
    build_action_buttons(
        root,
        lambda: print("  [CONVERT clicked]"),
        lambda: print("  [CLEAR clicked]")
    )
    build_result_card(root)

    # Print widget info to terminal
    print("  Widgets created:")
    print(f"    Amount input  → StringVar id: {id(amount_var)}")
    print(f"    From dropdown → default: {from_var.get()}")
    print(f"    To   dropdown → default: {to_var.get()}")
    print(f"    Display list  → {len(make_display_list())} currencies")
    print()
    print("  ✅ ui.py loaded successfully!")
    print("=" * 50)

    root.mainloop()