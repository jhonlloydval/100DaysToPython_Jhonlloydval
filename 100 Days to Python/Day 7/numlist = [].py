numlist = []

while True:
    num = int(input("Enter a number: "))
    numlist.append(num)
    if num == 0:
        break
print(numlist)

div2 = []
div3 = []
div5 = []

for number in numlist:
    if number%2 == 0:
        div2.append(number)
    if number%3 == 0:
        div3.append(number)
    if number%5 == 0:
        div5.append(number)

sum2 = 0
for x in div2:
    sum2 += x

sum3 = 0
for x in div3:
    sum3 += x

sum5 = 0
for x in div5:
    sum5 += x

print(f"The sum of numbers divisible by 2: {sum2} ")        
print(f"The sum of numbers divisible by 3: {sum3}")        
print(f"The sum of numbers divisible by 5: {sum5}")        