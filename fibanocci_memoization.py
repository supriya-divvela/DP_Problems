def fibanocci(n,mem={1:1,2:1}):
   if n in mem.keys():
      return mem[n]
   x=fibanocci(n-1,mem)+fibanocci(n-2,mem)
   mem[n]=x
   return x
print(fibanocci(int(input())+1))


'''
ip:45
op:1836311903


ip:38
op:63245986
'''
