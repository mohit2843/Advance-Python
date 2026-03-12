s = input("Enter string: ")
vowels = "aeiouAEIOU"
for ch in s:
    if ch not in vowels:
        print(ch, end="")