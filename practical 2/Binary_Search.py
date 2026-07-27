# Binary Search in Python

numbers = [10, 20, 30, 40, 50, 60, 70]

target = int(input("Enter the number to search: "))

low = 0
high = len(numbers) - 1

while low <= high:
    mid = (low + high) // 2

    if numbers[mid] == target:
        print("Number found at index", mid)
        break

    elif numbers[mid] < target:
        low = mid + 1

    else:
        high = mid - 1

if low > high:
    print("Number not found")