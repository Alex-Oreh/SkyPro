lst = []

def add(a):
    lst.append(a)

for i in range(18,1,-4):
    add(i) 
    
for i in range(len(lst)):
    print(lst[i])