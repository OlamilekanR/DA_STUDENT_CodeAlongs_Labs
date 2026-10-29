#!/usr/bin/env python3
"""Day 1 code-along: Control Flow & Conditionals. Run: python3 <file>"""

# ===== 1. If/Elif/Else, Live =====
# Print "Too hot", "Too cold", or "Just right" based on temperature.
print('----- 1. If/Elif/Else, Live -----')
# TODO: set temperature to any number
# TODO: write the if/elif/else check yourself
temperature = 71

if temperature > 80:
    print("Too hot")
elif temperature < 60:
    print("Too cold")
else:
    print("Just right")
print("Temperature:", temperature + 6)
# ===== 2. For Loop, Live =====
# Print the four scores, one per line, so the output is 88, 92, 75, then 100.
print('----- 2. For Loop, Live -----')
# TODO: write a for loop that prints every value in scores
scores = [88, 92, 75, 100]
for i in scores: 
    if i >= 90:
        print("great job")
    else:
        print("keep practicing")
    
# ===== 3. range() Generates Numbers to Loop Over =====
# Count from 0 up to 4 with range(), one number per line. Notice it stops
# before 5.
# 1. Turn the range into an iterator
# 1. Create your range object
my_range = range(0,6)


# 2. Use len() to check the range's size, and square brackets [] to get the item
for i in my_range:
    print(i)
    
    # 3. Increment i so it doesn't loop infinitely
    i += 1


   

print('----- 3. range() Generates Numbers to Loop Over -----')
# TODO: use range() to print the numbers 0 through 4


    
# PREDICT before you run: Change range(5) to range(3). What does the loop print
#                         now?
# Your answer:
# 3 = 0,1,2

# 4 = 0,1,2,3


# ===== 4. While Loop, Live =====
# Count up from 0 and stop after 3, printing 0, 1, 2, 3.
# DISCUSS: Put these in order: A: run body. B: check again. C: first check.
# Your answer:
# 0,1,2,3

#
print('----- 4. While Loop, Live -----')
# TODO: write a while loop that prints 0, 1, 2, 3 -
count = 0
while count < 4:
    print(count)
    count = count + 1
    
# think carefully about the condition
count = 0
while count < 3:
    print(count)
    count = count + 1
# PREDICT before you run: In the While Loop, Live code above, change count <= 3
#                         to count < 3. How many numbers print?
# Your answer:
#
# 3 numbers; 0,1,2


# ===== 5. Loop and Conditional, Together =====
# Label each score: 90+ gets "great job", lower gets "keep practicing".
print('----- 5. Loop and Conditional, Together -----')
# TODO: loop over scores; print "great job" if a score is 90 or above
# TODO: otherwise print "keep practicing"
scores = [88, 92, 75, 100]
for i in scores:
    if scores > 90:
        print("Great Job")
else:
    print("Keep Practicing")