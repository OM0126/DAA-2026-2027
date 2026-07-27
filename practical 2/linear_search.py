# Linear Search in Python


n = int(input("Enter the number of elements: "))

numbers = []

print("Enter the elements:")
for i in range(n):
    numbers.append(int(input()))

target = int(input("Enter the number to search: "))

found = False

for i in range(n):
    if numbers[i] == target:
        print("Number found at index", i)
        found = True
        break

if found == False:
    print("Number not found")



# Enter the number of elements: 5
# Enter the elements:
# 10
# 20
# 30
# 40
# 50
# Enter the number to search: 30
# Number found at index 2
