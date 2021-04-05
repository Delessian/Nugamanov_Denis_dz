src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
src = src[::-1]

result = [
    src[num] for num in range(len(src)) 
    if (num < (len(src)-1)) and (src[num] > src[num+1])
][::-1]

print(result)