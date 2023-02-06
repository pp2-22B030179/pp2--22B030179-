numb = [0 , 2 , 4, 6 , 8]
n = len(numb)
get_sum = sum (numb)
mean = get_sum / n
print(mean)
numb.sort() 
if n % 2 == 0 :
    median1 = numb[n//2]
    median2 = numb[n//2 - 1]
    median = (median1 + median2) / 2
else : 
    median = numb[n//2]
print(median)