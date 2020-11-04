from functools import reduce

nums = [1,2,4,5,6,4,2,5,8,9,3,7]

res = list(filter(lambda a: a%2!=0 ,nums))

doubles = list(map(lambda a:a*a, nums))

sum = reduce(lambda a,b: a+b, doubles)

print(res)

print(doubles)

print(sum)