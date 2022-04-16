# -Identify how many different IDs exist in a given log file & their # of instances 
# -When working with cangen(random) traffic lets identify 
#       left/right turn signal--> ID 188#01...for left & ID 188#02...right
#        & 20 mph--> ID 244#...followed by any value above 0 will register
#        on the speedometer
# traff_w_time recorded the following event: right signal(x2), left signal(x1),
# then accel to 20 then drop to zero

knownIDs = {
    'lt':'188#01',
    'rt':'188#02',
    '20mph':'244'
    }
# the 10 bits that follow the mph would need to be above 0

with open('traff_w_time', "r") as f:   # its in hex
    packets_time = f.readlines()                  # >25k lines
with open('traff_rand_gen', "r") as f: # its in hex
    packets_rand = f.readlines()                  # 20k lines

def allNodesEncountered(logFile):
    d = dict()
    for l in logFile:
        per_line = l.split(" ")
        node = per_line[2][:3]
        if node in d:# if already there, then simply update
            d[node] = d[node] + 1
        else: # otherwise, add it to the dictionary
            d[node] = 1
    for k in list(d.keys()):
        print(f'Node ID: {k} ({d[k]})')
    print(f'{len(d)} nodes encountered')

def identifyingTheSequence():
    print('')
    return ''

#firstNode(packets_time)
#firstNode(packets_rand)
allNodesEncountered(packets_time)
allNodesEncountered(packets_rand)