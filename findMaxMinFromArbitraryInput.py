# Find maximum and minimum numbers from arbitrary user input. User can enter anyting.
# No header/library can be used
# No complex types like list, tuple can be used
# No ready functions like isnumeric(), isdigit() can be used. (Only input(), float() or int() can be used 
# Type "done" at the end

largest = smallest = None
i=0

while i>=0:
    num = input("Enter anything: ")
    if num == "done" : break
    try:
        num=float(num)
        if i==0: 
          largest=num
          smallest=num
        i=i+1
    except:
        print('Warning: non-numeric value')
        continue
    
    if num>largest: largest=num
    elif num<smallest: smallest=num
    else: pass
    
print("Maximum is", largest)
print("Minimum is", smallest)
