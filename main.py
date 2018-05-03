filename = raw_input('Please enter filename')

file = open(filename, 'r')

l = c = 0

for i in file:
  l += 1
  for j in i:
    if j == " ":
      c += 1
print c+l
