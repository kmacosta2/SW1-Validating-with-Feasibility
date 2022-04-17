#
# CS4310 SW1 Team 5 GGs
l, r, mp = 'lt', 'rt', '20mph'
knownIDs = {
    'lt': 0,
    'rt': 0,
    '20mph': 0
    }

with open('traff_w_time', "r") as f:   # its in hex
    packets_time = f.readlines()       # >25k lines
with open('traff_rand_gen', "r") as f: # its in hex
    packets_rand = f.readlines()       # 20k lines

"""
    By default, this func allows you to collect all instances in a given log file per node and
    collect the total nodes encountered in a dictionary. Alternatively, you could just 
    acknowledge the known IDs only with param which='known'
"""
def nodesEncountered(logFile, le, r, mp, which='all'):
    d = {}
    if which == 'all':
        for l in logFile:
            per_line = l.split(" ")
            node = per_line[2][:3]
            if node in d:   # if already there, then simply update
                d[node] = d[node] + 1
            else:           # otherwise, add it to the dictionary
                d[node] = 1
        for k in list(d.keys()):
            print(f'Node ID: {k} ({d[k]})')
        print(f'{len(d)} nodes encountered')
    elif which == 'known':
        for l in logFile:
            per_line = l.split(" ")
            node = per_line[2][:14]
            if node[:6] == '188#01':
                knownIDs['lt'] += 1
            elif node[:6] == '188#02':
                knownIDs['rt'] += 1
            elif node[:3] == '244' and node[5:14] != '0000000000':
                knownIDs['20mph'] += 1
        print(f'left turn blink: ({knownIDs[le]})\nright turn blink: ({knownIDs[r]})\n20 mph: ({knownIDs[mp]})')

nodesEncountered(packets_time, l, r, mp)
#nodesEncountered(packets_rand, l, r, mp)
nodesEncountered(packets_time, l, r, mp, which='known')
#nodesEncountered(packets_rand, l, r, mp, which='known')