heights = input("Enter student heights:\n").split()
for x in range(0,len(heights)):
    heights[x]=int(heights[x])
total_height = 0
for n in heights:
    total_height += n
print(f"Total height = {total_height}")
students = 0
for s in heights:
    students += 1
print(f"Total students = {students}")
average_height = round(total_height/students)
print(f"Average height of students is: {average_height}")
    