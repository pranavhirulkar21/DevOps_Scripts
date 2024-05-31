
#string Concatination
str1 = "Hello"
str2 = "World"
result = str1+" "+str2
print(result)

#string Length
length = len(result)
print("Length of the Concatination result is :", length)

# UpperCase and LowerCase
upper = result.upper()
lower = result.lower()
print("Result in lower case is :",lower)
print("Result in upper case is :",upper)

#String Replacement
new_result = result.replace("World", "BridgeLabz")
print("New Result : ", new_result)

#String Split
text1 = "Money is Real Power"
words = text1.split()    # It gives the Array of result
print("Words:", words)

#String Strip
text2 = "      Some Spaces Around            "
stripped_text = text2.strip()   # It removes the additional spaces present at the start and end of string 
                                # (Not remove the spaces in between the words)
print("Stripped Text : ",stripped_text)

print("Length of original string : ", len(text2))
print("Length of stripped string : ", len(stripped_text))

#Substring in String
text3 = "Money is Real Power"
substring = "Power"
if substring in text3:
    print(substring, ": Found in String")
else :
    print(substring, ": Not found in String")

