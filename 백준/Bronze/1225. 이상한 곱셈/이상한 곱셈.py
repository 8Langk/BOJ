a, b = input().split()


new_mul_sum=0
sum_a=0

for i in range (len(a)):
    sum_a+=int(a[i])

for i in range (len(b)):
    new_mul_sum+=(sum_a*int(b[i]))
        
print(new_mul_sum)