num = input()
result = int(num[0])
for i in range(1, len(num)): #1~4
    if result <=1 or num[i]<=1:
        result = result + int(num[i])
    else: 
        result = result * int(num[i])

print(result)