#Write a python program to implement binary search algorithm

def binary_search(arr, target):

    left, right = 0, len(arr)-1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        elif arr[mid] > target:
            right = mid - 1

        return -1

arr = list(map(int, input("Enter a sorted list (space-separated): ").split()))
target=int(input("enter the number to be searched: "))

index = binary_search(arr, target)

if index != -1:
    print(f"Element {target} found at index {index}.")
else:
    print(f"Element {target} not found.")
        
