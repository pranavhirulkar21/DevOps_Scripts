import re

# Finding pattern
text1 = "Money is the real power"
pattern1 = r"real"

search = re.search(pattern1, text1)
if search:
    print("Pattern Found : ", search.group())
else :
    print("Pattern not found!")


# Matching pattern
text2 = "Money is the real power"
pattern2 = r"Money"

match = re.match(pattern2, text2)
if match:
    print("Match Found : ", match.group())
else :
    print("No Match!")

# Replacing pattern
text3 = "The quick brown fox jumps over the lazy brown dog"
pattern3 = r"brown"

replacement = "white"
result = re.sub(pattern3, replacement, text3)
print("modified text : ", result)

# Searching pattern
text4 = "The quick brown fox"
pattern4 = r"brown"

search = re.search(pattern4, text4)
if search:
    print("Pattern found:", search.group())
else:
    print("Pattern not found")


# Spliting pattern
text5 = "apple,banana,orange,grape"
pattern5 = r","

split_result = re.split(pattern5, text5)
print("Split result:", split_result)