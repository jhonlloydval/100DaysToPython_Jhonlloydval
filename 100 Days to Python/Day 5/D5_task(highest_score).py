# DAY 5 TASK
# FINDING THE HIGHEST SCORE

largest_so_far = -1
student_scores = [12, 1, 34, 23, 101, 120, 11, 99, 132, 160, 150, 99, 189, 199, 100, 40, 50, 123]


for score in student_scores:
    if score > largest_so_far:
        largest_so_far = score
    print(score, largest_so_far)
print("The max score is: ",largest_so_far)

# 1-100 SUM
# CARL FRIEDRICH GAUSS PROBLEM
sum = 0
for number in range(1,101):
    sum += number
print(sum)

for x in range(1,101):
    if x%3 == 0 and x%5 == 0:
        x = "FizzBuzz"
    elif x%3 == 0:
        x = "Fizz"
    elif x%5 == 0:
        x = "Buzz"
    print(x)