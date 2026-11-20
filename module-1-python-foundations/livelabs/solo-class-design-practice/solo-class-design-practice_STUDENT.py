"Tool Lending Library - FINAL v3, two borrower lists."
#Run: python3 solo-class-design-practice_STUDENT.py


  #certified_borrowers = []   # said YES to "are you certified?"
  #regular_borrowers   = []   # said NO, or never needed a cert

#Checkout, safety first:
#1. "What is your name?"
# 2. "What tool?" -> find by name, location is its shelf unique ID
#3. Stock check: 0 left -> blocked
#4. Safety check, BEFORE access:
#- safety_check True -> normal checkout
#- safety_check False -> ask "Are you certified in this? Yes or no?"
# YES -> append them to certified_borrowers, continue as normal
#  NO  -> append them to regular_borrowers, DENY access:
"Sorry, this item is off limits."
#The CSV tool stays False for everyone. Only the LIST changes.
#5. Same late fee for both lists: $5/week, capped $50.
   #  Certified does NOT pay less, regular does NOT pay more.

# Return: name + tool + shelf ID, check days late, print fee ($0 on time),+1 back to stock.

from pathlib import Path
import csv
from csv import DictReader
from collections import Counter
from dataclasses import dataclass
from datetime import date, time, datetime, timedelta
from typing import List, Dict
import json
import math







"""Lab: Solo Class Design Rep
GitBook Quest 1.8: Meet the Objects
HOW TO RUN
    Open a terminal in this file's folder and run:
        python3 solo-class-design-practice_STUDENT.py
    Or make it executable once:
        chmod +x solo-class-design-practice_STUDENT.py
    and from then on run it directly:
        ./solo-class-design-practice_STUDENT.py
    The first line, #!/usr/bin/env python3 (the "shebang"), is what
    makes ./ work. python3 <file> ignores it as a comment.

ANSWER EVERYTHING IN THIS FILE
    - Code goes under each step's banner.
    - Written answers go in # comments under each "# Your answer:"
      line.
    - Run the file after every change. It runs top to bottom, so a
      later step can use anything an earlier step made.

HINTS live in the worksheet (LiveLabOverview&Steps.md), collapsed
under each step. Open one only when you are stuck.

SUBMIT
    Commit this file (you may rename it solo-class-design-practice.py) to your own data
    challenge repo, inside your Module 1 folder. Paste its direct GitHub URL
    into the LMS.
"""

# ===== Step 1: Read the Stakeholder Need =====
# A new stakeholder need. Not the board-game or office-supply domain from
# lecture, and not one of the project's own 4 scenarios.

# Your answer:
# simple way to track each tool.
#

# ===== Step 2: Decide Your Attributes, Each With a Reason From the Scenario =====

# Your answer:
# self,name,amount_free_to_borrowed, safety_check,):
# name = identifier
# amount_free_to_borrowed = total specific tools to be borrowed
# 

# ===== Step 3: Write __init__ and a Method, From Scratch =====
# There is no single correct design here. Your class name, your attribute
# names and your method can all differ from everyone else's and still be
# right. The test is whether each one traces back to the stakeholder
# paragraph.





# TODO: Write __init__ and a Method, From Scratch
   

@dataclass
class Tool:
    name: str
    category: str
    amount_free_to_borrow: int
    safety_check: bool
    location: str
    max_loan_days: int

    def __post_init__(self):
        self.amount_free_to_borrow = int(self.amount_free_to_borrow)
        self.safety_check = self.safety_check == "True" if isinstance(self.safety_check, str) else bool(self.safety_check)
        self.max_loan_days = int(self.max_loan_days)

    def __repr__(self):
        return f"<Tool: {self.name} ({self.category}) - {self.amount_free_to_borrow} available>"


@dataclass
class Borrower:
    # Rewritten 2026-11-15 by Lekan: NO list inserts.
    # Certified is just Yes or No. No semicolon list in the CSV.
    name: str
    certified: bool = False

    def __post_init__(self):
        # CSV gives us "Yes" / "No" as text. Turn it into a real bool.
        if isinstance(self.certified, str):
            self.certified = self.certified.strip().lower() == "yes"


@dataclass
class Loan:
    tool_name: str
    borrower: str
    location: str
    checked_out_at: datetime
    due_at: datetime
    certified_override: bool = False

    def is_overdue(self, now: datetime = None) -> bool:
        return (now or datetime.now()) > self.due_at

    def days_late(self, now: datetime = None) -> int:
        return max(0, ((now or datetime.now()) - self.due_at).days)

    def late_fee(self, config: Dict, now: datetime = None) -> float:
        lib = config["library"]
        weeks = self.days_late(now) // 7
        return min(weeks * lib.get("late_fee_per_week", 5),lib.get("late_fee_cap_per_item", 50))


# ===== Step 4: Instantiate 2+ Objects, Confirm Independent Storage =====
# The same proof Day 13's lecture asked for, now on a class you designed
# yourself. Predict what each print() will show before you run it.

# TODO: Instantiate 2+ Objects, Confirm Independent Storage

#Power_tool1 = tool_lending_library("Drill",5, True)
#Power_tool2 = tool_lending_library("Saw",9, True)
#ladder1 = tool_lending_library("Step",8, False)
#ladder2 = tool_lending_library("Platform",3, True)
#Pressure_washer1 = tool_lending_library("Cordless",2, True)
#Pressure_washer2 = tool_lending_library("Corded",1, False)
# ===== Step 5: Justify Your Design Choice in 2-3 Sentences =====

# Your answer:
# I chose common household power tools for conventional translations; between the consumer and Stakeholder.
#

# ----- Share Out -----
# Last 15 minutes, back together as a class. Bring:
#
# Come ready to show your class and defend it. Specifically:
# - The attribute list you chose, and for each one, the phrase in the
#   coordinator's request it came from. If you can't point at a phrase for
#   an attribute, say so - that's a real finding, not a failure.
# - One attribute you considered and rejected, and why. - Your method: what
#   question does it answer, and why would the coordinator reach for it
#   first?
# - Anything you got stuck on. Designing from a paragraph with nobody to
#   check against is genuinely hard, and naming where it was hard is worth
#   more to the room than a tidy answer.






























# Expect to be asked "why that attribute and not another?" - there is no
# single right list here, so the reasoning IS the answer.
#
# Be ready to answer "why did you do it that way?"

# Your notes for the share out:
# To make it deployable, in a scenerio. The point of this school is not only to learn, rather it is the implementation of learning.
# The config json is to allow the developer to be able to change settings rather than hardcoding it. I experienced it during my data conversion; I had a syntax error attached to the end of the last field and if kept would drop an error. 2 ways left to fix either manually or write a code aned thus the reasoning for the json config.

def load_config(path: Path = Path(__file__).resolve().parent / "config.json") -> Dict:
    with open(path, mode="r", encoding="utf-8") as file:
        return json.load(file)

def save_config(config: Dict, path: Path = Path(__file__).resolve().parent / "config.json") -> None:
    with open(path, mode="w", encoding="utf-8") as file:
        json.dump(config, file, indent=2, ensure_ascii=False)

def load_tools(path: Path) -> List[Tool]:
    tools: List[Tool] = []
    with open(path, mode="r", encoding="utf-8", newline="") as file:
        reader = DictReader(file)
        for row in reader:
            if not row.get("name") or row["name"] == "}":
                continue
            tools.append(Tool(**row))
    return tools


