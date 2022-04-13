import os
import sys
import re
import subprocess
#import numpy as np
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
#        on the speedometer from my understanding, wdyt?

# traff_w_time recorded the following event: right signal(x2), left signal(x1),
# then accel to 20 then drop to zero

with open('traff_w_time', "r") as f: # its in hex
    packets_time = f.readlines()
    #print(f.read())                  # little over 25k lines
with open('traff_rand_gen', "r") as f: # its in hex
    packets_rand = f.readlines()                  # 20k lines

def firstNode(logFile):
    per_line = [i.split(' ') for i in logFile]
    curr_nodeID = per_line[0][2][:3]
    print('first line', per_line[0])
    print('Current ID', curr_nodeID)

# Using a dictionary here is the best approach IMO..
def allNodesEncountered(logFile):
    d = dict()
    for l in logFile:
        per_line = l.split(" ")
        node = per_line[2][:3]
        if node in d:
              # if already there, then simply update
            d[node] = d[node] + 1
        else: # otherwise, add it to the dictionary
            d[node] = 1
    for k in list(d.keys()):
        print(f'Node ID: {k} (instances {d[k]})')
    print(f'{len(d)} nodes encountered')

#firstNode(packets_time)
#firstNode(packets_rand)
allNodesEncountered(packets_time)
allNodesEncountered(packets_rand)

# At some point afterwards we could do some performance analysis