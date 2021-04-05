def odd_nums(max_num):
   for num in range(1, max_num + 1, 2):
       yield num
       
odd_to_7 = odd_nums(7)

print(next(odd_to_7))
print(next(odd_to_7))
print(next(odd_to_7))
print(next(odd_to_7))
print(next(odd_to_7))