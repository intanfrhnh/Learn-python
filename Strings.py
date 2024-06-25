testString = "Wingardium Leviosa"

print(testString[2:9])
print(testString[:8])
print(testString[2:])
print(len(testString))

for letter in testString:
    print(letter)

if "Leviosa" in testString:
    print(True)