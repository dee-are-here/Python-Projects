# This file contains code related to summing and finding
# the maximum of a list of student scores.

student_scores = [78, 65, 89, 86, 55, 91, 64, 89]

# total_exam_score = sum(student_scores)

# sum = 0
# for score in student_scores:
# sum += score

# print(sum)

max_score = 0

for score in student_scores:
    if score > max_score:
        max_score = score

print(max_score)
