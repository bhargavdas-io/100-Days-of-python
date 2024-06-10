student_scores = input("Enter your scores:\n").split()
for n in range(0,len(student_scores)):
    student_scores[n] = int(student_scores[n])

high_score = 0
for x in student_scores:
    if x > high_score:
        high_score = x
print (f"The highest score in the class is: {high_score}")