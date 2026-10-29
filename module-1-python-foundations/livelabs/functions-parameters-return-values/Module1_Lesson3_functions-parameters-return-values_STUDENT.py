#!/usr/bin/env python3
"""Day 3 code-along: Functions, Parameters & Return.... Run: python3 <file>"""

# ===== 1. Define and Call, Live =====
# Build a reusable greeting: one function, called twice, prints it twice.
print('----- 1. Define and Call, Live -----')
<<<<<<< HEAD
# TODO: define greet() to print a welcome message, then call it twice


# ===== 2. Parameters, Live =====
# Make greet work for anyone: pass in a name, then greet Jordan and Amara.
print('----- 2. Parameters, Live -----')
# TODO: add a name parameter to greet
# TODO: print a personal welcome for each of 2 names
=======
# TODO: define a function named greet that prints a welcome
# message, then call it twice
def greet(n):

    print("Welcome\n" * n, end="")
greet(2)


# ===== 2. Parameters, Live =====
# Make greet work for anyone: ask for a name and print a personal welcome.
print('----- 2. Parameters, Live -----')
# TODO: add a name parameter to greet, and print a
# personalized welcome message
def greet(name):
    print(f"Welcome, {name}!")

my_name = input("What is your name? ")
greet(my_name)
>>>>>>> 3a59e7fa748762b972938156985c6b14cc504f56

# DISCUSS: Order double(5): A: n becomes 5. B: body runs. C: it gets called.
# Your answer:
<<<<<<< HEAD
#
# PREDICT before you run: If double(n) prints n * 2, what does double(5) print?
# Your answer:
=======
# A,C,B
#
#
# PREDICT before you run: Given def double(n): print(n * 2), what does
#                         double(5) print?
# Your answer:
# 10
>>>>>>> 3a59e7fa748762b972938156985c6b14cc504f56
#


# ===== 3. Return, Live =====
# Send a value back with return to use it in math. double(5) + 1 prints 11.
print('----- 3. Return, Live -----')
<<<<<<< HEAD
# TODO: write double(n) using return (not print)
# TODO: add 1 to its result and print that
=======
# TODO: write double(n) using return (not print), then use
# its result in an expression - add 1 to it and print that
def double(n):
   total = n * 2
   print(total + 1)
   return total
print  (double(5) + 1)

>>>>>>> 3a59e7fa748762b972938156985c6b14cc504f56

# DISCUSS: A doubling function's result + 1 raises TypeError. Likely cause?
# Your answer:
#
<<<<<<< HEAD
=======
# total + 1 is probably placed outside the return function making it not part of the double function.
>>>>>>> 3a59e7fa748762b972938156985c6b14cc504f56
