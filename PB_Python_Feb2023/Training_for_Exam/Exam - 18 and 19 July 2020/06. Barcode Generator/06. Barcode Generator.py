m = input()
n = input()

count = 0
for i in m:
    if count == 0:
        a = int(i)
    elif count == 1:
        b = int(i)
    elif count == 2:
        c = int(i)
    else:
        d = int(i)
    count+=1
count = 0
for i in n:
    if count == 0:
        a1 = int(i)
    elif count == 1:
        b1 = int(i)
    elif count == 2:
        c1 = int(i)
    else:
        d1 = int(i)
    count+=1
for i in range(a,a1+1):
    for j in range(b,b1+1):
        for k in range(c,c1+1):
            for l in range(d,d1+1):
                if not i%2==0 and not j%2==0 and not k%2==0 and not l%2==0:
                    print(f'{i}{j}{k}{l} ',end='')