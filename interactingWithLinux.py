import os
import sys
import re
import subprocess

data_pattern = "#+[]"
left_t_patt = "[]+188+01+[0-9,A-D]"
right_t_patt = "[]+188+02+[0-9,A-D]"
accel_20_patt = "[]+244+[0-9,A-D]"

# Some things we could possibly do:
# 1) based off of what the professor said: measure baud rate ourselves?
# 2) identify how many different IDs exist in a given log file?
# 3) When working with cangen(random) traffic lets identify 
#       left/right turn signal--> ID 188#01...for left & ID 188#02...right
#        & 20 mph--> ID 244#...followed by any value above 0 will register
#        on the speedometer from my understanding, wdyt, Javier?

# traff_w_time recorded the following event: right signal(x2), left signal(x1),
# then accel to 20 then drop to zero
with open('traff_w_time', "r") as f: # its in hex
    print(f.read())                  # little over 25k lines


with open('traff_rand_gen', "r") as f: # its in hex
    print(f.read())                  # 20k lines

# At some point afterwards we could do some 
# performance checks