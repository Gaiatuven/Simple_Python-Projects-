# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

total = 0
count = 0

for num in student_heights:
    total += num
    count += 1

avgHeight = round(total / count)
intHeight = int(avgHeight)

print(avgHeight)
