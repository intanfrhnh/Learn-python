testString = "Wingardium Leviosa"

print(testString[2:9])
print(testString[:8])
print(testString[2:])
print(len(testString))

for letter in testString:
    print(letter)

if "Leviosa" in testString:
    print(True)

#To upper case and lower case
print(testString.upper())
print(testString.lower())

#Remove whitespace
print(testString.strip())

#replace String
print(testString.replace("i","o"))

#split String
print(testString.split(" "))