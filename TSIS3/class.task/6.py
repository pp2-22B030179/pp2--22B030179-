a = int(input()) #size of list
nums = []
primes = []
cnt = 0
for i in range(a):
    nums.append(int(input()))
for i in nums:
    if i != 1:
       for j in range(2, i):
           if i % j == 0:
              cnt += 1
           else:
              continue
       if cnt == 0:
          primes.append(i)
       cnt = 0
    else:
        continue
print(primes)
