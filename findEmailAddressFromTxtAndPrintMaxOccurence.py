# Read the file mbox-short.txt, find the sender email address that occurs maximum. Print that address and occurance

name = "mbox-short.txt"

fh = open(name)
emailAddress=list()
emailCounts=dict()

for line in fh:
    if not line.startswith("From") : continue
    email=line.split()
    emailAddress.append(email[1])

for address in emailAddress:
    emailCounts[address]=emailCounts.get(address,0)+1

largest=0
email=None
for k,v in emailCounts.items(): 
    if v>largest: 
        largest=v
        email=k
        
    
print(email,largest)
