#1.Find the largest element in a list
nums = [10, 55, 2, 89, 4]
largest = nums[0]
for x in nums:
    if x > largest:
        largest = x
print(largest)

#2.Check if a number is even or odd
num = 7
result = "Even" if num % 2 == 0 else "Odd"      
print(result)

#3.Sum of digits
n = 1234
total = sum(int(digit) for digit in str(n))
print(total)

#4.Swap two variables (without a third)Python
a, b = 5, 10
a, b = b, a
print(a,b)


#5. Fibonacci series up to N terms
n = 5
a, b = 0, 1
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b

 
#6. Reverse a string (without slicing)
s = "Python"
reversed_s = ""
for char in s:
    reversed_s = char + reversed_s
print(reversed_s)



#7. Count vowels
text = "Hello World"
count = sum(1 for char in text.lower() if char in "aeiou")
print(count)



#8. Check if a string is a palindrome
s = "radar"
is_palindrome = s == s[::-1] 
print(is_palindrome)




#9. Count words in a sentence
sentence = "Coding is fun"
word_count = len(sentence.split())
print(word_count)



#10. Check if two strings are anagrams
s1, s2 = "listen", "silent"
is_anagram = sorted(s1) == sorted(s2)
print(is_anagram)


#11Min and Max in a list
nums = [3, 1, 9, 7]
mn, mx = min(nums), max(nums)
print(mn,mx)



#12. Second largest number
nums = [10, 20, 4, 45, 45, 99]
unique_nums = list(set(nums))
unique_nums.sort()
second_largest = unique_nums[-2]
print(second_largest)




#13. Remove duplicates (without set)
nums = [1, 2, 2, 3, 4, 4]
res = []
[res.append(x) for x in nums if x not in res]
print(res)





#14. Count frequency of elements
nums = [1, 2, 1, 3, 2, 1]
freq = {x: nums.count(x) for x in nums}
print(freq)



#15. Merge two sorted lists
l1, l2 = [1, 3, 5], [2, 4, 6]
merged = sorted(l1 + l2)
print(merged)


#16. Rotate a list by k positions
arr = [1, 2, 3, 4, 5]
k = 2
k = k % len(arr)
rotated = arr[-k:] + arr[:-k]
print(rotated)



#17. Flatten a nested list
nested = [[1, 2], [3, 4], [5]]
flat = [item for sublist in nested for item in sublist]
print(flat)




#18. All pairs with a given sum
nums = [1, 2, 3, 4, 5]
target = 5
pairs = [(nums[i], nums[j]) for i in range(len(nums)) for j in range(i+1, len(nums)) if nums[i] + nums[j] == target]
print(pairs)




#19. Check if a number is ArmstrongA number is Armstrong if the sum of its own digits raised to the power of the number of digits equals the number itself ($153 = 1^3 + 5^3 + 3^3$)
num = 153
sum_val = 0
for d in str(num):
    sum_val += int(d) ** len(str(num))

print(sum_val == num)



#20. Right triangle pattern
for i in range(1, 6):
    print("*" * i)
    
    
    
#21. Pyramid pattern
n = 5
for i in range(1, n + 1):
    spaces = " " * (n - i)
    stars = "*" * (2 * i - 1)
    print(spaces + stars)
    
    
#22. Prime numbers in a range
for num in range(2, 20):
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")