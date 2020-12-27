s = str(input("Enter a string:  "))
s = s.upper()
freq = {}

for char in s:
    if char.isalpha():
        freq[char] = 0
for char in s:
    if char.isalpha():
        freq[char] = freq[char] + 1
print("Dictionary:  ", freq)
c = input("Choose a letter:  ")
c = c.upper()
if c in freq:
    print("Frequency count of that letter:  ", freq[c])
    del freq[c]
    print("Dictionary after that letter removed:  ", freq)
else:
    print("Letter not in dictionary")
L = list(freq.keys())
L.sort()
print("Letters sorted:  ", L)