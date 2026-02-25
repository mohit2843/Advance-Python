#1.find common elements between two lists using sets
list1 = [1, 2, 3, 5,6]
list2 = [5, 6, 7, 8]
common = set(list1) & set(list2)       
print("Common elements between the two lists:", common)

#2.remove duplicates words from a sentence using sets
sentence = "giet university giet"
words = sentence.split()
unique_words = set(words)
print("Unique words in the sentence:", unique_words)

#3.check if two strings are anagrams using sets and logic
str1 = "listen"
str2 = "silent"
set1 = set(str1)
set2 = set(str2)
if set1 == set2 and len(str1) == len(str2):
    print("The two strings are anagrams.")
else:
    print("The two strings are not anagrams.")
    
#4.find elements present in one list but not in second using sets
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
set1 = set(list1)
set2 = set(list2)
diff_elements = set1.difference(set2)
print("Elements present in list1 but not in list2:", diff_elements)

