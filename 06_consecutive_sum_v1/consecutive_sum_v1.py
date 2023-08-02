limit = int(input("Limit: "))
initial = 1
total_sum = 1

while total_sum < limit:
    initial += 1
    total_sum += initial
    
print(total_sum)