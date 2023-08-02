limit = int(input("Limit: "))
initial = 1
string = '1'
total_sum = 1

while total_sum < limit:
    initial += 1
    total_sum += initial
    string += f" + {initial}" 
    
print(f"The consecutive sum: {string} = {total_sum}")