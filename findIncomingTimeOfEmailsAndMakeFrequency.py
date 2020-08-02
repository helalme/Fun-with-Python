# Read the file mbox-short.txt, read incoming time of each email, count the frequency for each hour and print

name = "mbox-short.txt"
fh = open(name)

hour=list()
hrCounts=dict()

for line in fh:
    if not line.startswith("From") : continue
    tmp=line.split()
    if len(tmp)>5:
        time=tmp[5].split(':')
        hour.append(time[0])
    
for hr in hour:
    hrCounts[hr]=hrCounts.get(hr,0)+1

for k,v in sorted(hrCounts.items()): 
    print(k,v)
    
