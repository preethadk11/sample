num=[3,44,5,90,12,8]
max=num[0]
min=num[0]
for i in range(len(num)):
    if num[i]>max:
        max=num[i]
    if num[i]<min:
        min=num[i]
print(max)
print(min)