s = input("Enter string: ")
lower = 0
upper = 0
for ch in s:
    if ch.islower():
        lower += 1
    elif ch.isupper():
        upper += 1
print("Lowercase:", lower)
print("Uppercase:", upper)