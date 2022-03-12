def fibanocci(p,memo={0:0,1:1,2:1}):
   if p in memo.keys():
      return memo[p]
   x=fibanocci(p-1,memo)+fibanocci(p-2,memo)+fibanocci(p-3,memo)
   memo[p]=x
   return x
print(fibanocci(int(input())))


'''
ip:30
op:29249425
ip:45
op:272809183135
'''
