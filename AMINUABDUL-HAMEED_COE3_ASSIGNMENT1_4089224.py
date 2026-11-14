numbers = [6, 3, 12, 5]
def find_maximum(numbers):
    maximum = numbers[0]
    for number in numbers:
        if number > maximum:
            maximum = number
    return maximum


"""1. Finding the maximum element in an array- The time complexity will
      be O(n): where n represents the numbers of elements in the array.
      The algorithm goes over the entire away only once  and compares 
      each element with the current maximum. The number of comparisons to 
      be done increase linearly """

arr = [5, 6, 7, 5, 8, 5, 9]
target = 5
def cout_occurrences(arr,target):
    count = 0
    for el in arr:
        if el == target:
            count += 1
    return count        

result = cout_occurrences(arr,target)
print(result)


"""2.Counting the occurrence of target elements in an array- The time complexity is Big o(n):
   because the algorithm goes over every element once and checks it against the target variable
   to see if it is the one it seeks. When the number of elements increase, the number of comparisons
   increase linearly."""


numbers = [2, 5, 9, 7, 12]
def is_sorted(numbers):
    for i in range(len(numbers) - 1 ):
        if numbers[i] > numbers[i+1]:
            return False
    return True

print(is_sorted(numbers))

"""3.The algorithm examines n-1 and as such the time complexity will be O(n):
   but if the first element is greater than the second then the time complexity would be O(1). """

grid = [
        [1, 2, 3,], 
        [4, 5, 6], 
        [7, 8, 9] 
        ]

def matrix_sum(grid1):
    total = 0
    for row in grid1:
        for numbers in row:
            total = total + numbers
    return total

print(matrix_sum(grid))
"""The time complexity is O(nxm) for this one."""

digits = [2, 4, 2, 6, 4]
target = 6

def find_pairs(digits, target):
    seen = set()
    pairs = set()
    for digit in digits:
        complement = target - digit
        
        if complement in seen:
            pairs.add(tuple(sorted((digit, complement))))
        seen.add(digit)
    return pairs


print(find_pairs(digits, target))

"""The time complexity for this one is O(n)."""