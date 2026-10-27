#!/usr/bin/env python3
"""Day 4 code-along: Local vs. Global Variables & Scope. Run: python3 <file>"""

# ===== 1. Local Scope, Live =====
# Find out if a variable made inside a function exists outside it.
# TODO: run it, read the NameError, then comment out the raising line
# DISCUSS: Order: A: total disappears. B: make_total() runs. C: total = 100.
# Your answer:
#
print('----- 1. Local Scope, Live -----')
# TODO: define make_total() with a local variable total set
# to 100, returning it, then try printing total outside the
# function and watch what happens
def make_total():
    total = 100
    return total
make_total()
print(total) # NameError: total isn't defined here
print(total) # NameError: total isn't defined here

# DISCUSS: set_x() sets x = 5, but print(x) outside raises NameError. Why?
# Your answer:
#


# ===== 2. Reading a Global, Live =====
# Price a $100 item with 8% tax, using a tax rate stored outside the function.
print('----- 2. Reading a Global, Live -----')
# TODO: define tax_rate as a global, then write
# price_with_tax(price) that reads it without taking it as
# a parameter
tax_rate = 0.08

def price_with_tax(price):
    total = price + (price * tax_rate)
    return total

print(price_with_tax(100))  # 108.0

# DISCUSS: Move price_with_tax to a file with no tax_rate. Why does it break?
# Your answer:
#


# ===== 3. Refactor: Global to Parameter =====
# Pass the tax rate in as a parameter. It should still print 108.0.
print('----- 3. Refactor: Global to Parameter -----')
# TODO: rewrite price_with_tax to take tax_rate as a parameter
tax_rate = 0.08
def price_with_tax(price, tax_rate):
    return price + (price * tax_rate)
print(price_with_tax(100, tax_rate))