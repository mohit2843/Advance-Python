#1.common elements between two list using set
list1=[1,2,3,4,5]
list2=[4,5,6,7,8]
set1=set(list1)
set2=set(list2)
common_elements=set1.intersection(set2)
print("Common elements between list1 and list2:",common_elements)

#2.remove duplicates words from a sentence using set
sentence="hello world hello python world"
words=sentence.split()
duplicate_words=set()
seen_words=set()
for word in words:
    if word in seen_words:
        duplicate_words.add(word)
    else:
        seen_words.add(word)
print("Duplicate words in the sentence:",duplicate_words)

#3.check if two strings are anagrams using set and logic
s1= input("Enter first string: ")
s2= input("Enter second string: ")
if len(s1) != len(s2):
    print("The strings are not anagrams.")
else:
    is_anagram = True
    for ch in s1:
        if s1.count(ch) != s2.count(ch):
            is_anagram = False
            break
    if is_anagram:
        print("The strings are anagrams.")
    else:
        print("The strings are not anagrams.")    
        
#4.find elements in first list but not in second list using set
list1=[1,2,3,4,5]
list2=[4,5,6,7,8]
set1=set(list1)
set2=set(list2)
unique_elements=set1.difference(set2)
print("Elements in list1 but not in list2:",unique_elements)

#5.check if all characters in a string are unique using set
s= input("Enter a string: ")
char_set=set()
is_unique=True
for ch in s:
    if ch in char_set:
        is_unique=False
        break
    char_set.add(ch)
if is_unique:
    print("All characters in the string are unique.")
else:
    print("The string contains duplicate characters.")
    
#6.count number of distinct elements in a list using set
list1=[1,2,3,4,5,2,3,1]
distinct_elements=set(list1)
print("Number of distinct elements in the list:",len(distinct_elements))

#7.find symmetric difference betweeen two sets without built in methods
set1={1,2,3,4,5}
set2={4,5,6,7,8}
symmetric_diff=set()
for elem in set1:
    if elem not in set2:
        symmetric_diff.add(elem)
for elem in set2:
    if elem not in set1:
        symmetric_diff.add(elem)
print("Symmetric difference between set1 and set2:",symmetric_diff)

#8.remove common characters from two strings using set
s1= input("Enter first string: ")
s2= input("Enter second string: ")
set1=set(s1)
set2=set(s2)
unique_chars=set1.symmetric_difference(set2)
result=''.join(unique_chars)
print("String after removing common characters:",result)

#9.check if one set is a subset of another set without built in functions
set1={1,2,3}
set2={1,2,3,4,5}
is_subset=True
for elem in set1:
    if elem not in set2:
        is_subset=False
        break
if is_subset:
    print("set1 is a subset of set2.")
else:
    print("set1 is not a subset of set2.")
    
#10.find repeated elements in a list using set
list1=[1,2,3,4,5,2,3,1]
seen=set()
repeated=set()
for elem in list1:
    if elem in seen:
        repeated.add(elem)
    else:
        seen.add(elem)
print("Repeated elements in the list:",repeated)