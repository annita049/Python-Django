file = open('random.txt','r')
content = file.read()

print(content)

# file pointer to the beginner
file.seek(0)
line = file.readline()
lines = file.readlines()

print(line)
print(lines)

file.close()