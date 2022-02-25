def func(n,l):
    m=[]
    for i in range(n+1):
        m.append([])
    m[0]=[[]]
    for i in range(len(m)):
        for j in l:
            if i+j<len(m):
                for k in m[i]:
                    temp=k.copy()
                    temp.append(j)
                    temp.sort()
                    if temp in m[i+j]:pass
                    else:m[i+j].append(temp)
    return len(m[n])
n,k=map(int,input().split())
l=[int(x) for x in input().split()]
print(func(n,l))
