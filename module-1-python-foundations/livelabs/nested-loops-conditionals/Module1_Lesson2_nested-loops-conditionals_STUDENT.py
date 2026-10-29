#!/usr/bin/env python3
"""Day 2 code-along: Nested Loops & Conditionals. Run: python3 <file>"""

# ===== 1. Nested Loop, Live =====
# Print all six row and column pairs, starting at 0 0 and ending at 1 2.
# DISCUSS: If both loops used range(2), order: A: 1 0. B: 0 0. C: 1 1. D: 0 1.
# Your answer:
#
print('----- 1. Nested Loop, Live -----')
<<<<<<< HEAD
# TODO: write a nested loop that prints every (row, col) pair
# TODO: row goes through range(2), col through range(3)

# PREDICT before you run: Outer range(3), inner range(2): how many lines print?
# Your answer:
#
# DISCUSS: A classmate gets 3 lines instead of 6. What's the likely cause?
# Your answer:
=======
# TODO: write a nested loop that prints every (row, col)
# pair for row in range(2) and col in range(3)
for row in range(2):
    for col in range(3):
        print(row, col)
# PREDICT before you run: Change the Nested Loop code to range(3) on the
#                         outside and range(2) on the inside. How many lines
#                         print?
# Your answer:
for row in range(3):
    for col in range(2):
        print(row, col)
#
#
# DISCUSS: With range(3) outside and range(2) inside, a classmate's version
#          prints only 3 lines instead of 6. What's the most likely cause?
# Your answer:
# print is indented outer range only runs.
>>>>>>> 3a59e7fa748762b972938156985c6b14cc504f56
#


# ===== 2. Nested Conditional, Live =====
# Check the operation type first, then if the quantity is positive.
print('----- 2. Nested Conditional, Live -----')
<<<<<<< HEAD
# TODO: check operation first
# TODO: if it's "ADD", nest a second check that quantity is above 0
operation = "ADD"
quantity = -5

# DISCUSS: If the inner quantity check never runs, what do you trace first?
# Your answer:
#
=======
# TODO: check operation first; if it's "ADD", nest a second
# check confirming quantity is greater than 0

operation = "ADD"
quantity = -5

if operation == "ADD":
    if quantity > 0:
        print("Adding quantity")
    else:
        print("Invalid quantity")
# DISCUSS: Suppose the inner quantity check in the Nested Conditional code
#          never seems to run. What should you trace first? Try it: set
#          operation to "SEARCH" and run.
# Your answer:
#
# 
operation = "SEARCH"
quantity = -5

if operation == "ADD":
    if quantity > 0:
        print("Adding quantity")
    else:
        print("Invalid quantity")
>>>>>>> 3a59e7fa748762b972938156985c6b14cc504f56


# ===== 3. Putting It Together: Loop + Nested Conditional =====
# Check each line: print whether it is valid, a bad quantity, or a remove.
print('----- 3. Putting It Together: Loop + Nested Conditional -----')
<<<<<<< HEAD
# TODO: loop over transactions; split each into operation and amount
# TODO: put the nested ADD/quantity check inside the loop
transactions = ["ADD 10", "REMOVE 3", "ADD -5"]
=======
# TODO: loop over transactions; for each line, split it into
# operation and amount, then nest the ADD/quantity check
# from the nested-conditional step inside the loop
transactions = ["Add 10","Remove 3","Add -5"]
for item in transactions:
    operation,quantity = item.split()
    quantity = int(quantity)
    if operation == "Add":
        if quantity > 0:
            print(item, "-valid quantity")
        else: 
            print(item, "-invalid quantity")
    elif operation == "Remove": 
            print(item, "-Processing Remove")
>>>>>>> 3a59e7fa748762b972938156985c6b14cc504f56

# PREDICT before you run: Which check flags "ADD -5" as invalid?
# Your answer:
#
