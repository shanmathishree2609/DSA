grades = [85, 92, 78, 65, 88, 91, 73, 89, 55, 94]
# Initialize counters
count_A = 0
count_B = 0
count_C = 0
count_below_70 = 0
# Loop through grades and count
for grade in grades:
    if grade >= 90:
        count_A += 1
    elif 80 <= grade <= 89:
        count_B += 1
    elif 70 <= grade <= 79:
        count_C += 1
    else:
        count_below_70 += 1
print("Number of students with grade A (≥90):", count_A)
print("Number of students with grade B (80–89):", count_B)
print("Number of students with grade C (70–79):", count_C)
print("Number of students with grade below 70:", count_below_70)
