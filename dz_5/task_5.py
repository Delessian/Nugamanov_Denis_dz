src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

result = set()
compare = set()
for i in src:
   if i not in compare:
       result.add(i)
   else:
       result.discard(i)
   compare.add(i)

result_ord = [i for i in src if i in result]
  
print(result_ord)
