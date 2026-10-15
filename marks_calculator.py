
name = input("Enter your name: ")

marks = []

for i in range(1, 4):
    mark = float(input(f"Enter marks for subject {i}: "))
    marks.append(mark)

total = sum(marks)
average = total / 3

print("\n--- Student Report ---")
print("Student:", name)
print("Total:", total, "/ 300")
print("Average:", round(average, 2), "%")

if average >= 40:
    print("Result: Pass")
else:
    print("Result: Needs improvement")
  
