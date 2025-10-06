# 🔍 Problem 1: Find Most Frequent Element
# Given a list of integers, return the value that appears most frequently.
# If there's a tie, return any of the most frequent.
#
# Example:
# Input: [1, 3, 2, 3, 4, 1, 3]
# Output: 3
num=[1, 3, 2, 3, 4, 1, 3]
def most_frequent(numbers):
    return max(set(numbers),key=numbers.count) #checks unique numbers using set() and uses numbers.count to count # of appearances

# print(most_frequent(num))

"""
Time and Space Analysis for problem 1:
- Best-case: All numbers are the same. Set()  gets the unique  numbers and checks through  the code once. O(n)
- Worst-case: 
- Average-case: Some numbers repeat like this problem. Set gets unique numbers and count() loops through to find number of occurances. O(n2)
- Space complexity: Uses space to store unique numbers
- Why this approach? : It is simple and readable and usues python built-in functions( max(), and couny())
- Could it be optimized? Yes, can be optimized to be O(n)
"""


# 🔍 Problem 2: Remove Duplicates While Preserving Order
# Write a function that returns a list with duplicates removed but preserves order.
#
# Example:
# Input: [4, 5, 4, 6, 5, 7]
# Output: [4, 5, 6, 7]

number=[4, 5, 4, 6, 5, 7]

def remove_duplicates(nums):
    seen = set()
    result = []
    for num in nums:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result


"""
Time and Space Analysis for problem 2:
- Best-case: There are no duplicates. O(n) time and O(n) space
- Worst-case: All elements are duplicates or all unique. O(n) time and O(n) space
- Average-case: A mix of unique and duplicate values. Still O(n) time and O(n) space
- Space complexity: O(n)
- Why this approach? This approach because set() does not allow  duplicates
- Could it be optimized? This is efficient 
"""


# 🔍 Problem 3: Return All Pairs That Sum to Target
# Write a function that returns all unique pairs of numbers in the list that sum to a target.
# Order of output does not matter. Assume input list has no duplicates.
#
# Example:
# Input: ([1, 2, 3, 4], target=5)
# Output: [(1, 4), (2, 3)]

def find_pairs(nums, target):
    # Your code here
    pairs=[]
    for i  in range(len(nums)): #length=5, i=0,1,2,3,4
        for j in range(i+1,len(nums)): #length=5, j=i+1
            if nums[i]+nums[j]==target: #e.g. if i in nums[i] is 0,then nums[i]== 1 etc 
               pairs.append((nums[i],nums[j]))
    return pairs
num1=[1, 2, 3, 4]           
print(find_pairs(num1,5))

"""
Time and Space Analysis for problem 3:
- Best-case: Input is small like less than the current. Can be O(1)
- Worst-case: Input increases and number of operations increase because of loops. O(n2) time and space.
- Average-case: O(n2) space and time. Input increasing slightly increases operation time.
- Space complexity: O(n)
- Why this approach? It was easy to implement with loops
- Could it be optimized? Yes
"""


# 🔍 Problem 4: Simulate List Resizing (Amortized Cost)
# Create a function that adds n elements to a list that has a fixed initial capacity.
# When the list reaches capacity, simulate doubling its size by creating a new list
# and copying all values over (simulate this with print statements).
#
# Example:
# add_n_items(6) → should print when resizing happens.

def add_n_items(n):
    lst=[]
    capacity=1
    size=0
    
    print(f"Initial capacity={capacity}")
    for i in range(n):
        lst.append(i)
        size=size+1
        if size==capacity:
            print(f"Resizing from {capacity} to {capacity*2}")
            capacity*=2
        print(f"Added item {i}, size = {size}, capacity = {capacity}")

    print(f"Final list:", lst)
    print(f"Final size = {size}, Final capacity = {capacity}")


add_n_items(5)

"""
Time and Space Analysis for problem 4:
- When do resizes happen? Happens whenever size==capacity
- What is the worst-case for a single append? O(n)
- What is the amortized time per append overall? O(1)
- Space complexity: o(n)
- Why does doubling reduce the cost overall? doubling increases space and saves time overall.
"""


# 🔍 Problem 5: Compute Running Totals
# Write a function that takes a list of numbers and returns a new list
# where each element is the sum of all elements up to that index.
#
# Example:
# Input: [1, 2, 3, 4]
# Output: [1, 3, 6, 10]
# Because: [1, 1+2, 1+2+3, 1+2+3+4]

test=[1, 2, 3, 4]

def running_total(nums):
    new_lst = []
    total = 0
    for i in range(len(nums)):
        total = total + nums[i]      # keep adding each element
        new_lst.append(total) # append running sum
    return new_lst
print(running_total(test))

"""
Time and Space Analysis for problem 5:
- Best-case: O(n)
- Worst-case:  O(n)
- Average-case:O(n)
- Space complexity: O(n)
- Why this approach? easy to implement, and no nested  loops
- Could it be optimized? Yes, by updating the list instead of creating a new one
"""
